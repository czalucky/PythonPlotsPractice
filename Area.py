import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv('df2')

df2.plot.area(alpha=0.4)
plt.savefig("./graphs/Area.png")

