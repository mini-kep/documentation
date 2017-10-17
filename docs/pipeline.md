Data pipleline
==============

```mini-kep``` collects data from static files and public APIs,
saves it in database and provides end-user interface to browse this data 
and read it with R/pandas for visualisation and modelling.  

## 1 [Parsers on static files or other APIs](https://github.com/mini-kep/parsers)

   - download data from source 
   - assign variable names from common namespace 
   - emit stream of dictionaries like  
     ```{'name': USDRUR_CB, 'date': '2017-09-28', 'freq': 'd', 'value': 58.0102}```

## 2 Scheduler

   - establish expected database content based on current date 
   - query parsers to get expected data 
   - resolve import conflicts (overwriting data on revision or same data from different sources)
   - upload to database

## 3 [Database](https://github.com/mini-kep/db)

   - flask app with SQLAlchemy and Postgres backend 
   - has REST API to upload and [retreive](https://github.com/mini-kep/db#get-calls) data
   - has custom API to retrive data, custom API maps simplified query syntax to REST API

## 4 [Frontend app](https://github.com/mini-kep/frontend-app)

   - project [news and how-to](https://mini-kep.herokuapp.com)
   - relaying data from database query API
   - html content for viewing data withi charts (not implemented)
   - social links for charts (not implemented)

## 5 [End-user examples](https://github.com/mini-kep/user-charts)

   - data access examples for end-user API
   - charting macroeconimic data
   - collection of Jupiter notebooks to demostrate data use (visualisation/modelling)
	
**Comments**
	
1. Pipeline is illustrated [here](https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py)
2. Common namespace discussed [here](https://mini-kep.github.io/documentation/datamodel_and_namespace/)
	