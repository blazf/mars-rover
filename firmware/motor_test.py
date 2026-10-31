# Mars rover - slow motor test. Run from the Mac with WHEELS OFF THE TABLE:
#
#   mpremote run firmware/motor_test.py
#
# Each step runs 2 s at SPEED %, then everything stops.

from machine import Pin, PWM
import utime

SPEED = 30  # percent

pwm1 = PWM(Pin(2)); dir1 = Pin(3, Pin.OUT, value=0)  # left
pwm2 = PWM(Pin(6)); dir2 = Pin(7, Pin.OUT, value=0)  # right
for p in (pwm1, pwm2):
    p.freq(20000)  # MDD20A max PWM frequency, quiet
    p.duty_u16(0)


def side(pwm, dir_pin, speed):
    """speed -100..100; negative = backward."""
    dir_pin.value(1 if speed < 0 else 0)
    pwm.duty_u16(abs(speed) * 65535 // 100)


def stop():
    side(pwm1, dir1, 0)
    side(pwm2, dir2, 0)


STEPS = [
    ("left forward", SPEED, 0),
    ("left backward", -SPEED, 0),
    ("right forward", 0, SPEED),
    ("right backward", 0, -SPEED),
    ("both forward", SPEED, SPEED),
    ("spin (left fwd, right back)", SPEED, -SPEED),
]

try:
    for name, left, right in STEPS:
        print(name)
        side(pwm1, dir1, left)
        side(pwm2, dir2, right)
        utime.sleep(2)
        stop()
        utime.sleep(1)
finally:
    stop()
    print("stopped")
