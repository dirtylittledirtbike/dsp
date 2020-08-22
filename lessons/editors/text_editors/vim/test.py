import matplotlib.pyplot as plt
import numpy as np

y = np.random.exponential(scale=1.0, size=2000)
plt.hist(y, bins=30)
plt.show()
