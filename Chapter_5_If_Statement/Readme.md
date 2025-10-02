# Chapter 5 If Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions.
Python's *if* statement allows you to examine the current state of a program and respond appropriately to that state.

## Simple Example 

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

```

## Conditional Test

At the heart of every *if* statement is an expression that can be evaluated
as ***True*** or ***False*** and is called a ***conditional test***. Python uses the values *True*
and *False* to decide whether the code in an *if* statement should be executed.


### Checking for Equality

Most conditional test compare the current value of a variable to a specific value of interest.
The simplest conditional test checks whether the value of a variable is *equal* toe the value of interest:

```bash
>>> car = 'bmw'
>>> car == 'bmw'
True
```


