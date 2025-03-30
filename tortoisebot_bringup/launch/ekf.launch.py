from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

ekf_config_path = os.path.join(get_package_share_directory('tortoisebot_bringup'), 'config', 'ekf.yaml')
def generate_launch_description():
    return LaunchDescription([
        Node(
            package="robot_localization",
            executable="ekf_node",
            name="ekf_localization",
            output="screen",
            parameters=[ekf_config_path],
        )
    ])
