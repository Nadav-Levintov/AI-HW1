from . import GreedySolver
import numpy as np

class GreedyBestFirstSolver(GreedySolver):
    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar, scorer)
        self._scorer = scorer
        self.visited = set()

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        if currState.isGoal():
            return None
        self.visited.add(currState)
        successors = list(problem.expand(currState))
        unvisitedSuccessors = [s for s in successors if s not in self.visited]
        if len(unvisitedSuccessors) <= 0:
            return None
        bestState = unvisitedSuccessors[0]
        for state in unvisitedSuccessors:
            if self._scorer.compute(currState,state) < self._scorer.compute(currState,bestState):
                bestState = state

        return bestState

