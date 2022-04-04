---
parent: random notes 
title: - check multiple conditions 
navorder: Conditions 
---

Sometimes we want to check that multiple conditions hold 

```python
if a == 1 and b == 2 and test3 == True:
	# Do something.
```

But once these conditions get a little more complex, then these if statements can get very long. 


A nice way around this is to use the following structure: 

```python
a = 1
b = 2
c = True

rules = [a == 1,
         b == 2,
         c == True]

if all(rules):
    print("Success!")
```

This structure allows to also write relatively complex rule expressions easily.

References:
- https://stackoverflow.com/questions/36757965/how-to-have-multiple-conditions-for-one-if-statement-in-python/50656647#50656647
- https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/
- Advent of Code 2020, Day 4b: https://adventofcode.com/2020/day/4