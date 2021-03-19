import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta#, bernoulli
# Set your value for n and s here!
n, s = 1000, 2
def plot_inverse_power_partial_sums(n, s):
    fig = plt.figure()
    ax = fig.gca()
    # Create an array of integers and compute the corresponding summands and partial sums
    x = np.arange(1., n+1)
    summands = np.reciprocal(np.power(x, s))
    partial_sums = np.cumsum(summands)
    # Plot the partial sums and the reference line
    ax.hlines(zeta(s), x[0], x[-1], linestyles='dashed')
    ax.plot(x, partial_sums)
    plt.show()
plot_inverse_power_partial_sums(n, s)
