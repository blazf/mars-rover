# Mars rover - safe boot (runs automatically when the Pico powers up)
#
# Holds both motor channels stopped, so nothing moves when the battery is
# plugged in. Then exits, leaving the REPL free for testing from the Mac.
#
# MDD20A truth table: PWM low = brake, PWM high + DIR low = forward,
# PWM high + DIR high = backward.

from machine import Pin

# Pico pin -> MDD20A input (see docs/wiring.md)
PWM1 = Pin(2, Pin.OUT, value=0)  # left speed
DIR1 = Pin(3, Pin.OUT, value=0)  # left direction
PWM2 = Pin(6, Pin.OUT, value=0)  # right speed
DIR2 = Pin(7, Pin.OUT, value=0)  # right direction

# Onboard LED on = safe boot ran
Pin(25, Pin.OUT, value=1)

print("Rover: motors stopped (safe boot)")
