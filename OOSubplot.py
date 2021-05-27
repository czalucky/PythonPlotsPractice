import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,3))

for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Subplot')


plt.tight_layout()
plt.savefig("./graphs/OOSubplot.png")
