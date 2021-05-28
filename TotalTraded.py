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

tesla['Total Traded'] = tesla['Open']*tesla['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']

tesla['Total Traded'].plot(label='Tesla',figsize=(16,8))
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Ford')
plt.legend()
plt.ylabel('Total Traded')

plt.savefig("./graphs/TotalTraded.png")
