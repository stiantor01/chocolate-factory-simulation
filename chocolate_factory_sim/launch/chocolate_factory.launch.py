import os

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
    robot = os.path.join(robot_path, 'urdf', 'chocolate_robot.urdf')

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

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'chocolate_factory',
            '-name', 'chocolate_robot',
            '-file', robot,
            '-x', '0',
            '-y', '0',
            '-z', '0.8347'
        ],
        output='screen'
    )

    return LaunchDescription([
        SetEnvironmentVariable(
            name='GZ_SIM_RESOURCE_PATH',
            value=resource_paths
        ),
        gazebo,
        TimerAction(
            period=5.0,
            actions=[spawn_robot]
        )
    ])
