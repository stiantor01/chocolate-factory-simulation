cmake_minimum_required(VERSION 3.8)
project(chocolate_tracking)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(chocolate_interfaces REQUIRED)
find_package(gz-transport13 REQUIRED)
find_package(gz-msgs10 REQUIRED)

add_executable(chocolate_tracking_node
  src/chocolate_tracking.cpp
)

ament_target_dependencies(chocolate_tracking_node
  rclcpp
  chocolate_interfaces
)

target_link_libraries(chocolate_tracking_node
  gz-transport13::gz-transport13
  gz-msgs10::gz-msgs10
)

install(TARGETS chocolate_tracking_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
