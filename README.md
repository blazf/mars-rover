# Mars Rover 🚀

A parent-and-kid project: a six-wheeled Mars-style rover built on a DAGU Wild Thumper 6WD chassis, driven by a Raspberry Pi Pico and controlled with an Xbox controller through an iPhone.

![The chassis with all six motors wired to a terminal strip](docs/images/2026-10-18-chassis-wired.jpg)

## Phases

| Phase | Goal | Status |
|---|---|---|
| **1. Drive** | Pico drives both sides of the rover; Xbox controller → iPhone → Mac → Pico (USB) | 🛒 Parts ordered |
| **2. Wireless** | Swap in a wireless Pico (Pico 2 W) so the iPhone talks to the rover directly; Pico powered from the battery | ⏳ Planned |
| **3. Payload** | Add things on top (e.g. a robotic arm) controlled by the Pico and the Xbox controller | ⏳ Planned |

## What's here

| Document | What it covers |
|---|---|
| [Architecture](docs/architecture.md) | How the pieces talk to each other, per phase |
| [Bill of materials](docs/bom.md) | Every part, why we picked it, and its status |
| [Wiring](docs/wiring.md) | Wiring diagram and Pico pinout |
| [Power & LiPo safety](docs/power-and-safety.md) | Battery rules, fuse, switch, alarm, and why they matter |
| [Build log](docs/build-log.md) | Dated diary of what we did, with photos |

## Repository layout

```
├── README.md
├── docs/                 # documentation + photos
├── hardware/wiring/      # WireViz source (rover.yml) and rendered diagrams
├── firmware/pico/        # MicroPython for the Pico          (coming soon)
├── bridge/mac/           # Mac ↔ Pico relay for Phase 1      (coming soon)
└── app/ios/              # iPhone app + Xbox controller      (coming soon)
```

## Rendering the wiring diagram

The wiring diagram is written as text in [`hardware/wiring/rover.yml`](hardware/wiring/rover.yml) using [WireViz](https://github.com/wireviz/WireViz). After editing it, regenerate the images:

```bash
brew install graphviz
pip install wireviz
wireviz hardware/wiring/rover.yml
```
