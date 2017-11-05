```mini-kep``` collects data from static files and public APIs,
saves it in database and provides end-user interface to browse this data 
and read it with R/pandas for visualisation and modelling.  

## 1 [Parsers](https://github.com/mini-kep/parsers)

   - download data from static files or other APIs 
   - assign variable names from common namespace 
   - emit stream datapoints (observations)
   - each observation is a dictionary like:  
   
```{'name': USDRUR_CB, 'date': '2017-09-28', 'freq': 'd', 'value': 58.0102}```

## 2 Scheduler

   - establish expected database content based on current date 
   - query parsers for missing data 
   - upload to database
   - implemented as python script run by heroku scheduler

## 3 [Database](https://github.com/mini-kep/db)

   - flask app with SQLAlchemy and Postgres backend 
   - has REST API to upload and retreive data
   - has custom API with simplified query syntax to retrieve data 

## 4 [Data browser](https://github.com/mini-kep/frontend-dash)

   - plotly/dash app deployed at <https://macrodash.herokuapp.com)>
   - allows browsing dataset by frequency and variable name 
   - provides download links
   

## 5 [Notebooks](https://github.com/mini-kep/user-charts)

   - data access examples for end-user API
   - charting macroeconimic data
   - collection of Jupiter notebooks to demostrate visualisation and modelling
	
**Comments**
	
1. Pipeline is illustrated [here](https://github.com/mini-kep/intro/blob/master/pipeline/pipeline.py)
2. Common namespace discussed [here](https://mini-kep.github.io/documentation/datamodel_and_namespace/)
	