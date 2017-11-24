from ways import compute_distance
from . import Heuristic

# Use the L2 aerial distance (in meters)
class L2DistanceHeuristic(Heuristic):
    def estimate(self, problem, state):
        return compute_distance(problem.target.coordinates, state.coordinates)
