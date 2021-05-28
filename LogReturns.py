import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2021, 1, 1)
tesla = web.DataReader("TSLA", 'yahoo', start, end)
ford = web.DataReader("F", 'yahoo', start, end)
gm = web.DataReader("GM", 'yahoo', start, end)

stocks = pd.concat([tesla['Close'],ford['Close'],gm['Close']],axis=1)
stocks.columns = ['tesla','ford','gm']
stocks.head()
stock_normed = stocks/stocks.iloc[0]
stock_normed.plot()

log_ret = np.log(stocks/stocks.shift(1))
log_ret.hist(bins=100,figsize=(12,6));
plt.tight_layout()
plt.savefig("./graphs/LogReturns.png")
