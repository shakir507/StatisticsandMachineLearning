1+2
 1+2*3
x=6
total.revenue=18.4
expenses=x
 net.profit=total.revenue-expenses
net.profit
z=c(2,3,4,5,6)
mean(z)
var(z)
sd(z)
seq(from=1, to=10, by=1)

#builtin functions: eg. trees
trees #data on set of trees giving height diameter and volume of the tree

help(trees)#get help on what kind of data set is trees
attach(trees)#gets the names of colums
names(trees) #prints the names
hist(Girth)#get histogram of the column named 'Girth'.
plot(Girth,Height)#plot scatter plot girth vs height
pairs(trees) # plots pairwise scatter plot with three variables girth,height, volume 
summary(trees)#summarises the data with mean, median, range and quantiles, 
