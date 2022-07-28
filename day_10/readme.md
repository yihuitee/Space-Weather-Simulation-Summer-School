Final Project
=============

## Project A

Solve and plot the temperature using steady-state heat equation using the 
data and functions from `day_7` and `day_8`:

$$
\frac{\partial^2 T_i}{\partial z^2} = - \frac{Q_{EUV,i}}{4 \cdot 10^{-4}}
$$

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
\frac{\partial N_i}{\partial t} = Q_{EUV,i} - R \times M \times N_i
$$

Make an animation of the results and explain what is happening.
