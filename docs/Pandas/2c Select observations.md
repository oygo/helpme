---
parent: Pandas 
title: Select observations 
nav_order: 2c 
---

# Selecting data in Pandas
{: .no_toc } 
<details open markdown="block"> 
  <summary> 
    Table of contents 
  </summary> 
  {: .text-delta } 
1. TOC 
{:toc} 
</details> 

## The clearest way: .loc and .iloc
1.  Use ``.loc[]`` for label-based indexing
2.  Use `.iloc[]` for position-based indexing, and
3.  Explicitly designate both the rows and the columns even if it’s with a colon.

#### Example setup
The goal is to identify a single strategy for pulling data from a DataFrame that is straightforward to interpret and produces reliable results.

Assume we have a small data frame using data from Wikipedia on the highest mountains in the world. For each mountain, we have its name, height in meters, year when it was first summitted, and the range to which it belongs. Each mountain and its associated information is a row, and each piece of information, for instance name or height, is a column.
![](https://e2eml.school/images/pandas_indexing_1.png)

Each column has a name associated with it, also known as a label. The labels for our columns are 'name', 'height (m)', 'summitted', and 'mountain range'. In pandas data frames, each row also has a name. By default, this label is just the row number. However, you can set one of your columns to be the index of your DataFrame, which means that its values will be used as row labels. We set the column 'name' as our index.

#### Designate a column of row labels as an index
![](https://e2eml.school/images/pandas_indexing_2.png)

It is a common operation to pick out one of the DataFrame's columns to work on. To select a column by its label, we use the .loc[] function. One thing that we can do that makes our commands easy to interpret is to always include both the row index and the column index that we are interested in. In this case, we are interested in all of the rows. To show this, we use a colon. Then, to indicate the column that we're interested in we add its label. The command mountains.loc[:, 'summitted'] gets us just the 'summitted' column.

#### Select a column by name (label)
![](https://e2eml.school/images/pandas_indexing_3.png)

It’s worth noting that it this command returns a Series, the data structure that pandas uses to represent a column. If instead of a Series, we just wanted an array of the numbers that are in the 'summitted' column, then we add '.values' to the end of our command. This returns a numpy array containing [1953, 1954, 1955, and 1956].

![](https://e2eml.school/images/pandas_indexing_4.png)

If we would only like to get a single row, then we use the .loc[] function again, this time specifying a row label, and putting a colon in the column position.

#### Select a row by label
![](https://e2eml.school/images/pandas_indexing_5.png)


If we only want a single value, for instance the year that K2 was summitted, then we can specify the labels for both the row and the column. The row always comes first.

#### Select a value by row and column label
![](https://e2eml.school/images/pandas_indexing_6.png)

While it is true that you can get away with using only one argument in the .loc[] function, it is most straightforward to interpret if you always specify both row and column, even if it is with a colon.

We don’t have to limit ourselves to a single row or single column using this method. Here, in the row position we pass a list of labels. This returns a set of rows, rather than just one.

#### Select several rows by label
![](https://e2eml.school/images/pandas_indexing_7.png)

We can also get a subset of the columns, by specifying the start and end column, and putting a ':' in between. In this case, 'height': 'summitted' will give us all of the columns between and including the startpoint, 'height', and the endpoint, 'summitted'. Note that this is different than numerical indexing in numpy, where the endpoint is omitted. Also, because we have already specified the name column as the index, it will also be returned in the data frame that we get back

# Select several columns by label
![](https://e2eml.school/images/pandas_indexing_8.png)

In addition, we can select rows or columns where the value meets a certain condition. In this case, we want to find the rows where the values of the 'summitted' column are greater than 1954. In the rows position, we can put any Boolean expression that has the same number of values as we have rows. We could do the same for columns if we wished.

#### Select rows based on a column value (observations meeting certain criteria)
![](https://e2eml.school/images/pandas_indexing_9.png)

As an alternative to selecting rows and columns by their labels, we can also select them by their row and column number. The ordering of the columns, and thus their positions, depends on how the data frame is initialized. The index column, our 'name' column, doesn’t get counted.

#### Select rows and columns by position
![](https://e2eml.school/images/pandas_indexing_10.png)

To select data by its position, we use the .iloc[] function. Again, the first argument is for the rows, and the second argument is for the columns. To select all the columns in the zeroth row, we write .iloc[0, ;]

![](https://e2eml.school/images/pandas_indexing_11.png)

Similarly, we can select a column by position, by putting the column number we want in the column position of the .iloc[] function.

![](https://e2eml.school/images/pandas_indexing_12.png)

We can pull out a single value, by specifying both the position of the row and the column.

![](https://e2eml.school/images/pandas_indexing_13.png)

We can pass a list of positions if we want to cherry pick certain rows and/or certain columns.

![](https://e2eml.school/images/pandas_indexing_14.png)

We can also use the colon range operator to get a contiguous set of rows or columns by position. Note that unlike the .loc[] function using labels, the .iloc[] function using positions does not include the endpoint. In this case, it returns only columns zero and one, and does not return column two.


#### .loc when using Multiindexes
- when working with multi-indices, simply pass a tuple to `.loc`
- when you want to get all values from specific level of hierarchy, use `slice(None)`

example 
- (screenshot here)
- the columns have a hierarchical/multiindex (year, month, measure)
- to get the values for a specific year, use `df.loc[:,(2008,slice(None),slice(None))]`
- to get all measures for January of all years, use `df.loc[:,(slice(None),'01',slice(None))]`



## The indexing operator `df[here]`
The indexing operator is overloaded. This means, that depending on the inputs, pandas will do something completely different. Here are the rules for the different objects you pass to the indexing operator.

-   string — return a **column** as a Series
-   list of strings — return all those **columns** as a DataFrame
-   a slice — select **rows** (can do both label and integer location — confusing!)
-   a sequence of booleans — select all **rows** where **`True`**

In summary, primarily _just the indexing operator_ selects **columns**, but if you pass it a sequence of booleans it will select all **rows** that are **`True`**. 
This is the (shortcut) approach we often take when we want to select rows meeting specific criteria.

## More ways for selecting rows meeting specific criteria
- see [this post](https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c) for more
- we generally use boolean selection

![](https://miro.medium.com/max/1225/1*6IeCRgckPO-SI6bj5VUGYA.png)

#### Simple conditions
- select all rows with score with a score higher 10: `df[df['score'] >= 10]`

What happens behind the scenes?
- the inner `df[score] >= 10` creates a boolean series (with the same length as the df)
- the outer `df[ ]` then performs a boolean selection on `df[score] >= 10` and returns only the selected rows

Operators
- the 6 comparison operators: 
	- `<`  for smaller
	- `<=` for smaller or equal
	- `>` for greater
	- `>=` for greater or equal
	- `==` for equal
	- `!=`  for not equal
- multiple conditions: 
	- `&` for **and**
	- `|` for **or**
	- `~` for **not**

#### Complex conditions and specific operators
- use brackets `(` and `)` for more complex conditions
- instead of lots of `or` conditions in single column: use `isin` 
	- instead of:
	```python
	criteria = ((df['ans_name'] == 'Scott Boston') |  
	(df['ans_name'] == 'Ted Petrou') |  
	(df['ans_name'] == 'MaxU') |  
	(df['ans_name'] == 'unutbu'))
	```
	- use:
	``` python
	criteria = df['ans_name'].isin(['Scott Boston', 'Ted Petrou',   'MaxU', 'unutbu'])
	```
- for complex conditions (1): split complex conditions into criteria:
```python 
criteria_1 = df['ans_name'].isin(['Scott Boston', 'Ted Petrou',  
'MaxU', 'unutbu'])  
>>> criteria_2 = df['score'] > 30  
>>> criteria_all = criteria_1 & criteria_2  
>>> df[criteria_all].tail()
```
- for complex conditions (2): calculate the criterion using map or apply
```python 
# Example dataset
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

# filter by one criterion
df[df['A']=='foo']

# filter by multiple criteria
df[(df['A']=='foo') & (df['B']=='one') ] 

# filter by complex criteria (example: only observations where the word in the second column starts with 't'): 
criterion = df['B'].map(lambda x: x.startswith('t')) # first approach: using the map method
```

- to find rows with missing values use `isnull`

## on a sidenote: `.loc[]` also allows Boolean selection

## Never use .ix: .ix is deprecated

## Random further tricks:
#### using where
Boolean indexing returns a subset of the data: 
to guarantee that the output has the same shape as the original data, the [where()](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-where-method-and-masking) method can be used. This returns a true/false mask of the size of the original dataset.

## 4 great resources
- Official Pandas tutorial: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
- great overview: https://e2eml.school/dataframe_indexing.html
- comprehensive 4-part series on Pandas indexing: https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
- Official Pandas user guide: https://pandas.pydata.org/docs/user_guide/indexing.html