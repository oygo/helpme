---
has_children: true 
parent: Pandas 
title: Load data 
nav_order: 0a 
---

# Load data into Pandas

{: .no_toc } 
<details open markdown="block"> 
  <summary> 
    Table of contents 
  </summary> 
  {: .text-delta } 
1. TOC 
{:toc} 
</details>] 

## from a CSV file

```python
df = pd.read_csv("../input/new-york-city-taxi-fare-prediction/train.csv")
```

### **For files stored on github:** to load a CSV file that's stored on Github, append ``?raw=true`` to the URL. 
Example: https://github.com/nguyen-toan/ISLR/blob/master/dataset/Advertising.csv isn't actually the URL to the file, but is a Github homepage previewing the file. 	https://github.com/nguyen-toan/ISLR/blob/master/dataset/Advertising.csv?raw=true is the actual file. [see here](https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas)

### How to deal with dates
specify the date column when loading the csv and pandas deals with it

```python
date_cols = ['pickup_datetime'] # specify which columns are dates
df = pd.read_csv("../input/new-york-city-taxi-fare-prediction/train.csv", parse_dates = date_cols)
```

### Tricks when the CSV file is very large:
1. take a look at it in the linux shell first (and count the number of lines) 
	```shell 
	! head -n 5 ../input/new-york-city-taxi-fare-prediction/train.csv
	! cat ../input/new-york-city-taxi-fare-prediction/train.csv | wc -l
	```
	[look here for Windows equivalent](https://superuser.com/questions/959036/what-is-the-windows-equivalent-of-wc-l)
2. only load the first N lines into Pandas
	```python
	# Load rows 1000-1999 of the dataset (= load 1000 rows after skipping the first 1000)
	df = pd.read_csv('../input/new-york-city-taxi-fare-prediction/train.csv', sep=',', skiprows= 1000, nrows=1000)

	# Do the same, now also labelling the columns (with the names extracted from the unix shell)
	df = pd.read_csv('../input/new-york-city-taxi-fare-prediction/train.csv', names=['key','fare_amount','pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count'], sep=',', skiprows= 1000, nrows=1000)
	```
3. only load a random subset of N lines into Pandas [SX](https://stackoverflow.com/questions/22258491/read-a-small-random-sample-from-a-big-csv-file-into-a-python-data-frame)
	```python
	n = 55423856 - 1 # number of records in file (excludes header)
	s = 100000 # desired sample size
	filename = "../input/new-york-city-taxi-fare-prediction/train.csv" 
	skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
	df = pd.read_csv(filename, skiprows=skip)
	```

Always: attempt to reduce the memory usage of the dataframe. The fast.ai tabular library has the function [df_shrink](https://docs.fast.ai/tabular.core.html#df_shrink), which automatically changes the datatype of each column to the one that uses least space (while still being able to contain the data)

```python
from fastai.tabular.all import *
df2 = df_shrink(df) # use the function to shrink

df.info(verbose=True) # show the data for the old dataframe
df2.info(verbose=True) # show the data for the new dataframe
```

df_shrink also converts objects into categories, but this might not always be the best approach. Set the option obj2cat = False to avoid this, and see if this reduces size more. 
``` python
df2 = df_shrink(df, obj2cat=False)
df2.info(verbose=True)
```



## from an Excel file

```python
df = dataframe = pd.read_excel(url, sheetname=0, header=1)
```


## from a SQL database

``` python
# Load libraries
import pandas as pd
from sqlalchemy import create_engine
# Create a connection to the database
database_connection = create_engine('sqlite:///sample.db')
# Load data
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)
# View first two rows
dataframe.head(2)
```

## using Google Big Query


## from an R file:
Pyreadr seems to be the go-to Python library
https://github.com/ofajardo/pyreadr
