# Exponential Decay
require(deSolve)

# TIME Impact core model (no MDR TB, no post treatment compartments, no HIV, no age groups)

derivs = function(t, state, parms){
  with(as.list(c(state,parms)),{ 
    labda = beta*(I+c*N)/(S+L+I+N) 
    flowStoL =           (1-alpha)*labda*S
    flowStoI =    sigma *   labda *alpha*S
    flowStoN = (1-sigma)*   labda *alpha*S
    
    flowLtoI =    sigma*   (labda*alpha*(1-x)+nu)*L
    flowLtoN = (1-sigma)*  (labda*alpha*(1-x)+nu)*L
    
    flowItoL = (gamma*Sei*eta*tau+r)*I
    flowNtoL = (gamma*Sen*eta*tau*d+r)*N
    dS    = -(flowStoL +  flowStoI + flowStoN) +  omega*(S+L+I+N) - mu*S
    dL    =   flowStoL +  flowItoL + flowNtoL  - (flowLtoI + flowLtoN)  - mu*L
    dI    =   flowStoI +  flowLtoI - flowItoL  + theta*N - (mu+muI)*I 
    dN    =   flowStoN +  flowLtoN - flowNtoL  - theta*N - (mu+muN)*N 
    list(c(dS,dL,dI,dN))
  })
}
parms = c( 
  omega = 0.01594,
  mu    = 0.015,
  muI   = 0.20,
  muN   = 0.20,
  beta  = 14.75, 
  c     = 0.25, # rel_inf
  alpha = 0.031,
  x     = 0.65, # p
  nu    = 0.002, # v
  sigma = 0.4,
  gamma = 0, # 1.4,  #kneg 
  eta   = 0.83, # l_s
  tau   = 0.76, #tneg 
  r     = 0.25,
  Sei   = 0.82, # 2015
  Sen   = 0.57, # 2015
  theta = 0.02,
  d     = 0.8 # rel_d
)

# run to equilibrium (100 years)
state = c(S = 80000, L = 17000, I = 100, N = 200)
times = (0:1000)/10
result = as.data.frame(ode(y=state,times=times,func=derivs,parms=parms))
result$pop = apply(result[,2:5],1,sum) 
tail(result)

state = as.numeric(result[nrow(result),2:5])
names(state)=colnames(result)[2:5]
parms["gamma"] = 1.4
result.treatment = as.data.frame(ode(y=state,times=(0:300)/10,func=derivs,parms=parms))
result.treatment$pop = apply(result.treatment[,2:5],1,sum) 
# result$A   = apply(result[,4:5],1,sum)
tail(result.treatment)

