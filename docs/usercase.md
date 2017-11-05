**Web interface user**  wants to: 

- browse available dataset on a web site 
- select some time series to compare 
- download selected data locally 

This user is likely to use data browser at <http://macrodash.herokuapp.com/>. 

**```R``` or ```pandas``` users**  with experience
in [FRED](https://fred.stlouisfed.org) 
or [quandl](https://www.quandl.com/) would want: 

- a clean dataset with latest data from different sources
- download this data on a local machine (in ```pandas``` or ```R```)
- quickly draw some charts (like one below)
- develop explanatory/forecasting models and share them as IPython notebooks.

[![](http://datachart.cc/images/rub_oil.png)](http://datachart.cc/)

**Example: read official daily ruble/usd exchange rate from start of 2017**

```python 
import pandas as pd

def read_ts(source_url):
	"""Read pandas time series from *source_url*."""
	return pd.read_csv(source_url, 
                      converters={0: pd.to_datetime}, 
                      index_col=0,
                      squeeze=True)

er = read_ts('http://minikep-db.herokuapp.com/ru/series/USDRUR_CB/d/2017')
assert er['2017-09-28'] == 58.01022

```

Click [here](http://minikep-db.herokuapp.com/ru/series/USDRUR_CB/d/2017) to see 
the same data in browser.

See [end_use.py](examples/end_use.py) for examples of end user code.
