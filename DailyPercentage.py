import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2021, 1, 1)
tesla = web.DataReader("TSLA", 'yahoo', start, end)
ford = web.DataReader("F", 'yahoo', start, end)
gm = web.DataReader("GM", 'yahoo', start, end)

tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

tesla['returns'].hist(bins=100,label='Tesla',figsize=(10,8),alpha=0.5)
gm['returns'].hist(bins=100,label='GM',alpha=0.5)
ford['returns'].hist(bins=100,label='Ford',alpha=0.5)
plt.legend()
plt.savefig("./graphs/DailyPercentChange.png")
