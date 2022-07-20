---
parent: Pandas 
title: Select observations 
nav_order: 2c 
---

# Select observations

## Indexing
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

df

```

## Boolean indexing:
```python 
# filter by one criterion
df[df['A']=='foo']

# filter by multiple criteria
df[(df['A']=='foo') & (df['B']=='one') ] 

# filter by complex criteria (example: only observations where the word in the second column starts with 't'): 
criterion = df['B'].map(lambda x: x.startswith('t')) # first approach: using the map method
df[criterion]

df[[x.startswith('t') for x in df['B']]] # second appraoch: using a list comprehension (slower)

```

**using where**
Boolean indexing returns a subset of the data: 
to guarantee that the output has the same shape as the original data, the [where()](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-where-method-and-masking) method can be used. This returns a true/false mask of the size of the original dataset.

**using isin**
