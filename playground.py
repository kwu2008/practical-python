
from matplotlib import pyplot as plt
import numpy as np
import math

x = np.arange(0, math.pi * 2, 0.05)
y = np.sin(x)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, y)

ax.set_title("Sine Wave")
ax.set_xlabel("Angle")
ax.set_ylabel("Sine")

fig.show()
