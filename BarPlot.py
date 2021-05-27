import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv('df2')

df2.plot.bar(stacked=True)

plt.savefig("./graphs/Barplot.png")

