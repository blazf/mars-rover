# Mars rover - drive firmware (runs automatically when the Pico powers up)
#
# Motors start stopped. The Mac sends text lines over USB:
#
#   D <left> <right>   drive, each side -100..100 (negative = backward)
#   S                  stop now
#   P                  ping, answers PONG
#
# Watchdog: if no D command arrives for 300 ms, the motors stop. So if the
# Mac script crashes or the cable comes out, the rover halts by itself.
#
# MDD20A truth table: PWM low = brake, PWM high + DIR low = forward,
# PWM high + DIR high = backward.

import sys
import uselect
import utime
from machine import Pin, PWM

WATCHDOG_MS = 300
RAMP_STEP = 10      # max speed change (%) per tick, 0 -> 100 % takes 0.2 s
TICK_MS = 20

# Pico pin -> MDD20A input (see docs/wiring.md). Pins go low before PWM starts.
dir1 = Pin(3, Pin.OUT, value=0)  # left direction
dir2 = Pin(7, Pin.OUT, value=0)  # right direction
pwm1 = PWM(Pin(2, Pin.OUT, value=0))  # left speed
pwm2 = PWM(Pin(6, Pin.OUT, value=0))  # right speed
for p in (pwm1, pwm2):
    p.freq(20000)  # MDD20A max PWM frequency, quiet
    p.duty_u16(0)

# Onboard LED on = firmware running
Pin(25, Pin.OUT, value=1)


def apply(pwm, dir_pin, speed):
    dir_pin.value(1 if speed < 0 else 0)
    pwm.duty_u16(abs(speed) * 65535 // 100)


def clamp(v):
    return max(-100, min(100, v))


def ramp(current, target):
    if target > current:
        return min(target, current + RAMP_STEP)
    return max(target, current - RAMP_STEP)


target = [0, 0]
current = [0, 0]
last_cmd = utime.ticks_ms()
last_tick = last_cmd

poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)

print("Rover ready")

try:
    while True:
        if poll.poll(TICK_MS):
            parts = sys.stdin.readline().split()
            if parts and parts[0] == "D" and len(parts) == 3:
                try:
                    target = [clamp(int(parts[1])), clamp(int(parts[2]))]
                    last_cmd = utime.ticks_ms()
                except ValueError:
                    pass
            elif parts and parts[0] == "S":
                target = [0, 0]
                current = [0, 0]
            elif parts and parts[0] == "P":
                print("PONG")

        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_cmd) > WATCHDOG_MS:
            target = [0, 0]
            current = [0, 0]  # stop at once, no ramp
        if utime.ticks_diff(now, last_tick) >= TICK_MS:
            last_tick = now
            current = [ramp(current[0], target[0]), ramp(current[1], target[1])]
        apply(pwm1, dir1, current[0])
        apply(pwm2, dir2, current[1])
finally:
    apply(pwm1, dir1, 0)
    apply(pwm2, dir2, 0)
