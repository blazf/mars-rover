# Power and LiPo safety

![Our battery: Lectron Pro 2S 7.4 V 2000 mAh 25C with XT60 plug](images/2026-10-18-lipo-battery.jpg)

## Our battery

| Spec | Value | Meaning |
|---|---|---|
| Type | LiPo, 2S (two cells) | Light and powerful, but needs careful handling |
| Voltage | 7.4 V nominal | **8.4 V full**, 7.6 V storage, **stop at ~7.0 V** |
| Capacity | 2000 mAh | Roughly 30–60 min of normal driving |
| Discharge | 25C | 25 × 2 A = 50 A burst — plenty for six motors |
| Plug | XT60 (female on battery) | Only fits one way round |

## LiPo rules

1. **Never run it flat.** Stop at about 3.5 V per cell while driving (7.0 V total). Over-drained LiPos can swell and become dangerous.
2. **Always use the alarm.** Plug the LiPo alarm into the balance lead (black wire to the "−" pin), set it to 3.5 V. When it beeps — stop driving.
3. **Charge only with a LiPo balance charger**, on a hard surface, in a LiPo safe bag, and never leave it charging unattended.
4. **Store at half charge** (about 7.6 V) if it won't be used for a week. Most chargers have a "storage" mode.
5. **Puffy battery = retire it.** Take swollen packs to battery recycling.
6. **Unplug the battery when you're done.** Also unplug the alarm — it slowly drains the battery.

## Pre-drive checklist

- [ ] Battery voltage on the alarm display is above 7.6 V
- [ ] Alarm plugged in and set to 3.5 V
- [ ] Fuse in place (20 A, yellow)
- [ ] No loose wires near the wheels or chassis joints
- [ ] First test with the wheels off the ground

## Why each protection part is there

| Part | Protects against |
|---|---|
| **XT60 connector** | Plugging the battery in backwards (would destroy the MDD20A, which has no reverse protection of its own). |
| **20 A fuse** | A short circuit melting wires or starting a fire. Without a fuse, a LiPo can push 50 A+ into a short. |
| **Power switch (Pololu HP)** | Turning off without unplugging; second layer of reverse protection; lets the Pico cut power on low battery. |
| **LiPo alarm** | Over-discharging the battery. |
| **MDD20A current limiting** | The driver protects itself when the wheels stall. |

## Order of operations

- **Connecting:** wire everything else first, battery **last**.
- **Disconnecting:** battery **first**, then touch wires.
