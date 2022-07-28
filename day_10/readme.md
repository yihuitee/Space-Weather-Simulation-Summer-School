Final Project
=============

## Project A

Solve and plot the temperature using steady-state heat equation using the 
data and functions from `day_7` and `day_8`:

$$
\frac{\partial^2 T_i}{\partial z^2} = - \frac{Q_{EUV,i}}{4 \cdot 10^{-4}}
$$

The boundary conditions should be $\partial T / \partial z = 0$ at the top and
$T=200$ K in the bottom.

## Project B

Using RK4 solve the below question for 24 hours:

$$
\frac{\partial T_i}{\partial t} = \frac{Q_{EUV,i}}{1500 \cdot \rho_i}
$$

Start with a 5 min time step. If you have time, make an animation and explain
what is seen.

## Project C

Solve the chemistry equation using an implicit method

$$
\frac{\partial N_i}{\partial t} + \frac{V \cdot N_i}{z} = Q_{EUV,i} - R \times M \times N_i
$$

Where N is the number density, V=-10m/s, R is the reaction rate, M is the
density of species it is reacting with. Make an animation of the results and 
explain what is happening.
