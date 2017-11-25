from consts import Consts
from astar import AStar
from ways import load_map_from_csv
from busSolvers import GreedyBestFirstSolver, GreedyStochasticSolver
from problems import BusProblem
from costs import L2DistanceCost
from heuristics import L2DistanceHeuristic
import numpy as np

REPEATS = 150

# Load the files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("HAIFA_100.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

scorer = L2DistanceCost(roads)

# Run the greedy solver
pickingPath = GreedyBestFirstSolver(roads, mapAstar, scorer).solve(prob)
greedyDistance = pickingPath.getDistance() / 1000
print("Greedy solution: {:.2f}km".format(greedyDistance))

# Run the stochastic solver #REPATS times
solver = GreedyStochasticSolver(roads, mapAstar, scorer,
                                Consts.STOCH_INITIAL_TEMPERATURE,
                                Consts.STOCH_TEMPERATURE_DECAY_FUNCTION,
                                Consts.STOCH_TOP_SCORES_TO_CONSIDER)
results = np.zeros((REPEATS,))
print("Stochastic repeats:")
for i in range(REPEATS):
    print("{}..".format(i+1), end=" ", flush=True)
    results[i] = solver.solve(prob).getDistance() / 1000

print("\nDone!")

mono = results
mono[0] = min([mono[0],greedyDistance])
for i in range(1,REPEATS):
    mono[i]=min([mono[i],mono[i-1]])



from matplotlib import pyplot as plt

plt.plot(range(1,REPEATS+1),mono)
plt.plot(range(1,REPEATS+1),[greedyDistance for x in mono])
plt.legend(['stochastic','greedy best first'])
plt.axis([0, REPEATS, 0.9*mono.min(), 1.1*mono.max()])
#plt.legend([[greedyDistance for x in mono],mono],['greedy best first','stochastic'])
plt.title('Length of solution by Number of Repeats')
plt.xlabel('#Repeats')
plt.ylabel('Solution Length')
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.show()



# TODO : Part2 - Remove the exit and perform the t-test
raise NotImplementedError