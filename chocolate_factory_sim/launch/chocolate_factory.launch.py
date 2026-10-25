import os
from pathlib import Path

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    sim_path = get_package_share_directory('chocolate_factory_sim')
    robot_path = get_package_share_directory('chocolate_robot_description')
    gz_path = get_package_share_directory('ros_gz_sim')

    world = os.path.join(sim_path, 'worlds', 'chocolate_factory.sdf')
    robot = os.path.join(robot_path, 'urdf', 'chocolate_robot_gazebo.urdf')

    # Finn controller-konfigurasjonen uavhengig av brukernavn
    controller_config = os.path.join(
        sim_path, 'config', 'controller_config.yaml'
    )

    # Lag en URDF med riktig filbane for denne maskinen
    robot_description = Path(robot).read_text()
    robot_description = robot_description.replace(
        '__CONTROLLER_CONFIG_PATH__',
        controller_config
    )

    # Lagre en midlertidig URDF som Gazebo kan laste
    import tempfile
    generated_robot = os.path.join(
        tempfile.gettempdir(), 'chocolate_robot_generated.urdf'
    )
    Path(generated_robot).write_text(robot_description)

    resource_paths = os.pathsep.join([
        os.path.join(sim_path, 'models'),
        os.path.dirname(robot_path),
        os.environ.get('GZ_SIM_RESOURCE_PATH', '')
    ])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gz_path, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-r ' + world}.items()
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }],
        output='screen'
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'chocolate_factory',
            '-name', 'chocolate_robot',
            '-file', generated_robot,
            '-x', '0',
            '-y', '0',
            '-z', '0.8347'
        ],
        output='screen'
    )

    joint_state_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager', '/controller_manager'
        ],
        output='screen'
    )

    arm_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'arm_controller',
            '--controller-manager', '/controller_manager'
        ],
        output='screen'
    )

    return LaunchDescription([
        SetEnvironmentVariable(
            name='GZ_SIM_RESOURCE_PATH',
            value=resource_paths
        ),
        gazebo,
        robot_state_publisher,
        TimerAction(
            period=5.0,
            actions=[spawn_robot]
        ),
        TimerAction(
            period=8.0,
            actions=[joint_state_spawner, arm_spawner]
        )
    ])
