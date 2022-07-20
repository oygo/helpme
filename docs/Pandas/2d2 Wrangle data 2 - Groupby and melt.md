---
parent: Pandas 
title: Wrangle data 2 - Groupby and melt 
nav_order: 2d2 
---

# Wrangle 2: Reshape (group, melt, etc.)

{: .no_toc } 
<details open markdown="block"> 
  <summary> 
    Table of contents 
  </summary> 
  {: .text-delta } 
1. TOC 
{:toc} 
</details>] 

## Groupby
see [here](https://dfrieds.com/data-analysis/groupby-python-pandas.html) for a nice writeup

```python
import pandas as pd
import seaborn as sns

df_tips = sns.load_dataset('tips')
df_tips # dataset of restaurant visits, indicating bill and tip for each visit and some other characteristics


# group by one/several variable(s)
df_tips.groupby(by='sex').size() # group by sex, then display the size (= number of observations) in each group (i.e. number of)
df_tips.groupby(by=['sex','time']).size() # can also group by several variables


# summary statistics
df_tips.groupby(by='sex')['total_bill'].mean() # group by sex, then - for the variable total_bill - display the mean for each group
df_tips.groupby(by='sex')['total_bill'].describe() # group by sex, then - for the variable total_bill - describe the variable
```
Summary statistics that can be calculated:
- sum(), mean(), count(), size(), var(), std(), sem()
- median(), first(), last(), nth(), min(), max()
- describe()

```python
#  summary statistics II (now fancier): using 'agg'
df_tips.groupby(by='sex').agg({'total_bill': ['count', 'mean', 'sum']}) # get multiple summary statistics for a variable
df_tips.groupby(by='sex').agg({'total_bill': 'max', 'tip': 'min'}) # get multipe summary statistics for several variables
df_tips.groupby(by='sex').agg({'total_bill': lambda bill: bill.max() - bill.min()}).rename(columns={'total_bill': "range_total_bill"}) # use 'agg' with lambda functions to calculate your own summary statistics
```
for Lambda expressions see here: [[Functions  - Lambda expressions]]


```python
#  summary statistics III: using 'pipe' to calculate summary statistics from more than one column (i.e. as in the previous example, but now using both the columns 'bill' and 'tip')
df_tips.groupby(by=['sex', 'time', 'day']).pipe(lambda group: group.tip.sum()/group.total_bill.sum()*100) # 


# Turn the groupby into a new dataframe: use 'reset_index()'
df_agg = df_tips.groupby(by=['sex', 'time', 'day']).agg({'total_bill':['mean','sum'],'tip':['mean','sum']}).reset_index()
df_agg
```
the resulting dataframe here will hve a double 


## Melt


## Stack, unstack

## Pivot