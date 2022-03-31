---
parent: Pandas 
---

# Columns

### Drop columns
``` python 
df.drop(['B', 'C'], axis=1) 
df.drop(columns=['B', 'C']) # alternative approach
```
[SX](https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe?rq=1)

### Change order of columns 
- the easiest way is to reassign the dataframe, specifying the desired order of columns. 
- example: move the column 'mean' to the front (spelling out all column names)
	```python
	df = df[['mean', '0', '1', '2', '3']]
	```

to get a list of columns use: ``df.columns.tolist()`` *(this can avoid having to type out all the column names in larger dataframes)*
- example: move the columns 'HH_id' and 'ind_id' to the front (without having to spell out all the column names)
```python
rest = df.columns.tolist() # get a list of all column names
rest.remove('HH_id')       # remove the two column names from the list
rest.remove('ind_id')

df = df[['idhogar','Id']+rest]	# reorder the dataframe
```
- [Stackexchange](https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns):

### Rename columns
```python
df.rename(columns={'Old Name': 'New Name'}, inplace=True)
```
to rename a column that does not have a name simply use the index. Here an example for renaming the first column, which does not have an index
```python
# make an example dataframe
data = [1,4,6,2]
df = pd.DataFrame(list)
df.rename(columns={0:'Numbers'})
```

### Creating new columns
- using Boolean expressions
	caveat: when creating new columns using boolean expressions on existing columns, the operators `&` and `|` need to be used (instead of `and` and `or`), and each expression needs to be individual brackes [SX](https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o)
	
	```python
	df['isinquarter1'] = ( (df.var_datetime.dt.month>=1) & (df.var_datetime.dt.month<=3) ).astype('int')
	```

- using apply

### Dealing with hierarchical columns/hierarchical column indices
Example:
```python
import seaborn as sns
df_tips = sns.load_dataset('tips')
df_tips.columns
df_grouped = df_tips.groupby(by=['sex', 'time', 'day']).agg({'total_bill':['mean','sum'],'tip':['mean','sum']})

df_grouped # the columns now have a hierarchical index
```
Approach [1a](https://stackoverflow.com/questions/14507794/pandas-how-to-flatten-a-hierarchical-index-in-columns): simply rename the columns (combining the names of the different hierarchies into one using `strip()`)
```python
df_grouped.columns = [' '.join(col).strip() for col in df_grouped.columns.values]
```
Approach [1b](https://cmdlinetips.com/2020/05/fun-with-pandas-groupby-aggregate-multi-index-and-unstack/): take advantage of the fact that each element of df.columns is a tuple, and hence apply a function (namely `join()`, which takes an iterable and joins it using the separator it is chained to) to the tuple, in order to collapse each tuple into just a single string
```python
df_grouped.columns = df_grouped.columns.map('_'.join())
```
Approach [2](https://stackoverflow.com/questions/14507794/pandas-how-to-flatten-a-hierarchical-index-in-columns) (worse): rename the columns (discarding the names of lower columns)
```python
df_grouped.columns = df_grouped.columns.get_level_values(0)
```

### Replace values in a column
this is also useful for fixing weird encodings, i.e. when a dataframe is not consistently labelled, i.e. when in the same column 'no' is encoded sometimes as 'no' and sometimes as '0'
```python
df_train.edjefe.replace('no', 0 , inplace=True) # replace one value
df_train.edjefe.replace({'no': 0, 'yes': 1}, inplace=True) # replace several values using a dictionary
```
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html

### Iterate over columns:
``pd.DataFrame.items()``
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html

# Rows
### Drop rows:
- by condition:
	- Nutshell: select the rows using a condition (can also use a apply/map function to select the rows)
	- [SX](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression), answers 1 and 2 are great
- by location:
	- [SX1](https://stackoverflow.com/questions/15703283/pandas-drop-a-range-of-rows-from-df), [SX2](https://stackoverflow.com/questions/14661701/how-to-drop-a-list-of-rows-from-pandas-dataframe), [SX3](https://stackoverflow.com/questions/50974845/dropping-rows-in-pandas-with-index)

### Add a row:
simply add an index to the dataframe: [Medium](https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff)
```python
# setup
import pandas as pd
df = pd.DataFrame({ 'A': [1,2,3,4],
	'B': [10,20,30,40],  
    'C': [20,40,60,80]},   
	index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])
	

df.loc['Row 5'] = df.apply(lambda x:x.sum(), axis=0)
```

### Iterate over rows
``pd.DataFrame.iterrows``
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows

### Show specific row(s)
```python
print(df.iloc[[]])
```
https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe

### Create a row-complete dataset (i.e. that has an every hour and every location, even when this pair didn't occur in the original data)  
Situation:
- dataset of taxi rides in each zone during each hour (created by collapsing a dataset of individual taxi rides)
- some zones have no rides during a given hour
- due to the structure of the dataset, these observations are simply missing in the collapsed (i.e. there is no row for this zone and hour (which would indicate zero rides)

Want:
- but for visualisation/machine learning purposes we need to have an observation for every zone and hour, even when the number of rides is zero.

Solution:
- do this by re-indexing a dataset (as in my Kaggle notebook)
- [Medium](https://medium.com/when-i-work-data/using-pandas-multiindex-from-product-to-fill-in-missing-data-43c3cfe9cf39)


# Indices
Tricks with indices:
join two dataframes (which are aligned already) by simply appending the columns:
```python
# setup
import pandas as pd
df = pd.DataFrame({ 'A': [1,2,3,4],
	'B': [10,20,30,40],  
    'C': [20,40,60,80]},   
	index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])

def cal_multi_col(row):  
	return [row['A'] * 2, row['B'] * 3]

res = df.apply(cal_multi_col, axis=1,  result_type='expand')  # res is a dataframe with two columns
df[res.columns] = res
```


# Create new variables from a dataframe
[a great tutorial on apply, applymap, and map](https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff)
- apply(): go through a **dataframe** row by row (or column by column) and do something with each column
- map(): go through a **series** and apply something to each element. apply() on a series is equivalent (*I think?*) to map()
- applymap(): go through a **dataframe** and apply something to each element