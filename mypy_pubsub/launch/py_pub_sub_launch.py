from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypy_pubsub',
           
            executable='talker',
       
        ),
        Node(
            package='mypy_pubsub',
           
            executable='listener',
           
        ),
    ])
