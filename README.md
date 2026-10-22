# Chocolate Factory Simulation

ROS 2 Jazzy and Gazebo Harmonic simulation of a chocolate production line.

## Packages

- `chocolate_factory_sim` - Gazebo world, models and automatic chocolate spawning
- `chocolate_conveyor` - Custom Gazebo plugin for conveyor movement
- `chocolate_robot_description` - Robot URDF and 3D models

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic
- ros_gz_sim
- Python 3
- colcon

## Installation

Install the required tools:

    sudo apt update
    sudo apt install -y git python3-colcon-common-extensions python3-rosdep ros-jazzy-ros-gz

Initialize rosdep if necessary:

    sudo rosdep init
    rosdep update

Clone the repository:

    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone https://github.com/stiantor01/chocolate-factory-simulation.git

Install dependencies and build:

    source /opt/ros/jazzy/setup.bash
    cd ~/ros2_ws
    rosdep install --from-paths src --ignore-src -r -y
    colcon build --symlink-install
    source ~/ros2_ws/install/setup.bash

## Running the Simulation

Use two separate Ubuntu terminals.

### Terminal 1 - Start Gazebo

    source /opt/ros/jazzy/setup.bash
    source ~/ros2_ws/install/setup.bash
    export GZ_SIM_SYSTEM_PLUGIN_PATH="$HOME/ros2_ws/install/chocolate_conveyor/lib:${GZ_SIM_SYSTEM_PLUGIN_PATH}"
    ros2 launch chocolate_factory_sim chocolate_factory.launch.py

### Terminal 2 - Spawn Chocolate Bars

    source /opt/ros/jazzy/setup.bash
    source ~/ros2_ws/install/setup.bash
    ros2 run chocolate_factory_sim spawn_chocolate

Chocolate bars spawn automatically at randomized intervals of 3-8 seconds.

Press Ctrl+C to stop spawning.

## Conveyor System

The custom conveyor plugin:

- Moves chocolate bars using physical forces.
- Targets a conveyor speed of approximately 0.5 m/s.
- Allows chocolate bars to fall naturally from the conveyor.
- Automatically removes chocolate bars after they fall below a defined height.

## Updating the Project

From a cloned repository:

    cd ~/ros2_ws/src/chocolate-factory-simulation
    git pull origin main

    cd ~/ros2_ws
    source /opt/ros/jazzy/setup.bash
    colcon build --symlink-install
    source ~/ros2_ws/install/setup.bash

Restart Gazebo after rebuilding.

## Simulation Notes

- The factory floor and conveyor structures are static.
- Chocolate bars are dynamic physics objects.
- The robot base is fixed to the world.
- The robot has five movable joints.

## Development

The project is under active development.

Planned features include robot control, chocolate detection and automated pick-and-place operations.

## Chocolate tracking (ROS 2)

The C++ tracking node reads chocolate bar poses from Gazebo
and publishes them to ROS 2.

### Packages

- chocolate_interfaces: Custom ROS 2 message definitions.
- chocolate_tracking: Gazebo-to-ROS 2 tracking node.

### Published topic

Topic: /chocolate/poses
Type: chocolate_interfaces/msg/ChocolatePoseArray

Each chocolate bar includes:
- Name
- Gazebo entity ID
- XYZ position in meters
- Quaternion orientation (X, Y, Z, W)

Only entities starting with chocolate_bar_ are published.

### Build

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
colcon build --symlink-install --packages-up-to chocolate_tracking
source ~/ros2_ws/install/setup.bash
```

### Terminal 1 - Gazebo

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
export GZ_SIM_SYSTEM_PLUGIN_PATH="$HOME/ros2_ws/install/chocolate_conveyor/lib:${GZ_SIM_SYSTEM_PLUGIN_PATH}"
ros2 launch chocolate_factory_sim chocolate_factory.launch.py
```

### Terminal 2 - Spawn chocolate bars

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run chocolate_factory_sim spawn_chocolate
```

### Terminal 3 - Tracking

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run chocolate_tracking chocolate_tracking_node
```

### Terminal 4 - Inspect ROS 2 data

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 topic echo /chocolate/poses --once
```
