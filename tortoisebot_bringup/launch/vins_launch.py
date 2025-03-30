import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to the YAML configuration file
    config_file = os.path.join(
        get_package_share_directory('tortoisebot_description'),  # Adjust if needed
        'camera_config',
        'raspicam',
        'raspicam_mono_imu.yaml'
    )

    # Nodes to launch
    vins_node = Node(
        package='vins',
        executable='vins_node',
        output='screen',
        parameters=[{'config_file': config_file}]
    )

    loop_fusion_node = Node(
        package='loop_fusion',
        executable='loop_fusion_node',
        output='screen',
        parameters=[{'config_file': config_file}]
    )

    return LaunchDescription([vins_node, loop_fusion_node])
