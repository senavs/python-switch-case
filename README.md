# Python - Switch Case Simulation (C Like)
Python implementation of `C` Switch Case clause

## How does it work?
Using python `context manager` and `if` blocks, we can simulate switch case by instantiating `Switch` class
and calling its method `__call__()`

## Using
Import `Switch` class from switch.py module
```python
from switch import Switch
```

Create the cases block inside `Switch` instance context block
```python
variable = 10

with Switch(variable) as case:
    if case(0):
        print('case 0')
    elif case(*range(1, 6)):
        print('case 1, 2, 3, 4 and 5')
    elif case(6, 7, 8):
        print('case 6, 7, and 8')
    elif case(9, 10):
        print('case 9 and 10')
    else:
        print('default')

# >> case 9 and 10
```

## Suppressing exceptions
You can also handle exceptions that can occurs inside the switch block, without using `try/except`
```python
variable = 11
mylist = list(range(10))

with Switch(variable, suppress=IndexError) as case:
    if case(*range(10)):
        print(mylist[variable])  # the same as print(mylist[case.value])
    else:
        print(mylist[variable])
        print('Index out of the range')
```

Without the suppress argument, it will raise the exception
```python
variable = 11
mylist = list(range(10))

with Switch(variable) as case:
    if case(*range(10)):
        print(mylist[variable])  # the same as print(mylist[case.value])
    else:
        print(mylist[variable])
        print('Index out of the range')

# Traceback (most recent call last):
#   File "~/tests.py", line 10, in <module>
#     print(mylist[variable])
# IndexError: list index out of range
```