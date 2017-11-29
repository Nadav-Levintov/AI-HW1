from heuristics import Heuristic

# TODO : Implement as explained in the instructions
from ways import compute_distance


class TSPCustomHeuristic(Heuristic):
    _distMat = None
    _junctionToMatIdx = None
    roads = None

    # TODO : You can add parameters if you need them
    def __init__(self, roads, initialState):
        super().__init__()
        self.roads = roads

    # Estimate heuristically the minimal cost from the given state to the problem's goal
    def estimate(self, problem, state):
        max_val = 0
        for waiting_order in state.waitingOrders:
            coord1 = self.roads[waiting_order[0]].coordinates
            coord2 = self.roads[waiting_order[1]].coordinates
            current = compute_distance(coord1, coord2)
            if (max_val < current):
                max_val = current
        return max_val