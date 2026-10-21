# Chocolate Factory Simulation

ROS 2 Jazzy and Gazebo simulation of a chocolate production line.

## Packages
- chocolate_factory_sim: Gazebo world, conveyor belts and factory floor
- chocolate_robot_description: Robot URDF and 3D models

## Requirements
- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Sim
- ros_gz_sim

## Installation

Before starting, make sure Ubuntu 24.04 and ROS 2 Jazzy are installed.

Install the required tools:

    sudo apt update
    sudo apt install -y git python3-colcon-common-extensions python3-rosdep ros-jazzy-ros-gz

If rosdep has not been initialized:

    sudo rosdep init
    rosdep update

Note: Run `source ~/ros2_ws/install/setup.bash` in every new terminal before launching the simulation.


1. Create a workspace and clone the repository:

    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone https://github.com/stiantor01/chocolate-factory-simulation.git

2. Install dependencies and build:

    source /opt/ros/jazzy/setup.bash
    cd ~/ros2_ws
    rosdep install --from-paths src --ignore-src -r -y
    colcon build --symlink-install
    source install/setup.bash

3. Launch Gazebo:

    ros2 launch chocolate_factory_sim chocolate_factory.launch.py

## Simulation

The floor, foundation and conveyor belts are static.
The robot base is fixed to the world.
The five robot joints remain movable.
