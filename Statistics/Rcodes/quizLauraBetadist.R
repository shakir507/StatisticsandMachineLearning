# Laura keeps record of her loan applications and performs a Bayesian analysis of her success rate \thetaθ. Her analysis yields a \text{Beta}(5,3)Beta(5,3) posterior distribution for \thetaθ.
# 
# The posterior mean for \thetaθ is equal to \frac{5}{5+3} = 0.625. However, Laura likes to think in terms of the odds of succeeding, defined as \frac{\theta}{1 - \theta} 
# 	
# , the probability of success divided by the probability of failure.
# 
# Use R to simulate a large number of samples (more than 10,000) from the posterior distribution for \thetaθ and use these samples to approximate the posterior mean for Laura's odds of success ( \text{E}(\frac{\theta}{1-\theta})
set.seed(32)
m=10000
a=5
b=3
thetaL=rbeta(m,shape1 = a,shape2 = b)
ods=thetaL/(1-thetaL)
mean(ods)
mean(thetaL)

# 
# Laura also wants to know the posterior probability that her odds of success on loan applications is greater than 1.0 (in other words, better than 50:50 odds).
# 
# Use your Monte Carlo sample from the distribution of \thetaθ to approximate the probability that \frac{\theta}{1-\theta} 
# 
# is greater than 1.0.
# 
# Report your answer to at least two decimal places.

odsgt1=ods>1

mean(odsgt1)
sum(odsgt1)/m


# Use a (large) Monte Carlo sample to approximate the 0.3 quantile of the standard normal distribution (\text{N}(0,1)N(0,1)), the number such that the probability of being less than it is 0.3.
# 
# Use the \tt quantilequantile function in R. You can of course check your answer using the \tt qnormqnorm function.
# 
# Report your answer to at least two decimal places.
m=100000
nrm1=rnorm(m,0,1)

quantile(nrm1,0.3)

qnorm(0.3,0,1)
