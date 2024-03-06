A = matrix(0,6,3)
A[1,]=1:3
A[2,]=4:6
# does not work (as maybe naively expected):
A[3:6,]=A[1:2,]
# this works:
A[3:6,] = t(matrix(t(A)[,1:2],3,4))


df=data.frame(a=runif(20),b=runif(20),c=rep(c("kjsnbkasj","dasdas"),10))
str(df)
df$d = as.numeric(as.factor(df$c))
str(df)

