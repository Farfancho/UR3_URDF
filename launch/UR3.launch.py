import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = "ur3_description"

    robot_desc_path = os.path.join(
        get_package_share_directory(package_name),
        "UR3",
        "robot.urdf"
    )

    with open(robot_desc_path, "r") as f:
        robot_description = f.read()

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[{
            "use_sim_time": False,
            "robot_description": robot_description
        }]
    )

    return LaunchDescription([
        robot_state_publisher_node,
    ])