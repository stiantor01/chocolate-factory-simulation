cmake_minimum_required(VERSION 3.8)
project(chocolate_conveyor)

find_package(ament_cmake REQUIRED)
find_package(gz-sim8 REQUIRED)

add_library(conveyor_system SHARED
  src/conveyor_system.cpp
)

target_link_libraries(conveyor_system
  gz-sim8::gz-sim8
)

install(TARGETS conveyor_system
  LIBRARY DESTINATION lib
)

ament_package()
