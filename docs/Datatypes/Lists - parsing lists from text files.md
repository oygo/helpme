---
parent: Datatypes 
---

#python #lists #wrangling #loading

split_lines()
loads a textfile, in which each line is one entry. Then creates a list of lines.
```python 
f = open('inputs/day1.txt', 'r')  
lines = f.read().splitlines()
```

