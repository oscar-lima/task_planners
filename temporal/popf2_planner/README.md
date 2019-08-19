# popf2_planner

POPF is forward-chaining temporal planner developed by KCL University in London.

See [popf website](https://nms.kcl.ac.uk/planning/software/popf.html) for more details.

This package is a ROS wrapper that allows easy integration of the planner with [ROSPlan](https://github.com/KCL-Planning/ROSPlan) framework.

## Difference between popf_planner and popf2_planner

popf_planner -> downloads popf-1.1.tar.gz from [sourceforge](https://sourceforge.net/projects/tsgp/files/POPF)

popf2_planner -> downloads popf2-11jun2011.tar.bz2 from [sourceforge](https://sourceforge.net/projects/tsgp/files/POPF)

## Installation

Make sure you have an active internet connection, then build the ROS pkg.

        catkin build popf2_planner

See below for an explanation of the steps it performs.

## Explanation

This pkg performs the following steps automatically for you, when you trigger building:

1. Download [popf2 planner](https://datapacket.dl.sourceforge.net/project/tsgp/POPF/popf2-11jun2011.tar.bz2)

2. Unzip and build popf2 planner

        cd build/tempo-sat-popf2/compile && cmake ../src -DCMAKE_BUILD_TYPE=Release -DCMAKE_VERBOSE_MAKEFILE=TRUE && $(MAKE) popf3-clp -Wno-dev

3. Patch. This pkg ships with a "patch" folder. Inside it contains files that solve compilation errors and warnings in the popf2 code.

Most of the changes are small, like for example the addition of a header that for some reason is needed in newer gcc versions but was not in the past.

This patch files get automatically copied in the right location for you when you build the ros pkg with the usual catkin build commands.

## Test

This pkg ships with an example launch file to demo the use of this planner in [ROSPlan](https://github.com/KCL-Planning/ROSPlan).

First make sure you have [ROSPlan](https://github.com/KCL-Planning/ROSPlan) installed on your system.

This demo requires four terminals. The order in which you execute the commands is important.

    # launch example
    roslaunch popf2_planner popf2_planner_example.launch

    # listen to planner output
    rostopic echo /rosplan_planner_interface/planner_output

    # generate a pddl problem
    rosservice call /rosplan_problem_interface/problem_generation_server "{}"

    # make plan
    rosservice call /rosplan_planner_interface/planning_server "{}"
