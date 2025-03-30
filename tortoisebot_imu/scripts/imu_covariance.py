#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import numpy as np

class ImuCovarianceNode(Node):
    def __init__(self):
        super().__init__('imu_covariance_node')
        # Publisher on /imu/data topic
        self.publisher = self.create_publisher(Imu, '/imu_propagate', 10)
        # Subscriber to /imu_plugin/out topic
        self.subscription = self.create_subscription(
            Imu,
            '/imu_plugin/out',
            self.imu_callback,
            10)
        self.subscription  # prevent unused variable warning

    def imu_callback(self, msg: Imu):
        # Create a new message or modify the received one
        new_msg = Imu()
        # new_msg.header = msg.header
        # new_msg.orientation = msg.orientation
        # new_msg.angular_velocity = msg.angular_velocity
        # new_msg.linear_acceleration = msg.linear_acceleration

        # # Define identity covariance (3x3 identity matrix flattened to 9 elements)
        # identity_cov = np.random.rand(9).tolist()

        # # print(len(msg.orientation_covariance), len(msg.angular_velocity_covariance), len(msg.linear_acceleration_covariance))
        # # Set the covariance for orientation, angular velocity, and linear acceleration
        # new_msg.orientation_covariance = identity_cov.copy()
        # new_msg.angular_velocity_covariance = identity_cov.copy()
        # new_msg.linear_acceleration_covariance = identity_cov.copy()
        new_msg = msg
        # Publish the new message
        self.publisher_.publish(new_msg)
        # self.get_logger().info('Published IMU data with identity covariance')

def main(args=None):
    rclpy.init(args=args)
    node = ImuCovarianceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    # Shutdown
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
