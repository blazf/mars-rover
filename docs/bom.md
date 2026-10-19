# Bill of materials

Status: ✅ have · 📦 ordered · ⏳ later phase

## Chassis and drive

| Part | Qty | Why | Status |
|---|---|---|---|
| DAGU Wild Thumper 6WD chassis with 6 gearmotors | 1 | The rover body. Motors are rated for about 7.2 V; each draws ~0.4 A free-running and up to **6.6 A when stalled** ([Pololu](https://www.pololu.com/product/1561)). | ✅ |
| [Cytron MDD20A](https://thepihut.com/collections/cytron/products/20a-6v-30v-2-channel-dc-motor-driver) dual motor driver | 1 | Two channels (left side, right side), **20 A per channel**, works with the Pico's 3.3 V signals. Three stalled motors on one side can draw ~20 A, so smaller drivers (L298N etc.) are not enough. | 📦 |

## Power

| Part | Qty | Why | Status |
|---|---|---|---|
| Lectron Pro 2S LiPo, 7.4 V 2000 mAh 25C, XT60 | 1 | Main battery. 25C × 2 Ah = 50 A burst, enough for all motors. | ✅ |
| XT60 male connector (rover side) | 1 | Matches the battery. Only fits one way round, which protects the motor driver from a reversed battery. Unplugging it is the off switch until the power switch arrives. | 📦 |
| Inline ATO/ATC blade fuse holder, 12 AWG, with fuse assortment (5–40 A) | 1 pack of 4 | **20 A fuse (yellow)** on the main line protects the wiring from a short. Small fuses (5–10 A) are for Phase 2/3 circuits. Do **not** use the 30/40 A fuses on this rover. | 📦 |
| [Pololu #2813](https://www.pololu.com/product/2813) Big Pushbutton Power Switch, HP (16 A) | 1 | Main power switch: push on, push off, reverse-battery protection, and the Pico can switch it off on low battery. Backordered — fallback is a BEP 20 A @ 12 V DC rocker. | 📦 |
| 16 AWG silicone wire, red and black | ~1 m each | Battery → fuse → switch → driver → motors. | 📦 |
| LiPo voltage checker / alarm (BX100 type, 1–8S) | 2 | Plugs into the balance lead and beeps when a cell drops below the set voltage (set to **3.5 V**). | 📦 |
| 5 V 3 A buck converter / UBEC | 1 | Powers the Pico from the battery in Phase 2. | 📦 |

## Electronics

| Part | Qty | Why | Status |
|---|---|---|---|
| Raspberry Pi Pico (RP2040, headers soldered) | 1 | Brains for Phase 1. | ✅ |
| SunFounder Thales kit | 1 | Breadboard, jumper wires, resistors (battery voltage divider), potentiometer (manual motor test), buzzer (horn), WS2812 strip (lights), I2C LCD1602 (status display), 9g servo (Phase 3 prototyping). | ✅ |
| Raspberry Pi Pico 2 W | 1 | Drop-in wireless replacement for Phase 2. | ⏳ |

![Thales kit packing list](images/2026-10-17-thales-kit-parts.jpg)

## Later phases

| Part | Why | Status |
|---|---|---|
| PCA9685 16-channel servo driver | Drives arm servos over I2C. | ⏳ |
| 6 V, 5 A+ UBEC | Separate power for servos. | ⏳ |
| Robotic arm kit / servos | Phase 3 payload. | ⏳ |

## Parts we considered and rejected

| Part | Why not |
|---|---|
| L298N motor driver | ~2 A per channel — far too weak for three motors per side. |
| Cytron MDD10A | Works on flat ground, but little margin when wheels get stuck. |
| Small KCD1 / SparkFun rocker switches as main switch | Rated ~6–16 A **AC**; too weak for 20 A DC. Fine as a control switch for a Pololu MOSFET switch. |
| Pololu #2812 (MP, 8 A) power switch | Too small for skid-steer turns on carpet. Only the HP versions (#2813, #2815) are strong enough. |
| 5×20 mm glass fuse holders | Holders rated ~10–15 A; fine for small circuits, not the main line. |
