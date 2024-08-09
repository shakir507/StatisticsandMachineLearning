#SIMULATING from a heirarchical model

#simulate a binomial trial with sucess probability phi

#1 simulate phi_i from Beta(2,2) prior
#2 simulate y_i from Binom(10,phi_i) from binomial distribution with 10 trials and sucess probability phi_i

m=1e5
print(m)
y=numeric(m)
phi=numeric(m)

for (i in 1:m){
  phi[i]=rbeta(1,shape1 = 2,shape2 = 2)
  y[i]=rbinom(1,size=10,prob = phi[i])
}

#same simulation from vectorised code


phi=rbeta(m,shape1 = 2,shape2 = 2)
y=rbinom(m,size = 10,prob = phi)

#marginal distribution for y can be done with just condireing the y distribution

table(y)#how often each values of y are drawn
table(y)/m#approximation of the probabilities
plot(table(y)/m)#marginal distribution of y

mean(y)#mean of marginalised distribution
