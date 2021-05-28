import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2021, 1, 1)
tesla = web.DataReader("TSLA", 'yahoo', start, end)
ford = web.DataReader("F", 'yahoo', start, end)
gm = web.DataReader("GM",'yahoo',start,end)

tesla.to_csv('./Tesla_Stock.csv')
ford.to_csv('./Ford_Stock.csv')
gm.to_csv('./GM_Stock.csv')

tesla['Volume'].plot(label='Tesla',figsize=(16,8),title='Volume Traded')
gm['Volume'].plot(label='gm')
ford['Volume'].plot(label='ford')
plt.legend()
plt.savefig("./graphs/Volume.png")
