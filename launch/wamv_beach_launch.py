from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_anchor_gazebo = get_package_share_directory('shoreline_sim')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py']),
            ),
            launch_arguments={'gz_args': [
                PathJoinSubstitution(
                    [pkg_anchor_gazebo, 'worlds', 'beach_world.sdf']),
            ],
                'on_exit_shutdown': 'True'}.items(),
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/imu_wamv_link/sensor/imu_wamv_sensor/imu@sensor_msgs/msg/Imu@gz.msgs.IMU',
                       '/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/gps_wamv_link/sensor/navsat/navsat@sensor_msgs/msg/NavSatFix@gz.msgs.NavSat',
                       '/model/wamv/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
                       '/model/wamv/joint/left_engine_propeller_joint/cmd_thrust@std_msgs/msg/Float64@gz.msgs.Double',
                       '/model/wamv/joint/right_engine_propeller_joint/cmd_thrust@std_msgs/msg/Float64@gz.msgs.Double',
                       '/model/wamv/pose@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V',
                       '/debug/wind/speed@std_msgs/msg/Float32@gz.msgs.Float',
                       '/debug/wind/direction@std_msgs/msg/Float32@gz.msgs.Float',
                       '/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/front_camera_sensor/image@sensor_msgs/msg/Image@gz.msgs.Image',
                       '/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/front_camera_sensor/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo',
                       '/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/lidar_wamv_sensor/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
                       '/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/lidar_wamv_sensor/scan/points@sensor_msgs/msg/PointCloud2@gz.msgs.PointCloudPacked',
                       ],
            remappings=[
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/imu_wamv_link/sensor/imu_wamv_sensor/imu',
                 '/wamv/sensors/imu/imu/data'),
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/gps_wamv_link/sensor/navsat/navsat',
                 '/wamv/sensors/gps/gps/fix'),
                ('/model/wamv/joint/left_engine_propeller_joint/cmd_thrust',
                 '/wamv/thrusters/left/thrust'),
                ('/model/wamv/joint/right_engine_propeller_joint/cmd_thrust',
                 '/wamv/thrusters/right/thrust'),
                ('/model/wamv/odometry', '/wamv/ground_truth/odometry'),
                ('/model/wamv/model/wamv/model/pose',
                 '/wamv/ground_truth/pose'),
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/front_camera_sensor/image',
                 '/wamv/sensors/camera/front/image'),
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/front_camera_sensor/camera_info',
                 '/wamv/sensors/camera/front/camera_info'),
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/lidar_wamv_sensor/scan',
                 '/wamv/sensors/front_lidar/scan'),
                ('/world/beach_world/model/wamv/model/wamv/model/wamv/link/wamv/base_link/sensor/lidar_wamv_sensor/scan/points',
                 '/wamv/sensors/front_lidar/points'),
            ],
            output='screen'
        ),
    ])
