import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y, 'g') # g for green
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.savefig("./graphs/BasicPlot.png")

plt.show()