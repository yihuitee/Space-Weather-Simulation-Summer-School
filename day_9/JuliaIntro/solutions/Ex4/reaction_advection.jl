using DifferentialEquations, SparseArrays, CairoMakie

Nx = 100
x_range = range(0, 1, length= Nx) 
global ∇ = spzeros(Nx, Nx)
dx = step(x_range)
global b = spzeros(Nx); b[1] = -1/dx
∇[1,1] = 1/dx
for i in 2:Nx
    ∇[i, i-1] = -1/dx 
    ∇[i,i] = 1/dx 
end

#######
## A + B -> C
## C -> D
#######
k = [1.0, 10.0]

S = [-1 0
     -1 0
     1 -1
     0 1]

function rates(c,p,t)
    k, S = p
    r = k .* [c[1]*c[2],c[3]]
    return S*r
end


function advection_reaction(c,p,t)
    S, k, c0 = p
    Nx, Ns = size(c) 
    chemistry = zeros(Nx, size(c,2))
    for i in 1:Nx
        r = rates(c[i,:], (k,S), t)
        chemistry[i, :] .= r
    end
    return -(∇*c + b*c0') + chemistry
end

c0 = [1.0, 2.0, 0, 0]

c0_mat = zeros(Nx, 4)

prob = ODEProblem(advection_reaction, c0_mat, (0.0, 1.0), (S, k, c0))
sol = solve(prob, saveat=0.01)

fig = Figure()
ax = Axis(fig[1,1])
ylims!(ax, 0, 2)
A = Observable(sol.u[1][:,1])
B = Observable(sol.u[1][:,2])
C = Observable(sol.u[1][:,3])
D = Observable(sol.u[1][:,4])
lines!(ax, x_range, A, color = :red, label = "A")
lines!(ax, x_range, B, color = :blue, label = "B")
lines!(ax, x_range, C, color = :green, label = "C")
lines!(ax, x_range, D, color = :orange, label = "D")
axislegend(ax)
record(fig, "reaction_advection.mp4", enumerate(sol.u); framerate = 24) do (i,u)
    A[] = u[:,1]
    B[] = u[:,2]
    C[] = u[:,3]
    D[] = u[:,4]
end


using DifferentialEquations, SparseArrays, CairoMakie

Nx = 100
x_range = range(0, 1, length= Nx) 
global ∇ = spzeros(Nx, Nx)
dx = step(x_range)
global b = spzeros(Nx); b[1] = -1/dx
∇[1,1] = 1/dx
for i in 2:Nx
    ∇[i, i-1] = -1/dx 
    ∇[i,i] = 1/dx 
end

#######
## A -> 2A
## 2A -> A
#######
Nx = 100
x_range = range(0, 1, length= Nx) 
global ∇ = zeros(Nx, Nx)
dx = step(x_range)
global b = zeros(Nx)
b[1] = -1/dx
∇[1,1] = 1/dx
for i in 2:Nx
    ∇[i, i-1] = -1/dx 
    ∇[i,i] = 1/dx 
end

k = [0.1, 0.1]

S = [1 -1]

function rates(c,p,t)
    k, S = p
    r = k .* [c[1],c[1]^2]
    return S*r
end


function advection_reaction(c,p,t)
    S, k, c0 = p
    Nx, Ns = size(c) 
    chemistry = zeros(Nx, size(c,2))
    for i in 1:Nx
        r = rates(c[i,:], (k,S), t)
        chemistry[i, :] .= r
    end
    return -(∇*c + b*c0') + chemistry
end

c0 = [1.0]

c0_mat = zeros(Nx, 1)

prob = ODEProblem(advection_reaction, c0_mat, (0.0, 1.0), (S, k, c0))
sol = solve(prob, saveat=0.01)



fig = Figure()
ax = Axis(fig[1,1])
ylims!(ax, 0, 2)
A = Observable(sol.u[1][:,1])
lines!(ax, x_range, A, color = :red)
record(fig, "aut_catalytic_reaction_advection.mp4", enumerate(sol.u); framerate = 24) do (i,u)
    A[] = u[:,1]
end