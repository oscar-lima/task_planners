cmake_minimum_required(VERSION 2.8.3)
project(popf_planner)
find_package(catkin REQUIRED COMPONENTS
    mk
)

add_custom_target(
  popf_planner ALL
  COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR} make -f Makefile.tarball
  COMMAND cmake -E make_directory ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/popf-1.1/build/popf/popf-clp ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}/popf
)

catkin_package()
