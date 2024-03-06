require("deSolve")

# time unit : days
parameters <- c(
  b = 0.1, # 10% probability of transmission per contact
  c = 2.5, #  5  (close) contacts per day
  d = 5
) #  5 days infectious

# R0 = b * c * d

with(as.list(c(parameters)), {
  b * c * d
})

state <- c(
  S = 1000,
  I = 1,
  R = 0
)

SIR <- function(t, state, parameters) {
  with(as.list(c(state, parameters)), {
    # rate of change
    N <- S + I + R
    flowStoI <- b * c * I / N * S
    flowItoR <- I / d
    dS <- -flowStoI
    dI <- flowStoI - flowItoR
    dR <- flowItoR
    # return the rate of change
    list(c(dS, dI, dR))
  }) # end with(as.list ...
}

times <- seq(0, 360, 0.02)
out <- as.data.frame(ode(y = state, times = times, func = SIR, parms = parameters))

plot(x = times, y = out$S, type = "l", lwd = 2, col = "blue", ylim = c(0, 1000), ylab = "S, I or R", xlab = "time in days")
lines(x = times, y = out$I, type = "l", lwd = 2, col = "red", ylim = c(0, 1000))
lines(x = times, y = out$R, type = "l", lwd = 2, col = "darkgreen", ylim = c(0, 1000))

? plot
