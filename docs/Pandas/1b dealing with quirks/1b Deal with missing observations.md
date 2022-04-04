---
parent: 1b Dealing with quirks 
title: Deal with missing observations
nav_order: 1b
---

### Describe missing values in Pandas

```python
# print for each column the number of observations which have missing values
transaction_df.isna().sum()
```

### Visualise missing values
[missingo](https://github.com/ResidentMario/missingno) is a module to visualise data completeness and missing variables easily

```python
import missingno as msno
import pandas as pd
collisions = pd.read_csv("https://raw.githubusercontent.com/ResidentMario/missingno-data/master/nyc_collision_factors.csv")

# visualise the data as rows
msno.matrix(collisions.sample(250)) # line

# draw a bar chart, showing for each variable the number of missing observations
msno.bar(collisions)

# correlations between missing variables (as a heatmap)
msno.heatmap(collisions)

# dendrogram
msno.dendrogram(collisions)
```

 missingno can be [further configured](https://github.com/ResidentMario/missingno/blob/master/CONFIGURATION.md)




### Deal with missing values: fill them using pandas.fillna()

1. fill just one column
	```python
	df['income'].fillna((df['income'].mean()), inplace=True)
	```
	can also fill this column with the `median()`, `mode()`, a specific value or whatever

2. fill all columns
	```python
	df.fillna(df.mean())
	```

	Example:

	```python
	df = pd.DataFrame(np.random.randn(10,4))
	df.iloc[3:5,0] = np.nan
	df.iloc[4:6,1] = np.nan
	df.iloc[5:8,2] = np.nan

	df

	df.fillna(df.mean(),inplace=True)
	```


3. Keep track of which missing values were filled:

	Create variables that indicate - for a given observation - whether a value was missing.

	In order to keep track of which missing values were 'imputed', run this code first. For each column which had missing values, this creates a new column indicating observations where the value was missing.

	```python
	for col in df.columns:
		# create the indicator variable only when a variable had any missing values in the first place
		if df[col].isnull().sum()>0:
			# create a variable equal 1 if the value is missing (for the given observation)
			df[str(col)+'_isna'] = df[col].isnull().astype(int)
	```


### Imputation to deal with missing data:

Concepts:
- Conceptual frameworks: missing at random, missing conditionally at random, not missing at random
- single imputation, multiple imputation (Q: why multiple imputation? A: to account for uncertainty)
- univariate vs. multivariate imputation (univariate = when filling a missing value, only use this variable to value to decide a value to fill with; multivariate imputation = when filling a missing value, decide what the imputed value should by considering the observation as a whole, taking into account other feature dimension to decide on the missing value)

Book that I think we used at the IDinsight book club: https://stefvanbuuren.name/fimd/

Imputation in scikit-learn; imputation in statsmodels
