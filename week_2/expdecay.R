require(deSolve)

state <- c(Y = 1)
parameters <- c(k = -1)

derivs <- function(t, state, parameters) {
  with(as.list(c(state, parameters)), {
    dY <- k * Y
    list(c(dY))
  })
}
t <- (1:100) / 10
out <- ode(state, t, derivs, parameters)
plot(out)
