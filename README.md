# intersection_traffic_flow

## Main Project Idea:
Reduce wait times of vehicles at an intersection. 

## Thought Process:
Vehicles can pass through an intersection efficiently when there is no other vehicle path intersecting their path -> Construct a conflict graph as follows:

Vertices v_i : All possible paths vehicles may take through an intersection.
Edges v_i-v_j : All possible path collisions between vehicle path v_i and vehicle path v_j. 

The most vehicles can pass through this intersection when as many vertices of this conflict graph can be 'active' without their neighbours also being 'active' - this is the maximum independent set of this graph. Can we take the maximum independent set of the original graph, allow these vehicles to pass through the intersection, remove this set from the graph and repeat this process until there are no vertices remaining? I.e. would this increase the number of vehicles passing through an intersection resulting in a reduction of wait times at this intersection?
