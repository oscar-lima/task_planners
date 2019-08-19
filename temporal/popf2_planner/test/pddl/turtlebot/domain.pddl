(define (domain turtlebot_demo)

(:requirements :strips :typing :fluents :disjunctive-preconditions :durative-actions)

(:types
	waypoint 
	robot
)

(:predicates
	(robot_at ?r - robot ?wp - waypoint)
	(connected ?from ?to - waypoint)
	(visited ?wp - waypoint)
)

(:functions
	(distance ?wp1 ?wp2 - waypoint) 
)

;; Move between any two waypoints, avoiding terrain
(:durative-action goto_waypoint
	:parameters (?r - robot ?from ?to - waypoint)
	:duration ( = ?duration 10)
	:condition (and
		(at start (robot_at ?r ?from)))
	:effect (and
		(at end (visited ?to))
		(at start (not (robot_at ?r ?from)))
		(at end (robot_at ?r ?to)))
)
)

