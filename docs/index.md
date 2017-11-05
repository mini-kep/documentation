Introduction
============

```mini-kep``` is a small ETL (extract, transform, load) framework and a dataset for 
Russian and global macroeconomic time series with public end-user API.

This work is inspired by [St Louis FRED](https://fred.stlouisfed.org) and 
[Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science)
and aims to provide open, timely, machine-readable data for reproducible 
analysis in economics.

Poll
====

Please [fill a poll about data sources](https://goo.gl/2wY43R) to support our case.  

Motivation
===========
 
Why another database for macroeconomic data? 
 
- Machine-readable datafeeds for economic data are growing ([FRED](https://research.stlouisfed.org/docs/api/fred/), 
  [quandl](https://blog.quandl.com/api-for-economic-data), 
  [OECD](https://data.oecd.org/api), 
  [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589), 
  [EIA](https://www.eia.gov/opendata/)).

- However, some data is still left in the dark. Russian macroeconomic statistics seems very 
  fragmented (HTML, Word, Excel are common dessimination formats). 
  This is a roadblock to reproducible analysis as dirty data escalates costs of model maintenance.      

- ```mini-kep``` aims to remove this roadblock by providing 
  [public API for Russian macroeconomic data](http://mini-kep.herokuapp.com/) 
  and examples of economic research/business planning/marketing problems 
  solved in python pandas or R.

Project links
=============

Data browser: <http://macrodash.herokuapp.com>

Repositories:

- [parsers](https://github.com/mini-kep/parsers)
- [database](https://github.com/mini-kep/db)
- [data browser](https://github.com/mini-kep/frontend-dash)
- [user charts](https://github.com/mini-kep/user-charts)

This documentation is stored at <https://github.com/mini-kep/documentation>.