
## Conveyor speed and chocolate spawning

The conveyor simulation is configured according to ELE208 Robot Design Challenge 5.

- Target conveyor speed: 0.3 m/s
- Movement method: Force-based velocity regulation
- Chocolate spawning interval: Randomly between 0.8 and 1.5 seconds
- Chocolate positions: Randomized across the conveyor width
- Chocolate orientation: Randomized around the vertical axis

Configuration files:
- Conveyor speed: chocolate_conveyor/src/conveyor_system.cpp
- Spawning interval: chocolate_factory_sim/chocolate_factory_sim/spawn_chocolate.py

The simulation has been visually tested with these settings.
The actual conveyor speed has not yet been quantitatively verified.
