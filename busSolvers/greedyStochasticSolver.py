from . import GreedySolver
import numpy as np
import sys


def _calc_sum(vector_x, t, vector_min):
    vector_sum = 0.0
    for x_i in vector_x:
        vector_sum += pow((x_i / vector_min), (-1 / t))
    return vector_sum


def _cal_prob(x_i, alpha, t, vector_sum):
    res = x_i / alpha
    res = pow(res, (-1 / t))
    res /= vector_sum
    return res

class GreedyStochasticSolver(GreedySolver):
    _TEMPERATURE_DECAY_FACTOR = None
    _INITIAL_TEMPERATURE = None
    _N = None

    def __init__(self, roads, astar, scorer, initialTemperature, temperatureDecayFactor, topNumToConsider):
        super().__init__(roads, astar, scorer)

        self._INITIAL_TEMPERATURE = initialTemperature
        self._TEMPERATURE_DECAY_FACTOR = temperatureDecayFactor
        self._N = topNumToConsider




    def _getSuccessorsProbabilities(self, currState, successors):
        # Get the scores
        X = np.array([self._scorer.compute(currState, target) for target in successors])

        # Initialize an all-zeros vector for the distribution
        P = np.zeros((len(successors),))

        # TODO: Fill the distribution in P as explained in the instructions.
        # find the N best indexes on X

        t = self.T
        bestNindexes = []

        for i in range(0,min([self._N,len(X)])):
            curr_best = sys.maxsize
            candidate = -1
            for idx,score in enumerate(X):
                if score < curr_best:
                    if idx not in bestNindexes:
                        candidate = idx
                        curr_best = score
            bestNindexes.append(candidate)


        bestNscores = [X[i] for i in bestNindexes]

        alpha =  X.min()
        vec_sum = _calc_sum(bestNscores,t ,alpha)
        #vec_prob = np.array([0.0 for x in X])
        for idx in bestNindexes:
            P[idx] = _cal_prob(X[idx],alpha,t,vec_sum)





        # Update the temperature
        self.T *= self._TEMPERATURE_DECAY_FACTOR

        return P

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        P = self._getSuccessorsProbabilities(currState, successors)


        # You should look for a suitable function in numpy.random.
        P = self._getSuccessorsProbabilities(currState,successors)

        nextIdx = np.random.choice(range(0,len(successors)),None,None,P)


        return successors[nextIdx]

    # Override the base solve method to initialize the temperature
    def solve(self, initialState):
        self.T = self._INITIAL_TEMPERATURE
        return super().solve(initialState)