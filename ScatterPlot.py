import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1',index_col=0)

df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')
plt.savefig("./graphs/ScatterPlot.png")

