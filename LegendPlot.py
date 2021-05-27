import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)

fig = plt.figure()

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_xlabel("x")
ax.set_ylabel("y");
ax.plot(x, x**2, 'b.-', label="x**2")
ax.plot(x, x**3, 'r--', label="x**3")
ax.legend(loc=4)

plt.savefig("./graphs/LegendPlot.png")
