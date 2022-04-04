---
parent: Machine Learning 
title: index 
navorder: inde 
---



**Workflow 1:** from loading the data to a first random forest
- loading the data
- deal with categories, missing values, dates
	- turn the dataset entirely numerical
- run a first random forest
this is all in "Kaggle: Costa Rica 2"

Workflow 2:
- load data (run a first random forest)
- split into test and training datasets
- tune RF parameters (eyeballing, exhaustive grid search, random grid search)
- interpret the forest (1)
	- drawing trees
	- FEATURE IMPORTANCES (still missing)
	- interpret individual observations
this is all in "Kaggle: Health Insurance"