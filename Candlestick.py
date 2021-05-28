import pandas as pd
import datetime
import mplfinance as mpf

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2021, 1, 1)
ford = pd.read_csv('./Ford_Stock.csv', index_col=0, parse_dates=True)

dt_range = pd.date_range(start="2020-03-01", end="2020-03-31")
ford = ford[ford.index.isin(dt_range)]

mpf.plot(ford, type="candle",title='Ford March-2020', style='starsandstripes', savefig="./graphs/Candlestick.png");

