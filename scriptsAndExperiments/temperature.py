import numpy as np
from matplotlib import pyplot as plt

X = np.array([400, 900, 390, 1000, 550])


def _calc_sum(vector_x, t, vector_min):
    vector_sum = 0.0
    for x_i in vector_x:
        vector_sum = vector_sum + pow((x_i / vector_min), (-1 / t))
    return vector_sum


def _cal_prob(x_i, alpha, t, vector_sum):
    res = x_i / alpha
    res = pow(res, (-1 / t))
    res /= vector_sum
    return res


range = np.linspace(0.01, 5, 100)
alpha = X.min()
for pnt in X:
    pnt_vector = []
    for t in range:
        vector_sum = _calc_sum(X, t, alpha)
        pnt_vector.append(_cal_prob(pnt, alpha, t, vector_sum))
    plt.plot(range, pnt_vector)

plt.axis([0, 5, 0, 1])
plt.legend(X)
plt.title('Probability as a function of the temperature')
plt.xlabel('T')
plt.ylabel('p')
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.show()
