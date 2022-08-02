import Base: +, -, *, ^, /, sin, cos, show

#################################
##### Defining our DualNumber type
#################################
struct DualNumber{Tval,Tgrad}
    val::Tval
    grad::Tgrad
end

#################################
##### product rule
#################################
function *(a::DualNumber, b::DualNumber)
    return DualNumber(a.val*b.val, b.val*a.grad + a.val*b.grad) # product rule
end

function *(a::Number, b::DualNumber)
    return DualNumber(a*b.val, a*b.grad) # complete
end

function *(a::DualNumber, b::Number)
    return b*a                          # complete
end

#################################
##### chain rule for powers
#################################
function ^(a::DualNumber, b::Number)
    return DualNumber(a.val^b, b*a.val^(b-1)*a.grad)
end

#################################
##### quotient rule 
#################################
function /(a::DualNumber, b::DualNumber)
    return DualNumber(a.val/b.val, a.grad/b.val - a.val*b.grad/b.val^2 )
end

function /(a::DualNumber, b::Number)
    return DualNumber(a.val/b, a.grad/b) 
end

#################################
##### addition
#################################
function +(a::DualNumber, b::DualNumber) 
    return DualNumber(a.val+b.val, a.grad + b.grad) # complete
end

function +(a::DualNumber, b::Number) 
    return DualNumber(a.val + b, a.grad) # complete
end

function +(a::Number, b::DualNumber)
    return b+a # complete
end

#################################
##### Chain Rule for sin/cos
#################################
function sin(a::DualNumber)
    return DualNumber(sin(a.val), cos(a.val)*a.grad)
end

function cos(a::DualNumber)
    return DualNumber(cos(a.val), -sin(a.val)*a.grad)
end

#################################
##### subtraction of dual numbers
#################################
function -(a::DualNumber)
    return DualNumber(-a.val, -a.grad) 
end

function -(a::DualNumber, b::T) where T <: Union{DualNumber, Number}
    return a + (-b)
end

function -(a::Number, b::DualNumber)
    return a + (-b)
end

#################################
##### We are suckers for neat printouts in the REPL!
#################################
show(io::IO, a::DualNumber) = println(io, "$(a.val) + $(a.grad)ϵ")