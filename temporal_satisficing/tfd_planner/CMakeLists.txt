cmake_minimum_required(VERSION 2.8.3)
project(tfd_planner)
find_package(catkin REQUIRED COMPONENTS
    mk
)

add_custom_target(
  tfd_planner ALL
  COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR} make -f Makefile.tarball
  COMMAND cmake -E make_directory ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/tfd-src-0.4/downward/preprocess/preprocess ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}/
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/tfd-src-0.4/downward/search/search ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}/

  # patch tfd planner
  COMMAND cmake -E copy ${PROJECT_SOURCE_DIR}/patch/plan.py ${PROJECT_SOURCE_DIR}/build/tfd-src-0.4/downward/plan.py
)

catkin_package()
catkin_python_setup()
