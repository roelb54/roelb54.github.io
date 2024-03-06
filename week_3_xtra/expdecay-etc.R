# Exponential Decay
require(deSolve)

# Simple
derivsfn = function(t, y, k){
    dy = -k * y
    list(c(dy))
}

k = 2
y = 1
# derivsfn(t=0,y,k)
ode(y=y,times=0:10,func=derivsfn,parms=k)

# More generic
state = c(y = 1)
parameters = c(k = -1)

derivsfn2 = function(t, state, parameters){
  with(as.list(c(state, parameters)),{
    dy = k * y
    list(c(dy))
  })
}
t = (1:100)/10
out = ode(state,t,derivsfn2,parameters)
plot(out)

# The more generic code also works with e.g. a 2 compartment system

derivsfn3 = function(t, state, parms){
  with(as.list(c(state,parms)),{
    dx = -p*x - q*(x-y)
    dy = q*(x-y)
    list(c(dx,dy))
  })
}
parms = c(p = 0.2, q=0.5)
state = c(x = 1, y = 0)
# derivsfn3(0,state,parms)
result = as.data.frame(ode(y=state,times=0:20,func=derivsfn3,parms=parms))
plot(result$t,result$x,type="b",col="blue")
lines(result$t,result$y,type="b",col="blue")
# plot(result$y,result$x,type="b",col="blue")
