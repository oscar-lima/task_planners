# tfd_planner

Temporal Fast Downward (TFD) is a temporal planning system developed by University of Freiburg.

See [tfd website](http://gki.informatik.uni-freiburg.de/tools/tfd/) for more details.

This package is a ROS wrapper that allows easy integration of the planner with [ROSPlan](https://github.com/KCL-Planning/ROSPlan) framework.

## Installation

Make sure you have an active internet connection, then build the ROS pkg.

        catkin build tfd_planner

See below for an explanation of the steps it performs.

## Explanation

This pkg performs the following steps automatically for you, when you trigger building:

1. Download [tfd planner](http://gki.informatik.uni-freiburg.de/tools/tfd/)

2. Unzip and build tfd planner using special flags (only for "search" binary).

        make release CCOPT=-Wno-error # to avoid treating warnings as errors

This step is a workaround for the pkg not building under ubuntu 18.04, using plain make release command.

3. Patch. This pkg ships with a "patch" folder. Inside it contains a modified version of plan.py that replaces

the old plan.py provided by the authors, this is needed to resolve global paths programatically using ROS bash,

as the planner will be called programatically using ROSPlan.

## Test

This pkg ships with an example launch file to demo the use of this planner in [ROSPlan](https://github.com/KCL-Planning/ROSPlan).

First make sure you have [ROSPlan](https://github.com/KCL-Planning/ROSPlan) installed on your system.

This demo requires four terminals. The order in which you execute the commands is important.

    # launch example
    roslaunch tfd_planner tfd_planner_example.launch

    # listen to planner output
    rostopic echo /rosplan_planner_interface/planner_output

    # generate a pddl problem
    rosservice call /rosplan_problem_interface/problem_generation_server "{}"

    # make plan
    rosservice call /rosplan_planner_interface/planning_server "{}"
