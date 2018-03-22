import numpy as np
import matplotlib.pyplot as plt

greyhounds = 5000
labs = 5000

grey_height = 28 + 4 * np.random.rand(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
plt.show()
