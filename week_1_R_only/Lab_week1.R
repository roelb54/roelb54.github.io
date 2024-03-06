### vectors, data, matrices, subsetting
x <- c(2, 7, 5) # c for combine
print(x)

y <- seq(from = 4, length = 3, by = 3)
# help on seq function
?seq
y
# operations on vectors apply to all elements of a vector
x + y
x / y
x^y
# selecting elements from a vector NOTE: first element is 1 (not 0 as in C, Python, ...)
x[2]
x[2:3] # elements 2 thru 3 (not as in Python - excluding 3)
x[-2] # all elements except 3rd
x[-c(1, 2)] # all elements except 1 and 2

# matrices
z <- matrix(seq(1, 12), 4, 3)
z
# or with argument names (which is better :-)
z <- matrix(data = 1:12, nrow = 4, ncol = 3) # NOTE matrix is filled by column by default
z
z[3:4, 2:3]
z[, 2:3]
z[, 1] # z[,1] is a vector corresponding to a matrix column
class(z[, 1])
# in this case an integer vector
z[, 1, drop = FALSE]
class(z[, 1, drop = F])
# now z[,1,drop=F] still is a matrix
dim(z)
ls()
rm(y)
ls()

### Generating random data, graphics
x <- runif(50) # random uniform
x <- runif(50, min = 0, max = 1) # random uniform
y <- rnorm(50) # random normal
y <- rnorm(50, mean = 0, sd = 1) # random normal

plot(x, y)
plot(x, y, xlab = "Random Uniform", ylab = "Random Normal", pch = "*", col = "blue")
par(mfrow = c(2, 1))
plot(x, y)
hist(y)
par(mfrow = c(1, 1))
? par

### Reading in data
Auto <- read.csv("Auto.csv")
dir()
names(Auto)
dim(Auto)
class(Auto)
summary(Auto)
str(Auto)
plot(Auto$cylinders, Auto$mpg)
plot(Auto$cyl, Auto$mpg)
attach(Auto)
search()
plot(cylinders, mpg)
cylinders <- as.factor(cylinders)
plot(cylinders, mpg, xlab = "Cylinders", ylab = "Mpg", col = "red")
pdf(file = "mpg.pdf")
plot(cylinders, mpg, xlab = "Cylinders", ylab = "Mpg", col = "red")
dev.off()
pairs(mpg ~ cylinders + acceleration + weight, Auto)
