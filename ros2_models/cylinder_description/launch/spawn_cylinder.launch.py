from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    cylinder_description_dir = get_package_share_directory('cylinder_description')
    return LaunchDescription([
        launch_ros.actions.Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=['-spawn_service_timeout', '60', '-entity', 'cylinder_model', '-x', '0', '-y', '0', '-z', '0', '-file', cylinder_description_dir + '/gazebo_model/cylinder_model/model.sdf']),
    ])        
