%% ROS 2 connection
setenv('ROS_DOMAIN_ID', '15');

node = ros2node("/matlab_controller");

%% Connect to the robot controller
client = ros2actionclient(node, ...
    "/arm_controller/follow_joint_trajectory", ...
    "control_msgs/FollowJointTrajectory");

% Wait for the action server
waitForServer(client);

%% Create trajectory goal
goal = ros2message(client);

goal.trajectory.joint_names = { ...
    'joint_1', ...
    'joint_2', ...
    'joint_3', ...
    'joint_4', ...
    'joint_5'};

% Target joint angles (radians)
point = ros2message("trajectory_msgs/JointTrajectoryPoint");

point.positions = [-0.4, 0.2, -1.0, -1.0, 0.0];

% Leave unused fields empty
point.velocities = [];
point.accelerations = [];
point.effort = [];

% Movement duration: 3 seconds
point.time_from_start.sec = int32(3);
point.time_from_start.nanosec = uint32(0);

goal.trajectory.points = point;

%% Send trajectory
goalHandle = sendGoal(client, goal);

disp("Trajectory sent to robot");
