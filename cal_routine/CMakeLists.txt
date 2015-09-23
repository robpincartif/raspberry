cmake_minimum_required(VERSION 2.8.3)
project(cal_routine)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs std_srvs actionlib actionlib_msgs )



## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################
add_message_files(
  DIRECTORY msg
)

## Generate services in the 'srv' folder
 add_service_files(
   DIRECTORY srv
 )


## Generate actions in the 'action' folder
add_action_files(
   DIRECTORY action
)

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs actionlib_msgs 
 )


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES strands_tweets
#  CATKIN_DEPENDS other_catkin_pkg
  DEPENDS actionlib_msgs
)


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination

install(DIRECTORY scripts/
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        USE_SOURCE_PERMISSIONS)


# Mark other files for installation (e.g. launch and bag files, etc.)
install(
  DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
