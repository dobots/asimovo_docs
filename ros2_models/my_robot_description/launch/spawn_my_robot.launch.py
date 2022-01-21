from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions

import xacro
import os

def generate_launch_description():
     # Urdf using xacro command substitution
    xacro_path = os.path.join(get_package_share_directory('my_robot_description'), 'urdf/', 'my_robot.xacro')
    assert os.path.exists(xacro_path), "The requested .xacro file doesnt exist in "+str(xacro_path)  
    print("xacro_path", xacro_path)
       
    doc = xacro.process_file(xacro_path)
    robot_desc = doc.toprettyxml(indent='  ')
    print(robot_desc)
    
    model_description_dir = get_package_share_directory('my_robot_description')

    return LaunchDescription([
        #Run the spawn script
        launch_ros.actions.Node(
            package='my_robot_description',
            executable='spawn_my_robot.py',
            arguments=[robot_desc],
            output='screen'),
            
        launch_ros.actions.Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[
                {"robot_description": robot_desc}],
            output="screen"),
       
       #Ensure gzweb can find the model description     
       launch_ros.actions.Node(
            package='gzweb_model',
            executable='gzweb_model.bash',
            name='foo',
            parameters=[model_description_dir],
            ),         
      
              
    ])        
