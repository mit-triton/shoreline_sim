from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory, get_package_prefix, PackageNotFoundError

def generate_launch_description():
    pkg_anchor_gazebo = get_package_share_directory('shoreline_sim')

    try:
        get_package_prefix('wamv_controller')
    except PackageNotFoundError:
        print("The 'wamv_controller' package was not found. Exiting.")
        exit(1)

    try:
        get_package_prefix('protobuf_client')
    except PackageNotFoundError:
        print("The 'protobuf_client' package was not found. Exiting.")
        exit(1)

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [pkg_anchor_gazebo, 'launch', 'wamv_beach_launch.py']),
            ),
        ),
        Node(
            package='wamv_controller',
            executable='thruster_controller',
            name='thruster_controller',
            output='screen'
        ),
        Node(
            package='wamv_controller',
            executable='nav_state_reporter',
            name='nav_state_reporter',
            output='screen'
        ),
        Node(
            package='protobuf_client',
            executable='protobuf_client_node',
            name='protobuf_client_node',
            output='screen'
        ),
        Node(
            package='wamv_controller',
            executable='waypoint_publisher',
            name='waypoint_publisher',
            output='screen'
        )
    ])
