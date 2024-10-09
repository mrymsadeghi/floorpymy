# Evaluator
## Basic Evaluator
DoorOffEdgeEvaluator: Checks if any door is placed too close to the edge of a room (outside valid boundaries).
MinimumWidthEvaluator: Ensures that rooms meet a minimum width and height threshold.
AdjacentHallwayFilter: Ensures narrow rooms do not spawn next to other narrow rooms, based on area-to-perimeter ratio and shared edge length.
LongDeadEndFilter: Detects narrow rooms that have only one or no doors, marking them as dead ends.
LowMeanAreaPerimeterRatio: Verifies that the median area-to-perimeter ratio for all rooms in the floorplan is above a specified threshold.
HighTravelCostBetweenRoomsFilter: Measures travel cost between rooms using an adjacency matrix and ensures the longest path is below a certain limit.

## Door Judge
The code defines a DoorJudge class that evaluates door placements in a floorplan based on two main criteria:
score_connectivity: This method calculates how well the rooms in a floorplan are connected based on door placements. It uses connectivity islands to determine the largest set of connected rooms, and checks for the existence of an outside door. The connectivity score is higher when more rooms are connected and there is at least one external door.
score_individual_doors: This method scores each room's door placement based on a specific scoring function for each room type, which is squared to emphasize larger differences. The overall door score is averaged across all rooms.
outside_door_exists: Checks if there is at least one external door in the floorplan.
get_connectivity_islands: Identifies and returns groups of connected rooms (islands) based on shared doors.
create_perfect_doorplan: Attempts to generate the best door configuration by repeatedly randomizing door placements, scoring the layout based on door and connectivity scores, and retaining the best configuration. The result is a "perfect" doorplan according to the evaluation criteria.

