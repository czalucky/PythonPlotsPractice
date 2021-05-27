import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./walmart_stock.csv',index_col='Date',parse_dates=True)

df['Open'].plot(figsize=(16,6))

df['Open'].plot()
df.rolling(window=30).mean()['Close'].plot()

#Legend
df['Close: 30 Day Mean'] = df['Close'].rolling(window=20).mean()
df['Upper'] = df['Close: 30 Day Mean'] + 2*df['Close'].rolling(window=20).std()
df['Lower'] = df['Close: 30 Day Mean'] - 2*df['Close'].rolling(window=20).std()
df[['Close','Close: 30 Day Mean','Upper','Lower']].plot(figsize=(16,6))

plt.savefig("./graphs/Rolling.png")
