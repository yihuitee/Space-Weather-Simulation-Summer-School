#!/usr/bin/env python
"""
Solution of a 1D Convection-Diffusion equation: -nu*u_xx + c*u_x = f
Domain: [0,1]
BC: u(0) = u(1) = 0
with f = 1

Analytical solution: (1/c)*(x-((1-exp(c*x/nu))/(1-exp(c/nu))))

Finite differences (FD) discretization:
    - Second-order cntered differences advection scheme

"""
__author__ = 'Jordi Vila-Pérez'
__email__ = 'jvilap@mit.edu'


import numpy as np
import matplotlib.pyplot as plt
from math import pi
%matplotlib qt
plt.close()
import matplotlib.animation as animation

"Flow parameters"
nu = 0.01
c = 2

"Number of points"

N = np.array([32, 64, 96, 128])
error_ar=np.array([])

for n_element in N:
    Dx = 1/n_element
    x = np.linspace(0,1,n_element+1)
    
    "System matrix and RHS term"
    "Diffusion term"
    Diff = nu*(1/Dx**2)*(2*np.diag(np.ones(n_element-1)) - np.diag(np.ones(n_element-2),-1) - np.diag(np.ones(n_element-2),1))
    "Advection term: centered differences"
    Advp = -0.5*c*np.diag(np.ones(n_element-2),-1)
    Advm = -0.5*c*np.diag(np.ones(n_element-2),1)
    Adv = (1/Dx)*(Advp-Advm)
    A = Diff + Adv
    "Source term"
    F = np.ones(n_element-1)
    
    
    "Solution of the linear system AU=F"
    U = np.linalg.solve(A,F)
    u = np.concatenate(([0],U,[0]))
    ua = (1/c)*(x-((1-np.exp(c*x/nu))/(1-np.exp(c/nu))))
    
    plt.plot(x,ua,'-r',linewidth=2,label='$u_a$')
    plt.plot(x,u,'+',linewidth=2,label='$\widehat{u}$')
    plt.legend(fontsize=12,loc='upper left')
    plt.grid()
    plt.axis([0, 1,0, 2/c])
    plt.xlabel("x",fontsize=16)
    plt.ylabel("u",fontsize=16)
    
    
    "Compute error"
    error = np.max(np.abs(u-ua))
    error_ar = np.append (error_ar,error)
    print("Linf error u: %g\n" % error)
    
    "Peclet number"
    P = np.abs(c*Dx/nu)
    print("Pe number Pe=%g\n" % P);


convergence1=error_ar[1]/error_ar[0]
convergence2=error_ar[2]/error_ar[1]
print("convergence1 : %g\n" % convergence1)
print("convergence2 : %g\n" % convergence2)
