---
parent: Pandas 
title: Deal with dates and geodata 
nav_order: 1b 
---

# Dates and Geodata in Pandas
{: .no_toc } 
<details open markdown="block"> 
  <summary> 
    Table of contents 
  </summary> 
  {: .text-delta } 
1. TOC 
{:toc} 
</details> 

# Dealing with dates
## When loading into Pandas
when loading data into Pandas, let it know that it is loading dates
specify the date column when loading the csv and pandas deals with it
```python
date_cols = ['pickup_datetime'] # specify which columns are dates
df = pd.read_csv("../input/new-york-city-taxi-fare-prediction/train.csv", parse_dates = date_cols)
```
---

## Retrospectively
Retrospectively denote a column in Pandas as a date column. (= convert a column in Pandas into a `datetime` column)

`make_date()` uses the Pandas function `to_datetime()`, which can convert dates/datetimes (even when they are split across several columns) into a single `datetime` column; see the [Pandas manual](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#converting-to-timestamps) for more. 
```python
# load sample dataset (from seaborn)
import seaborn as sns
taxis = sns.load_dataset("taxis")

# convert the variable pickup into a pandas datetime
taxis['date'] = pd.to_datetime(taxis['pickup'])
```
	
fast.ai has the function [`make_date()`](https://docs.fast.ai/tabular.core.html#make_date), which makes sure `df[date_field]` is of the right date type; it checks that it is, and if it isn't changes it to the right date type
```python
# load sample dataset (from seaborn)
import seaborn as sns
taxis = sns.load_dataset("taxis")

from fastai.tabular.all import *
# convert the variable pickup into a pandas datetime
make_date(taxis, 'pickup')
# check that it worked
test_eq(df['pickup'].dtype, np.dtype('datetime64[ns]'))
	```
	
---

## Automatically generate features (i.e. year, month, day, day of the week) from a timestamp
	
fast.ai has the function [`add_datepart()`](https://docs.fast.ai/tabular.core.html#add_datepart), which generates additional features from the column and returns a dataframe with the added features
```python
from fastai.tabular.all import * 
df = add_datepart(df, 'date')
```

it also drops the original column, so if you want to keep it, you need to feed a copy to add_datepart.

---
	
## Access/extract properties (i.e. year, day, hour) from a Pandas Timestamp 
Use the [dt.accessor](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#dt-accessor). 
List of time/date properties that can be accessed [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components)
```python
df['date_var'].dt.year
```
---
## Create a string variable (i.e. YYYY-MM) from a datetime
Use the function ``strftime()``. [see here](https://dfrieds.com/data-analysis/create-year-month-column.html)
```python	
df['yearmonth'] = df['datetimevar'].dt.strftime('%Y-%m')
```
	
# Dealing with geodata
Use [Geopandas](https://geopandas.org/gallery/create_geopandas_from_pandas.html) to deal with geodata in Pandas dataframes

## Load a shapefile of NYC taxi zones as a (geo)dataframe, display it, and plot it.

```python
# Load the zones
zones = gpd.read_file('../input/nyctaxizones/NYC Taxi Zones.geojson')
zones.head()) # show the header
zones.drop('geometry', axis=1).sample(10)) # show the entire dataframe, excluding the column geometry
zones.plot() # plot the shapefile as a map
```

## Turn a Pandas dataframe (which includes GPS coordinates) into a geodataframe.

This makes the coordinates usable as geodata.

Determine for each taxi ride which NYC taxi zone the ride starts in by performing a spatial join with the zone data.

#### EXAMPLE
```python
# PICKUPS:
gdf_pickup = gpd.GeoDataFrame( # create a geodataframe with the GPS coordinates of pickups
	df[['key','pickup_longitude','pickup_latitude']], 
	geometry=gpd.points_from_xy(df.pickup_longitude, df.pickup_latitude)) 
gdf_pickup.set_crs(epsg=4326, inplace=True) # set the CRS

pickups = gpd.sjoin(gdf_pickup, zones, how='left', op='intersects') # perform a spatial join between the GPS coordinates of pickups and the taxi zones
display_all(pickups.head(5)) # this dataset shows the zone of each pickup
```