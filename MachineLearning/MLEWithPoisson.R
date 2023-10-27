#Using a poisson likelihood:


#data section begins

x1<-10#events are observed
#and the observation interval is unit time or space

#data section ends

#the likelihood function for an observed data, x1 in the unit interval is, is given by

PoisLik<-function(lam,x1){
  lk<-(lam^x1)*exp(-lam)/factorial(x1)
  return (lk)
}

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
dp<-0.1
lk<-array(0,integer(100/dp))
i=1
max1<- -10
lmax<-0
for(lam in seq(0,100,0.1)){
  lk[i]<-PoisLik(lam,x1)
  if(lk[i]>max1){
    max1<-lk[i]
    lmax<-lam
  }
  i=i+1
}
print(c(lmax,max1))
dlam<-seq(0,100,dp)
plot(dlam,lk,type='b',col='red')

#calculating where the maximum is reached can be tricky:
