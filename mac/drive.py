"""Drive the rover from the Mac with an Xbox controller.

    pip install -r mac/requirements.txt
    python mac/drive.py
    python mac/drive.py --max 50    # raise the speed cap (default is DEFAULT_MAX)

Controls:
    left stick up/down    forward / backward
    left stick left/right turn
    hold RB               turbo (full speed)
    B                     stop (hold)

Sends "D <left> <right>" to the Pico 25 times a second. If this script stops,
the Pico's watchdog halts the motors within 0.3 s.
"""

import argparse
import glob
import sys
import time

import pygame
import serial
from pygame._sdl2 import controller

NORMAL_SPEED = 50   # % at full stick
TURBO_SPEED = 100
DEFAULT_MAX = 20    # % cap while testing on the cable; raise with --max
DEADZONE = 0.12
SEND_HZ = 25


def find_port():
    ports = glob.glob("/dev/cu.usbmodem*")
    if not ports:
        sys.exit("Pico not found. Is the USB cable plugged in?")
    return ports[0]


def axis(pad, which):
    v = pad.get_axis(which) / 32767
    if abs(v) < DEADZONE:
        return 0.0
    return max(-1.0, min(1.0, v))


def mix(throttle, turn, max_speed):
    """Arcade drive: stick up/down is speed, left/right is turning."""
    left = throttle + turn
    right = throttle - turn
    biggest = max(1.0, abs(left), abs(right))
    return (round(left / biggest * max_speed),
            round(right / biggest * max_speed))


def wait_for_controller():
    print("Waiting for Xbox controller (pair it with the Mac or plug it in)...")
    while True:
        pygame.event.pump()
        if controller.get_count() > 0:
            pad = controller.Controller(0)
            print("Controller:", pad.name)
            return pad
        time.sleep(0.5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=None, help="serial port of the Pico")
    parser.add_argument("--max", type=int, default=DEFAULT_MAX,
                        help="speed cap in %% for everything, turbo included (e.g. --max 10 for testing)")
    args = parser.parse_args()
    normal_speed = min(NORMAL_SPEED, args.max)
    turbo_speed = min(TURBO_SPEED, args.max)
    print(f"Speed: {normal_speed} %, turbo {turbo_speed} %")

    port = args.port or find_port()
    link = serial.Serial(port, 115200, timeout=0.5)
    link.write(b"P\n")
    time.sleep(0.3)
    print("Pico on", port, "-", link.read(link.in_waiting).decode(errors="ignore").strip() or "(no reply yet)")

    pygame.init()
    controller.init()
    pad = wait_for_controller()

    last = (None, None)
    try:
        while True:
            pygame.event.pump()
            if not pad.attached():
                link.write(b"S\n")
                pad = wait_for_controller()

            if pad.get_button(pygame.CONTROLLER_BUTTON_B):
                left, right = 0, 0
            else:
                max_speed = turbo_speed if pad.get_button(pygame.CONTROLLER_BUTTON_RIGHTSHOULDER) else normal_speed
                throttle = -axis(pad, pygame.CONTROLLER_AXIS_LEFTY)  # stick up = negative
                turn = axis(pad, pygame.CONTROLLER_AXIS_LEFTX)
                left, right = mix(throttle, turn, max_speed)

            link.write(f"D {left} {right}\n".encode())
            if (left, right) != last:
                print(f"\rleft {left:4d}  right {right:4d}", end="", flush=True)
                last = (left, right)
            time.sleep(1 / SEND_HZ)
    except KeyboardInterrupt:
        pass
    finally:
        link.write(b"S\n")
        link.close()
        print("\nStopped.")


if __name__ == "__main__":
    main()
