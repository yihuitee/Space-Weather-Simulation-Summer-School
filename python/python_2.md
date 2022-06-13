---
title: Space 477: Python: II
description: First Python lecture
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Qusai Al Shidi | qusai@umich.edu | CSRB 2118

# Space 477: Python: II

----------

# One more basic type!

----------

## Dictionaries

- A dictionary is an *iterable* with conjoining *keys* and *values* as the elements (*items*).
- Useful to encapsulate data.

```python
solar_system = {'planets': ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                            'Saturn', 'Uranus', 'Neptune'),
                'star': 'Sol',
                'dwarf_planets': ('Pluto', )
               }

solar_system['dwarf_planets']  # ('Pluto')
planets = [planet for planet in solar_system['planets']]
# or
planets = list(solar_system['planets'])
print(sorted(planets))  # Alphabet sort
```

----------

# numpy

----------

- With `numpy` you can make arrays and do vector arithmetic.
- This is faster than making `for` loops and adding.
    - *Python is not C.* 🐍
- `numpy` is optimized for math operations.
- `numpy` is well [documented](https://numpy.org/).
    - In the face of ambiguity, refuse the temptation to guess. 🧘
```python
import numpy as np  # convention use np

vec = np.linspace(start=0, stop=1, num=3)  # evenly spaced numbers
vec*vec  # element-wise multiplication
vec*vec == vec**2  # array([True, True, True])
mat = np.matrix([[1, 2],
                 [3, 4]])
mat*mat == mat**2
mat.transpose()  # Very useful
```

----------

## element access

```python
my_list = [1, 2, 3, 4, 5]
my_list[1]  # 2
my_array = np.array(my_list)
my_array[1:3]  # array([2, 3])
my_list[1:3]  # [2, 3]
my_array[:3]  # array([1, 2, 3])
my_array[3:]  # array([4, 5])
my_array[:-1]  # array([1, 2, 3, 4])
```

----------

# matplotlib

----------

- Most popular Python plotting library.
- Very good [documentation](https://matplotlib.org/).

Let's plot $f(x) = e^x , 0 \le x < 1$.

```python
import matplotlib.pyplot as plt  # here is the good stuff

x = np.linspace(0, 1)  # default num is 50
plt.plot(x, np.exp(x))
plt.xlabel(r'$0 \le x < 1$')
plt.ylabel(r'$e^x$')
plt.title('Exponential function')
plt.show()  # shows plot, can be saved
```

----------

# real world example

----------

## What was the SYM/H (Dst) like on your birthday?

- Go to [NASA OMNIWeb](https://omniweb.gsfc.nasa.gov/).
- Download high resolution SYM/H data for the day of your birthday.
- Use `np.genfromtxt()` to read that data.
- Create a new folder for your plotting code. `birthday_storm.py`
    - Now is better than never. 🧘
- Plot that data.

----------

# 😯😯😯 __SURPRISE__ 😯😯😯. Revise each others code.

----------

- Is it *readable*?
    - Explicit is better than implicit. 🧘
    - Readability counts. 🧘
- Are there comments explaining code?
    - Now is better than never. 🧘
- Did you make sure to label the axes?
    - The reviewer is coming for you. 😱

----------

# okay we need a better time axis

----------

```
from datetime import timedelta

birth_day = (1990, 10, 2)
omni_format = ('year', 'doy', 'hour', 'min', 'sym_h')  # from the format file
data = np.genfromtxt('im_not_old.lst', names=omni_format)
plt.plot(data['sym_h'])
plt.xlabel('Minute of the day')
plt.ylabel('SYM/H [nT]')
plt.title('SYM/H on ' + str(birth_day))
```

------------

Let's find the cross polar cap potential (CPCP) on your birthday using
[Ridley & Kihn (2004)](http://dx.doi.org/10.1029/2003GL019113).

$$
\Phi = 29.28 - 3.31 sin(T+1.49) + 17.81 PCI
$$

- Make a function that takes the PCI as input and CPCP as output.
- Plot the function.
- To get you started, normalize to *day of year* as opposed to *month*.
