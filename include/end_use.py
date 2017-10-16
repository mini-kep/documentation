import pandas as pd

def read_ts(source_url):
	"""Read pandas time series from *source_url*."""
	return pd.read_csv(source_url, 
                      converters={0: pd.to_datetime}, 
                      index_col=0,
                      squeeze=True)

er = read_ts('http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017/')
brent = read_ts('http://mini-kep.herokuapp.com/oil/series/BRENT/d/2017/')


# other urls - most not implemented yet

# monthly average Brent oil prices starting 2000 to present 
brent_m = read_ts('http://minikep.cc/oil/series/BRENT/m/avg/2000')

# monthly average Russian rouble exchange rate, same period
er_m = read_ts('http://minikep.cc/ru/series/USDRUR/m/avg/2000')

# monthly consumer inflation in different countries in 2017
# 'rog' = rate of growth 
cpi_ru = read_ts('http://minikep.cc/ru/series/CPI/m/rog/2017')
cpi_us = read_ts('http://minikep.cc/us/series/CPI/m/rog/2017')


# example with functools.partial
from functools import partial
read_csv = partial(pd.read_csv, converters={0: pd.to_datetime}, index_col=0)
read_json = partial(pd.read_json, precise_float=True, orient='split')
