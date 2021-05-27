import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1',index_col=0)

plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
df1['A'].hist()

plt.savefig("./graphs/StyleSheet.png")
