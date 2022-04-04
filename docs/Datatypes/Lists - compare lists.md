---
parent: Datatypes 
title: - compare lists 
nav_order: Lists 
---

check if a list contains an entry
``` python
fridge = ['tomatoes', 'lettuce', 'cucumber', 'yogurt']
print('cheese' in fridge)
# Output:
# False
print('tomatoes' in fridge)
# Output:
# True
```

check if list A contains all the items of another list, B.
An easy way is to use sets, and check whether B is a subset of A
``` python
fridge = ['tomatoes', 'lettuce', 'cucumber', 'yogurt']
needed_for_dinner = ['tomatoes', 'cheese']

print(set(needed_for_dinner).issubset(set(fridge)))
# Output:
# False
```

To check which items of the list B are missing in list A, look at the difference between sets:
``` python
fridge = ['tomatoes', 'lettuce', 'cucumber', 'yogurt']
needed_for_dinner = ['tomatoes', 'cheese', 'eggs']

need_to_buy = set(needed_for_dinner)-set(fridge)
print(need_to_buy)
# Output:
# {'eggs', 'cheese'}
```