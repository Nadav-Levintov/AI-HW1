import numpy as np
import sys

class AStar:
    cost = None
    heuristic = None
    _cache = None
    shouldCache = None

    def __init__(self, heuristic, cost=None, shouldCache=False):
        self.heuristic = heuristic
        self.shouldCache = shouldCache
        self.cost = cost

        # Handles the cache. No reason to change this code.
        if self.shouldCache:
            self._cache = {}

    # Get's from the cache. No reason to change this code.
    def _getFromCache(self, problem):
        if self.shouldCache:
            return self._cache.get(problem)

        return None

    # Get's from the cache. No reason to change this code.
    def _storeInCache(self, problem, value):
        if not self.shouldCache:
            return

        self._cache[problem] = value

    # Run A*
    def run(self, problem):
        # Check if we already have this problem in the cache.
        # No reason to change this code.
        source = problem.initialState
        if self.shouldCache:
            res = self._getFromCache(problem)

            if res is not None:
                return res

        # Initializes the required sets
        closed_set = set()  # The set of nodes already evaluated.
        parents = {}  # The map of navigated nodes.

        # Save the g_score and f_score for the open nodes
        g_score = {source: 0}
        open_set = {source: self.heuristic.estimate(problem, problem.initialState)}

        developed = 0
        hi = open_set[source]
        while open_set != {}:
            next = self._getOpenStateWithLowest_f_score(open_set)
            del open_set[next]
            closed_set.add(next)
            if(problem.isGoal(next)):
                self._storeInCache(problem, (self._reconstructPath(parents, next), g_score[next], hi, developed))
                return (self._reconstructPath(parents, next), g_score[next], hi, developed)
            developed += 1
            for succ, curr_cost in problem.expandWithCosts(next,self.cost):
                new_g = g_score[next] + curr_cost
                if succ in open_set:
                    if new_g < g_score[succ]:
                        g_score[succ] = new_g
                        parents[succ] = next
                        open_set[succ] = g_score[succ] + self.heuristic.estimate(problem, succ)
                else:
                    if succ in closed_set:
                        if new_g < g_score[succ]:
                            g_score[succ] = new_g
                            parents[succ] = next
                            closed_set.remove(succ)
                            open_set[succ] = g_score[succ] + self.heuristic.estimate(problem, succ)
                    else:
                        open_set[succ] = new_g + self.heuristic.estimate(problem, succ)
                        g_score[succ] = new_g
                        parents[succ] = next

    def _getOpenStateWithLowest_f_score(self, open_set):
        min = sys.maxsize
        res = None
        for key, value in open_set.items():
            if value < min:
                min = value
                res = key
        return res

    # Reconstruct the path from a given goal by its parent and so on
    def _reconstructPath(self, parents, goal):
        res = []
        ptr = goal
        res.insert(0, ptr)
        while ptr in parents.keys():
            ptr = parents[ptr]
            res.insert(0, ptr)
        return res

