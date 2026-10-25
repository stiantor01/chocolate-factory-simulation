# Chocolate Factory Simulation

ROS 2 Jazzy and Gazebo Harmonic.

## Setup

Clone the repository:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/stiantor01/chocolate-factory-simulation.git
```

Install dependencies and build:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

## Start simulation

**Terminal 1 – Gazebo**

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
export GZ_SIM_SYSTEM_PLUGIN_PATH="$HOME/ros2_ws/install/chocolate_conveyor/lib:${GZ_SIM_SYSTEM_PLUGIN_PATH}"

ros2 launch chocolate_factory_sim chocolate_factory.launch.py
```

**Terminal 2 – Chocolate spawning**

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run chocolate_factory_sim spawn_chocolate
```

**Terminal 3 – Chocolate tracking (optional)**

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run chocolate_tracking chocolate_tracking_node
```

Chocolate positions are published on `/chocolate/poses`.

## Robot control

The robot uses `ros2_control`. Both controllers start automatically with Gazebo.

**Action Server:**

```text
/arm_controller/follow_joint_trajectory
```

**Action type:**

```text
control_msgs/action/FollowJointTrajectory
```

**Joint names (in order):**

```text
joint_1
joint_2
joint_3
joint_4
joint_5
```

**Home position (radians):**

```text
[-0.785398, 0, -1.221730, -1.221730, 0]
```

Check that the controllers are running:

```bash
ros2 control list_controllers
ros2 action list -t
```

## MATLAB

MATLAB connects to the ROS 2 Action Server to send joint trajectories.

Use the same `ROS_DOMAIN_ID` on both machines (currently `15`). The machines must be able to communicate over the network.

Example MATLAB setup:

```matlab
setenv('ROS_DOMAIN_ID', '15');

node = ros2node("/matlab_controller");
client = ros2actionclient(node, ...
    "/arm_controller/follow_joint_trajectory", ...
    "control_msgs/FollowJointTrajectory");
```

Use the five joint names listed above when sending trajectories.

The MATLAB code must provide the target joint positions and the time for the movement.
