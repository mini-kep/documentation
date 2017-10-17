Overview
========

This document describes initial reuiqrement for database. 
Please refer to [README.md](https://github.com/mini-kep/db) for newest data. 

Expected fucntionality
======================

- parser delivers a list of dicts, each dict is a datapoint
- database should have a POST method at ```api\incoming``` and write incoming json to db
- POST operation must have some authentication
- for simplicity all data is upserted - newer data always overwrites older data
- database has GET method with datapoint keys as parameters (variable name, frequency),
- GET returns same format of output as incoming, output ordered by date, optionally    
  filtered by start date and end date 

Database schema
===============

Table **Datpoint**
```
Id – UID, autoincrement  
Name – type String \*  eg GDP
Freq – type String \*  
Date – type DateTime \*  2016-12-31
Value – Float  

\* - composite key
```

See example at <https://github.com/mini-kep/db/blob/master/demo/sqlalchemy/datapoint.py>

Data structures
===============

** Incoming / outgoing JSON**

```python 
[
    {
        "date": "2016-06-30",
        "freq": "m",
        "name": "CPI_rog",
        "value": 100.4
    },
    {
        "date": "2016-06-30",
        "freq": "m",
        "name": "EXPORT_GOODS_bln_usd",
        "value": 24.0
    },

	# ...
	
]	
```

Parser result is obtained [here](https://github.com/mini-kep/parsers/blob/master/parsers/runner.py)
from   ```Dataset.yield_dicts(start='2017-01-01')```. See ```Dataset.serialise()``` for json creation.
Sample json is [here](https://github.com/mini-kep/parsers/blob/master/parsers/test_data_2016H2.json)
 

** Outgoing CSV **

```
,GDP_yoy
2016-03-31,99.6
2016-06-30,99.5
2016-09-30,99.6
2016-12-31,100.3
2017-03-31,100.5
2017-06-30,102.5
```

Database methods
================

POST
----

```POST api/incoming``` 

Validates incoming json and upsert values to database. All fields should be filled.

For ```insert_many()``` operation see [*'sheep/flock'* example](https://stackoverflow.com/a/33768160/1758363)

Returns:
- empty JSON on success
- error 400 on error in incoming json (eg invalid date string or empty parameter or missing field)

POST methods should require API_TOKEN as URL parameter or header, validate it with environment variable (possibly Heroku config vars)


GET
---

```
GET api/datapoints?name=<name>&freq=<freq>
GET api/datapoints?name=<name>&freq=<freq>&start_date=<start_date>&end_date=<end_date>
```

Parameters:

- name (required) – name value to search like name=BRENT
- freq (required) – freq value to search like freq=m
- start_date (optional) – should return results with date greater than this parameter
- end_date (optional) – should return results with date less than this parameter
- format (optional, possible values ```json, csv```, default ```csv```) – returns data in chosen format. CSV data can be read by pandas with ```pd.read_csv(url_to_api_request)```

Returns:

- CSV or JSON (default CSV) in format similar to incoming json with data sorted by date
- empty CSV or JSON if there’s no data with such query.
- returns error 400 on error in parameters


Tests (to edit)
===============

Upload data from JSON to DB, run python unit tests with requests to different methods, validate them with uploaded data.

Use combinations GET – POST – GET to validate data inserts and updates.

[Example1](https://github.com/mini-kep/db/blob/master/demo/sqlalchemy/tests/test_clientdb_demo.py)
[Example2](https://github.com/mini-kep/full-app/blob/master/datapoint/tests.py)

Should we write some [tests in curl/httpie](https://github.com/mini-kep/db/blob/master/requests_tests.py)? 

Tech stack
==========

Web-frameworks: Flask + SQLAlchemy, alternative - Django, may consider Falcon

Container: prototype deployed to Heroku, alternative - use AWS EBTalk

Database: Postgres (default on Heroku*), alternative - AWS RDS


Repositories
============

[db](https://github.com/mini-kep/db): 
[![Build Status](https://travis-ci.org/mini-kep/db.svg?branch=master)](https://travis-ci.org/mini-kep/db)

Note: there is also [django project for database](https://github.com/mini-kep/full-app), but it is on hold now.