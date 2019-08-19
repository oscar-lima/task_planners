# popf_planner

POPF is forward-chaining temporal planner developed by KCL University in London.

See [popf website](https://nms.kcl.ac.uk/planning/software/popf.html) for more details.

This package is a ROS wrapper that allows easy integration of the planner with [ROSPlan](https://github.com/KCL-Planning/ROSPlan) framework.

## Difference between popf_planner and popf_planner

popf_planner -> downloads popf-1.1.tar.gz from [sourceforge](https://sourceforge.net/projects/tsgp/files/POPF/popf-1.1.tar.gz/download)

popf_planner -> downloads popf2-11jun2011.tar.bz2 from [sourceforge](https://sourceforge.net/projects/tsgp/files/POPF/popf-1.1.tar.gz/download)

## Installation

Make sure you have an active internet connection, then build the ROS pkg.

        catkin build popf_planner

See below for an explanation of the steps it performs.

## Explanation

This pkg performs the following steps automatically for you, when you trigger building:

1. Download [popf_planner](https://sourceforge.net/projects/tsgp/files/POPF/popf-1.1.tar.gz/download)

2. Unzip, build popf planner

        cd build/build/popf-1.1/build && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ../src && cd popf && make

3. Patch (is performed before building). This pkg ships with a "patch" folder. Inside it contains files that solve compilation errors and warnings in the popf code.

Most of the changes are small, like for example the addition of a header that for some reason is needed in newer gcc versions but was not in the past.

This patch files get automatically copied in the right location for you when you build the ros pkg with the usual catkin build commands.

## Test

This pkg ships with an example launch file to demo the use of this planner in [ROSPlan](https://github.com/KCL-Planning/ROSPlan).

First make sure you have [ROSPlan](https://github.com/KCL-Planning/ROSPlan) installed on your system.

This demo requires four terminals. The order in which you execute the commands is important.

    # launch example
    roslaunch popf_planner popf_planner_example.launch

    # listen to planner output
    rostopic echo /rosplan_planner_interface/planner_output

    # generate a pddl problem
    rosservice call /rosplan_problem_interface/problem_generation_server "{}"

    # make plan
    rosservice call /rosplan_planner_interface/planning_server "{}"
