# numpy for fast arrays and some linear algebra.
import numpy as np 
# import matplotlib for plotting
import matplotlib.pyplot as plt
# import Dormand-Prince Butcher tableau
import dormand_prince as dp
# import our Runge-Kutta integrators
import runge_kutta as rk

# Please implement here:
#    S - numpy array carrying the stoichiometry matrix
#    k - numpy array carrying the rate coefficients k1 = 100, k2=0.25, k3=1
#    c_0 - initial composition, i.e., c_0(A) = 1, c_0(B)=c_0(C)=0.0

S = np.array([[-1,0,0],
              [1, -1, 1],
              [0, 2, -2]])
k = np.array([100.0,0.25,1.0])
c_0 = np.array([1.0,0.0,0.0])

def reaction_rates(c,k):
    """
        Function implementing the reaction rate computation of our toy reactor
        
        inputs:
            c - concentration of species A, B, C (numpy array)
            k - rate constants (organized as list)

        outputs:
            reaction rates (numpy array)
    """
    return k * [c[0],c[1],c[2]**2]

def reactor(c,t,k,S):
    """
        Function returing the rhs of our toy reactor model 
        
        inputs:
            c - concentration of species  (numpy array)
            t - time 
            k - rate constants (organized as list)
            S - stoichiometry matrix (numpy array)

        outputs: 
            dc/dt - numpy array
    """
    return S @ reaction_rates(c,k)


# time step 
h = 1e-3

########################################
### hereafter no more code modification necessary
########################################

# time horizon
tspan = (0.0,5.0)

# define dormant_prince_stepper
def dormant_prince_stepper(f,x,t,h):
    return rk.explicit_RK_stepper(f,x,t,h,dp.a,dp.b,dp.c)

trajectory, time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                       c_0, 
                                       tspan, 
                                       h,
                                       dormant_prince_stepper)

species_names = ["A", "B", "C"]
colors = ["red", "blue", "black"]

fig, axs = plt.subplots(2)
ax = axs[0]
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(time_points, [c[i] for c in trajectory],
            color=colors[i], 
            linewidth=2, 
            label = species_names[i])
ax.legend(loc="center right")
fig.savefig("concentration_traces.pdf")

tspan = (0.0,0.1)
trajectory, time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                       c_0, 
                                       tspan, 
                                       h,
                                       dormant_prince_stepper)

ax = axs[1] 
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(time_points, [c[i] for c in trajectory],
            color=colors[i], 
            linewidth=2, 
            label = species_names[i])
ax.legend()
fig.savefig("zoomed_concentration_traces.pdf")
