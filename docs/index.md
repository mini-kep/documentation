Introduction
============

```mini-kep``` is a small ETL (extract, transform, load) framework for 
Russian and global macroeconomic time series data with public end-user API.

```mini-kep``` collects data from static files and public APIs,
saves it in database and provides end-user interface to browse this data 
and read it into R/pandas for visualisation and modelling.  

Inspired by [St Louis FRED](https://fred.stlouisfed.org) and 
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


Example: read official daily ruble/usd exchange rate from start of 2017

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

Project repositories and links
==============================

[Parsers](https://github.com/mini-kep/parsers):
data source descriptions and parser code.

[Database layer](https://github.com/mini-kep/db):
API and database for data storage and [retrieval](https://github.com/mini-kep/db#sample-get-calls), 
hosted at  
```https://minikep-db.herokuapp.com/api/```

[Frontend app](https://github.com/mini-kep/frontend-app):
can be viewed in browser at <https://mini-kep.herokuapp.com>, relies on API above. 

[End user code](https://github.com/mini-kep/user-charts):
а collection of Jupiter notebooks to demostrate data use. 
