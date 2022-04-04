---
parent: random notes 
title:  - Lambda expressions 
nav_order: Functions 
---

---
layout: default
title: Configuration
nav_order: 2
---

### Normal functions:



### Lambda expressions:

Lambdas are one line functions. They are also known as anonymous functions in some other languages. You might want to use lambdas when you don’t want to use a function twice in a program. They are just like normal functions and even behave like them. "Semantically, they are just syntactic sugar for a normal function definition." (copied from [here](https://book.pythontips.com/en/latest/lambdas.html))

The way a lambda function works is:
```python
lambda argument: manipulate(argument)
```
- before the ":"
	- write "lambda"
	- choose a name for the argument
- after the ":"
	- write what to do with the argument (i.e. the function). The Lambda function returns the result of this operation.


A standard use case for Lambda functions is in sorting: 
- Both [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort") and [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted") have a _key_ parameter to specify a function (or other callable) to be called on each list element prior to making comparisons. (see [here](https://docs.python.org/3/howto/sorting.html#key-functions))
- This allows for uses such as:
	```python
	pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	pairs.sort(key=lambda pair: pair[1])
	pair
	>>> [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
	```

References:
- [Python Manual](https://book.pythontips.com/en/latest/lambdas.html)
- [Python Tricks website](https://book.pythontips.com/en/latest/lambdas.html)