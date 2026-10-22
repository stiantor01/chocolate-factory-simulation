#!/usr/bin/env python3
from ament_index_python.packages import get_package_share_directory

import math
import random
import time
import subprocess
from pathlib import Path

# Dimensjoner i meter
BELT_WIDTH = 0.38
MARGIN = 0.03
CHOCOLATE_LENGTH = 0.262
CHOCOLATE_WIDTH = 0.077

# Transportbåndets posisjon
BELT_X = 1.0
BELT_Y = -2.0


def spawn_chocolate():
    # Tilfeldig rotasjon
    yaw = random.uniform(-math.pi / 2, math.pi / 2)

    # Beregn hvor mye plass platen tar langs X
    occupied_width = (
        CHOCOLATE_LENGTH * abs(math.cos(yaw))
        + CHOCOLATE_WIDTH * abs(math.sin(yaw))
    )

    # Beregn maksimal sideforskyvning
    max_offset = max(
        0.0,
        (BELT_WIDTH - 2 * MARGIN - occupied_width) / 2
    )

    x_offset = random.uniform(-max_offset, max_offset)

    # Spawn nær starten av båndet
    x = BELT_X + x_offset
    y = BELT_Y - 1.8
    z = 0.85

    model_path = (
        Path(get_package_share_directory("chocolate_factory_sim")) / "models/chocolate_bar/model.sdf"
    )

    model_name = f"chocolate_bar_{random.randint(100000, 999999)}"

    print(f"Rotasjon: {math.degrees(yaw):.1f}°")
    print(f"Sideforskyvning: {x_offset * 100:.1f} cm")
    print(f"Posisjon: X={x:.3f}, Y={y:.3f}, Z={z:.3f}")

    subprocess.run([
        "ros2", "run", "ros_gz_sim", "create",
        "-world", "chocolate_factory",
        "-name", model_name,
        "-file", str(model_path),
        "-x", str(x),
        "-y", str(y),
        "-z", str(z),
        "-Y", str(yaw)
    ], check=True)


def main():
    print("Automatisk spawning startet. Trykk Ctrl+C for å stoppe.")

    try:
        while True:
            spawn_chocolate()
            delay = random.uniform(0.8, 1.5)
            print(f"Neste plate om {delay:.1f} sekunder", flush=True)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nSpawning stoppet.")


if __name__ == "__main__":
    main()

