Overview
========
Custom API is a simplified interface for end-user queries from database. 
It uses long URL with slashes and no other parameters.

Сustom API is intended to allow:

1. intuitive construction of URL for user
2. shorter notation than standard database API GET method 
3. addressing several database API endpoints in one place
4. uniform call to same indicator for different countries or regions

API design originally discussed at [this issue](https://github.com/mini-kep/frontend-app/issues/8).

Custom API translates to db API 
===============================

Custom API is essentially a thin syntax layer on top of database API. 
All calls to custom API are redirected to database API. 

For example, this call to custom API: 

```http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2015/2017```

will return same data as:

```https://minikep-db.herokuapp.com/api/datapoints?name=CPI_rog&freq=m&start_date=2015-01-01&end_date=2017-12-31```

   
URL syntax
==========

Custom API url syntax is the following:

```
{domain}/series/{varname}/{freq}/{?suffix}/{?start}/{?end}/{?finaliser}

? - optional

Examples:
   oil/series/BRENT/m/eop/2015/2017/csv
   ru/series/EXPORT_GOODS/m/bln_rub   
```

For further details, refer to the docstring in 
[custom_api.py](https://github.com/mini-kep/helper-custom-api/blob/master/src/custom_api.py) file.

Expected usage of ```{domain}``` is to get similar data 
for different countries or regions by changing a little part of custom URL:

```
   ru/series/CPI/m/2017  # country-level inflation for Russia 
ru:77/series/CPI/m/2017  # inflation for Moscow region                         
   kz/series/CPI/m/2017  # country-level inflation for Kazakhstan
```

Output format
=============

By default custom API returns CSV file. This file is:

- viewable in browswer (download does not start)
- readable by R/pandas

Optional  ```{finaliser}``` may alter output format.
  
Implementation
==============

Custom API currently developped and tested at 
[own repo](https://github.com/mini-kep/helper-custom-api/blob/master/src/custom_api.py)
and mounted at [frontend app](https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py).

Next steps
==========

- [Mount custom API at db app](https://github.com/mini-kep/helpers/issues/13)
