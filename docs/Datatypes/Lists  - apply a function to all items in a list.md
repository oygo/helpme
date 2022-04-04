---
parent: Datatypes 
title:  - apply a function to all items in a list 
navorder: Lists 
---

In order to apply a function to all elements in a list, use a list comprehension.  

Example: 
- I have a list; each element in the list is a messy name
- I would like to fix each element of the list, by applying the function capitalize() to it; this capitalizes the first character of the string and makes all the other characters lowercase.

```python
list = ['NIKLAS', 'PAul', 'tom', 'johN']
list_clean = [name.capitalize() for name in list]
print(list_clean)
# Output:
# ['Niklas', 'Paul', 'Tom', 'John']
```