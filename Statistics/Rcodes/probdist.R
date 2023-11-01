x=0#is the mean.
q=-0.674#is the value of x where we expect a 25 quantile
p=0.25 #is the 25th quantile, where qnorm will return the value close to q above
n=10000 # we choose to get 10000 random numbers from normal distribution.

dnorm(x,mean,sd)#evaluates PDF at x with mean=mu and sd=sigma i.e evaluates the PDF at x
pnorm(q,mean,sd)#evaluate CDF at q i.e it wil calcuate what percentile is at q
qnorm(p,mean,sd)#evaluate quantile function at p i.e. evaluates what value is at percentile p
rnorm(n,mean,sd)#Generate n pseudo-random samples from the normal distribution


#similarly we can get PDF,CDF, quantiles for other distribtions

#Binomial

dbinom(x,size =10 ,prob = 0.4)

#Poisson
dpois(x,lambda,log=FALSE)

#Exponential
dexp(x,rate,log=FALSE)

#Gamma
dgamma(x,shape,rate)

#Uniform

dunif(x,min,max)

#Beta

dbeta(x,shape1,shape2)

#t_nu

dt(x,df)

a=c(0.1,0.9)
qexp(p=a,rate=1)
