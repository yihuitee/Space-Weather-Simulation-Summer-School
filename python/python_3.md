---
title: Space 477: Python: III
description: First Python lecture
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Qusai Al Shidi | qusai@umich.edu | CSRB 2118

# Space 477: Python: III

----------

# Time to get comfortable with the terminal

----------

Let's use Python's package manager `pip`.

```bash
$ conda install pip
$ pip install swmfpy
# if it doesn't work try
$ pip install --user swmfpy
```

----------

- Plot your birthday AL using data from `swmfpy.web.get_omni_data()`

Do the following in `IPython`:
```python
from datetime import datetime
from swmfpy.web import get_omni_data

start_time = datetime(1990, 10, 2)
end_time = datetime(1990, 10, 3)
data = get_omni_data(start_time, end_time)  # returns a dictionary
data.keys()
```

----------

# Now for something more relevant

----------

- Many of you will need a way to calculate, specifically,
    *Schmidt semi-normalized Legendre polynomials* $P_l^m$.
- `numpy` includes regular Legendre polynomials.

```bash
$ pip install pyshtools
```

```python
from pyshtools.legendre import legendre_lm
legendre_lm(l=0, m=0, z=0, 'schmidt')
```

-----------

# More terminal things

In your anaconda project directory, create a new directory for a project.

```bash
$ mkdir 3d_plot
$ cd 3d_plot
3dplot/$ touch 3d_plot.py
```

-----------

- Good code has good metadata and documentation.
    - Now is better than never 🧘. 

Using your favorite text editor
```python
"""A 3D plot script for spherical coordinates.
"""
__author__ = 'Haskell Curry'
__email__ = 'i_died_too_old_for_email@mathlovers.com'
```

-----------

# Make a function that converts spherical coordinates to cartesian.

$$
x = r \cdot \sin(\phi) \cdot \cos(\theta)
$$
$$
y = r \cdot \sin(\phi) \cdot \sin(\theta)
$$
$$
z = r \cdot \cos(\phi)
$$

----------

# 😯😯😯 __SURPRISE__ 😯😯😯. Revise each other's code. Are you still getting surprised?

----------

```python
def spherical_cartesian(radius, azimuth, zentith):
    """Convert spherical coordinates to cartesian"""
    x = radius*sin(zentith)*cos(azimuth)
    y = radius*sin(zentith)*sin(azimuth)
    z = radius*cos(zentith)
    return x, y, z

fig = plt.figure()  # better control
axes = fig.gca(projection='3d')  # make 3d axes
r = np.linspace(0, 1)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
x, y, z = spherical_cartesian(r, theta, phi)
axes.plot(x, y, z)
```

-----------

For your project most of you will be asked to solve equations like this.

$$
B(r, \theta, \phi) = \sum \sum a_n^m P_n^m (\cos \theta)
$$

----------

# Have you started your project? Any coding questions at all?
