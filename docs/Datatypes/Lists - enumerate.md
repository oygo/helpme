---
parent: Datatypes 
title: - enumerate 
navorder: Lists 
---

#python

Enumerate lists:

When going through a list, keep track of/use both the list elements and their position:

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print counter, value

# Output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear
```


Enumerate also accepts an optional argument that allows us to specify the starting index of the counter.

	
https://book.pythontips.com/en/latest/enumerate.html