# task_planners

AI model based task planners for decision making in [ROSPlan](https://github.com/KCL-Planning/ROSPlan)

ROS wrappers for AI task planning open source planners.

The design is based on the [mk](http://wiki.ros.org/mk) ros pkg, to import 3rdparty code.

It performs 3 steps: download a planner source code from the original author website, patches the code by replacing

some files from custom ones, build the code and offers launch files and sample pddl files for manual testing purposes.

User is advised to check sub-pkgs README files for specifics.

Supported planners are:

- [popf](https://nms.kcl.ac.uk/planning/software/popf.html) v1, v2 from KCL University.
- [tfd](http://gki.informatik.uni-freiburg.de/tools/tfd) from Freiburg University.
- [mercury_planner]
