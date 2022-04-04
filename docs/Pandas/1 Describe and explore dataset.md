---
parent: Pandas 
title: Describe and explore dataset 
navorder: 1 
---

``df.info()`` displays size of dataset (MB, # rows, # cols)
``df.head(5)`` display the top 5 rows; ``df.tail(5)`` for the bottom 5
``df.sample(10)`` display 10 sample rows
``df.columns`` displays the name of colums
``df.dtypes`` displays datatypes for all columns
``df.describe()`` describes all variables in the dataset (see below)
``df.series.value_counts()`` tabulate a series

### Display summary statistics for a dataset

define a function `display_all(df)`, which does not limit the number of lines that it shows
```python
def display_all(df):
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000): 
        display(df)
```

then display the summary statistics
```python
df.describe(include='all').T
```

use the option `datetime_is_numeric=True` to also display mean, min, and max (and percentiles) for the date variable

### Describe missing values
see [[Pandas - 1b Deal with missing observations]]


### Describe an individual variable
- graph it ([Pandas manual](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#))
	```python
	df.variable.plot() # plots the series (and index) as a line plot
	```
	
	The Pandas graphing library does not summarize/preprocess the data in any way. 
	- plot (line plot): line plot of variable(s) (y-axis value, x-axis index). Hence, usually for time series or where the index has some sort of meaning
	- bar (if given a row): each variable is plotted as a different bar (one observation, several variables)
	- bar (if given a dataframe): each row is plotted in a different group, and within that group, each variable is plotted in a different bar (the bars can be stacked) (several observations, several variables)
	- histogram, box plots, kde/density plots: many observations, one variable
	- scatter, hexagonal bin plot (show every point for two(x,y), three (x,y,colour), or four (x,y,colour,size) variables): many observations, 2-4 variables

- tabulate it: 
```python
df.variable.value_counts() # sorted by frequency (sort is true by default)
df.variable.value_counts().sort_index() # sort by value 
```


### Calculate summary statistics (by groups)
