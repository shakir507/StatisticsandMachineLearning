set.seed(32)#initialize random number genarator. To get different random number change the integer argument
#generate gamma distribution for theta with parameters a=2 b=1/3. This gamma dist could represent a posterior dist for posson dist.

m=100
a=2.0#shape param for gamma
b=1/3.0#rate param for gamma
theta=rgamma(m,a,b)
#plot histogram for the theta parameter

hist(theta,freq = FALSE)#freq=False gives probabiliy intsed of counts
#to compare this with theoretical prob dnsity function we plot the curve for densit of the gamma, dgamma

curve(dgamma(x,a,b),col='blue',add=TRUE)#add=true is for plotting on the same plot,x is generic and needs to be given for all distributions
#now use simulated values to caclucate monte carlo estimate of expected values of theta. to do this we take average

sum(theta)/m
mean(theta)

#how does this compare to true value of expected value? for gamma this number is a/b=2*3=6
#which shows that our approximation is close but not true. so we increase m
m=10000
theta=rgamma(n=m,shape=a,rate=b)

mean(theta)

#6.02, much closer to actual value. What about variance? we get it by using var

var(theta)
#we get 18.04318. true value is a/b^2

a/b^2=18
#so our monte carlo approximation is actually quite close

#how many theta values are less than 5?
ind=theta<5.0

head(ind)

#[1] FALSE FALSE  TRUE  TRUE FALSE FALSE
mean(ind)#calcuates the probability of theta less than 5

#[1] 0.497

#true value of this probabiityl is evaluated with pgamma(0.5,a,b)

pgamma(q=5.0,shape=a,rate=b)

#[1] 0.4963317, again very close to the monte carlo value

#what if we are interested in 90th percenticle?

quantile(theta,prob=0.9)

#[1] 11.74338 

#actual true quantile value is obtained by qgamma(0.9,a,b)

qgamma(0.9,a,b)

#[1] 11.66916

#again the monte carlo estimation and theoretical values are close
#