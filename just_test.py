import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 1000)
y = np.sin(x ** 2 + 5)

plt.plot(x, y)
plt.show()