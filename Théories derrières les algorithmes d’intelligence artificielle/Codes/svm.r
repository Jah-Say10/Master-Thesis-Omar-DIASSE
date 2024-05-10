print("Hello  R")

# select weights for the straight line
weight.w = matrix(c(2,3),nrow=1,ncol=2,byrow=TRUE)
print(weight.w)

# select intercept for the straight line
gamma.g = matrix(c(-10,-10),nrow=1,ncol=2,byrow=TRUE)
print(gamma.g)

# select points
point.x = matrix(c(5.5,1.5,4.5,-1.8),nrow=2,ncol=2,byrow=TRUE)
print(point.x)

# determine label error
hat.y = weight.w %*% t(point.x) + gamma.g
print(hat.y)

# assign class labels
label.s = matrix(c(1,-1),nrow=1,ncol=2,byrow=TRUE)
print(label.s)

# check for minimum error
print(label.s * hat.y)

# calculate SVM measure
print((weight.w %*% t(weight.w))/2)

# display the straight line and points
line.x1 = rep(0,10)
line.x2 = rep(0,10)

slope = weight.w[1]/weight.w[2]
intercept = gamma.g[1]/weight.w[2]
print(slope)
print(intercept)

for (i in 1:10)
{
    line.x1[i] = i
    line.x2[i] = -intercept - slope * line.x1[i]
}

plot(line.x1, line.x2, type="o", pch=20, ylim=c(-5,5))
points(point.x[1,1], point.x[1,2], col="red", pch=19)
points(point.x[2,1], point.x[2,2], col="blue", pch=19)
grid(15, 15, lwd=2)