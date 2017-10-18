Introduction
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
Russian and global macroeconomic time series data with public end-user API.

It is inspired by [St Louis FRED](https://fred.stlouisfed.org) and 
[Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)
and aims to provide open, timely, machine-readable data for reproducible 
analysis in economics.


User case
=========

We assume an end user has some experience with [FRED](https://fred.stlouisfed.org) 
or [quandl](https://www.quandl.com/). 

For his work an end user wants:

- a clean dataset with latest data from different sources
- browse what data is available
- read this data on a local machine (in ```pandas``` or ```R```)
- quickly draw some charts like one below: 

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

er = read_ts('http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017')
assert er['2017-09-28'] == 58.01022

```

Click [here](http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017) to see same data in browser.

Github
======

This documentation source is stored on [Github](https://github.com/mini-kep/documentation)
