import pandas as pd

def read_ts(source_url):
	"""Read pandas time series from *source_url*."""
	return pd.read_csv(source_url, 
                      converters={0: pd.to_datetime}, 
                      index_col=0,
                      squeeze=True)

er = read_ts('http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017/')
brent = read_ts('http://mini-kep.herokuapp.com/oil/series/BRENT/d/2017/')



# example with partial
from functools import partial
read_csv = partial(pd.read_csv, converters={0: pd.to_datetime}, index_col=0)
read_json = partial(pd.read_json, precise_float=True, orient='split')
