---
parent: Datatypes 
title: - split into different parts 
navorder: Strings 
---


split() split a string into several parts, using the specified separator, and returns a list with the parts
```python 
my_string = "FC Barcelona vs. Real Madrid"
teams = my_string.split(' vs. ')
print(teams)
# Output>
# ['FC Barcelona', 'Real Madrid']
```

when splitting a string further (=multiple times), this is useful:
```python 
my_string = "Niklas Heusch: Economist"
[name, job] = my_string.split(': ')
[first_name, last_name] = name.split(' ')
print(f'{first_name} is a {job}')
# Output
# Niklas is a Economist
```


more sophisticated way: use regular expressions
https://stackoverflow.com/questions/19017917/how-can-i-split-a-string-into-multiple-parts-in-python