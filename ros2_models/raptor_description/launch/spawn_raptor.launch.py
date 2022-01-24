from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    raptor_description_dir = get_package_share_directory('raptor_description')
    print(raptor_description_dir)
    return LaunchDescription([
        launch_ros.actions.Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=['-spawn_service_timeout', '60', '-entity', 'raptor_model', '-x', '0', '-y', '0', '-z', '0', '-file', raptor_description_dir + '/gazebo_model/raptor_model/model.sdf']),
            
        launch_ros.actions.Node(
            package='gzweb_model',
            executable='gzweb_model.bash',
            name='foo',
            arguments=[raptor_description_dir+'/gazebo_model/raptor_model'],
            ),    
    ])      
