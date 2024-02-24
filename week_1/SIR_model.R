library("deSolve")

# time unit : days
parameters <- c(b =  0.1, # 10% probability of transmission per contact
                c =  5,   #  5  (close) contacts per day
                d =  5)   #  5 days infectious


state <- c(S = 1000,
           I = 1,
           R = 0)


SIR<-function(t, state, parameters) {
  with(as.list(c(state, parameters)),{
    # rate of change
     N = S+I+R
    dS = -b*c*I/N*S
    dI =  b*c*I/N*S - I/d
    dR =  I/d
    # return the rate of change
    list(c(dS, dI, dR))
  })   # end with(as.list ...
}

times = seq(0,60,0.02)
out   = as.data.frame(ode(y = state, times = times, func = SIR, parms = parameters))
class(out)
plot(x=times, y=out$S, type="l",col="blue",ylim=c(0,1000),ylab="S, I or R",xlab="time in days")
lines(x=times, y=out$I, type="l",col="red",ylim=c(0,1000))
lines(x=times, y=out$R, type="l",col="darkgreen",ylim=c(0,1000))


