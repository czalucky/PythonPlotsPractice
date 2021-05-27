import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1',index_col=0)

df1['A'].plot.hist(bins=50)
plt.savefig("./graphs/Histogram.png")

