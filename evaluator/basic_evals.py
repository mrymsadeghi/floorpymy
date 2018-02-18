class DoorOffEdgeEvaluator(object):

    def evaluate(self, floorplan):
        edgeset = set()
        for room in floorplan.rooms:
            for edge in room.edges:
                edgeset.add(edge)

        for edge in edgeset:
            for door in edge.doors:
                a, b = edge.radial_t_values(door.t, door.width / 2)
                for t in [a, b]:
                    if t <= 0 or t >= 1:
                        print("\tFailed on t = ", t)
                        return 0
        return 1


class MinimumWidthEvaluator(object):

    def __init__(self, threshold):
        self.threshold = threshold

    def evaluate(self, floorplan):
        for room in floorplan.rooms:
            x_max, x_min, y_max, y_min = room.max_min_xy
            width = x_max - x_min
            height = y_max - y_min

            if width < self.threshold or height < self.threshold:
                print("\tFailed minimum width")
                return 0

        return 1


class AdjacentHallwayFilter(object):
    # Make sure that very narrow rooms do not spawn next to each other.

    def __init__(self, ap_ratio_threshold=4.25):
        self.ap_ratio_threshold = ap_ratio_threshold

    def evaluate(self, floorplan):
        
        for room in floorplan.rooms:
            ap_ratio = room.area / room.perimeter
            if ap_ratio < self.ap_ratio_threshold:
                # Then check neighbors to see if any of them have high ap_ratios
                for neighbor, edge in room.neighbors_and_edges:
                    neighbor_ap_ratio = neighbor.area / neighbor.perimeter
                    if neighbor_ap_ratio < self.ap_ratio_threshold:
                        # Does the edge shared between the two represent a longer edge?
                        if (neighbor.perimeter / edge.length) > len(neighbor.edges):
                            print("\tFailed on duplicate neighbors")
                            return 0
        return 1


import itertools
class LongDeadEndFilter(object):

    def __init__(self, ap_ratio_threshold=5.0):
        self.ap_ratio_threshold = ap_ratio_threshold

    def evaluate(self, floorplan):
        for room in floorplan.rooms:
            ap_ratio = room.area / room.perimeter
            if ap_ratio < self.ap_ratio_threshold:
                doors = list(itertools.chain(*[edge.doors for edge in room.edges]))
                if len(doors) <= 1:
                    print("\tFailed on narrow room to nowhere.")
                    return 0

        return 1

# import statistics
# class LowMeanAreaPerimeterRatio(object):

#     def __init__(self, ap_ratio_threshold=6.67):
#         self.ap_ratio_threshold = ap_ratio_threshold

#     def evaluate(self, floorplan):
#         median_ap = statistics.median([room.area / room.perimeter for room in floorplan.rooms])
        
#         if median_ap < self.ap_ratio_threshold:
#             print(f"Failed on Median AP is too low {median_ap}")
#             return 0
#         else:
#             return 1
            

        
        


