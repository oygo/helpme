---
parent: Pandas 
title: Plot data 
nav_order: 2e 
---

# Plot data for exploration

## Pairwise plot of data
Quick approach: use [seaborn.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
sns.pairplot(penguins)
```


Tricks:
- only plot some variables (or plot them in a different order)
	``` python 
	import seaborn as sns
	penguins = sns.load_dataset("penguins")
	
	columns_i_want = ['bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
	sns.pairplot(penguins[columns_i_want])
	```

Options:
- only plot the lower triangle
`` sns.pairplot(penguins, corner=True) ``
- use colour to denote a third dimension: hue
`` sns.pairplot(penguins, hue="species")``
- draw histograms or kernel densities instead of dots (not as intuitive, but helpful when there are too many dotes)
	`` sns.pairplot(penguins, kind="hist")``
	`` sns.pairplot(penguins, kind="kde")``


Further points:
- seaborn allows to separately specify what is displayed on the lower triangle, the diagonal, and the upper triagonal. 
For example, this allows: a scatterplot on the lower triangle, histogram of the variable on the diagonal, and a kernel density plot on the upper triangle. For this seaborn has the ``pairgrid``, which is a class that does not automatically fill the grid, but allows to subsequently specify what's displayed. See on [Medium](https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166) (just before the conclusion) and the [Seaborn manual](https://seaborn.pydata.org/generated/seaborn.pairplot.html) for an explanation

``` python
# Create an instance of the PairGrid class.  
grid = sns.PairGrid(data= penguins, vars = ['bill_depth_mm', 'flipper_length_mm', 'body_mass_g'], size = 3)

# Map a scatter plot to the upper triangle  
grid = grid.map_upper(plt.scatter, color = 'darkred')
# Map a histogram to the diagonal  
grid = grid.map_diag(plt.hist, bins = 10, color = 'darkred',  
edgecolor = 'k')
# Map a density plot to the lower triangle  
grid = grid.map_lower(sns.kdeplot, cmap = 'Reds')
```


## Visualise activity in a calendar:  Github-style heatmap

[calplot](https://calplot.readthedocs.io/en/latest/) (also [here](https://github.com/tomkwok/calplot)) creates a Github-style calendar showing activity. As input calplot takes a Pandas **series** (of events), which has a datetime index. 

Calplot then counts how many observations there are for each index (i.e. each date) and visualises this in a calendar.

```python
# ! pip install calplot
import calplot as calplot
import seaborn as sns

taxis = sns.load_dataset("taxis") # load dataset
taxis['date'] = pd.to_datetime(taxis['pickup']).dt.date # create a date variable
taxis.set_index(pd.DatetimeIndex(taxis['date']), inplace=True) # index the dataframe by date

calplot.calplot(taxis.passengers) # feed a series to calplot (because calplot takes a series, I am feeding it a specific variable instead of the dataframe. I could have picked any variable here)
calplot.calplot(taxis.passengers, textformat='{:.0f}', figsize=(24, 3), vmin=200 ) # alternative visualisation with some options
```

Alternative packages/other options:
- [july](https://github.com/e-hulten/july): additionally allows to plot months, and to plot a year in calendar format (i.e. separate as months). 
Unlike calplot, july takes as input a dataframe that has one observation for each date (and a separate variable which states the count/variable that is to be visualised) for that date. This makes it well-suited to also visualise data other than activity (for example, temperatures). When visualising frequencies, this means that the pandas dataframe needs to be grouped first.)
I haven't tried it out, but it looks like a neat package.
- [Calmap](https://github.com/MarvinT/calmap/): is the father of calplot, but calplot seems to have easier customisation.
	```python
	# !pip install calmap
	import calmap
	import seaborn as sns

	taxis = sns.load_dataset("taxis") 

	# Create a date variable
	taxis['date'] = pd.to_datetime(taxis['pickup']).dt.date

	# Index the dataframe by date
	taxis.set_index(pd.DatetimeIndex(taxis['date']), inplace=True)

	# Pass a series to calmap (instead of passengers, I could have picked any variable)
	calmap.yearplot(taxis.passengers, year=2019)
	```

- an alternative (less pretty, but potentially more customizable way) would be to plot this as a heatmap (in seaborn or matplotlib)