#Using a poisson likelihood:


#data section begins

x1<-10#Wait time until the event of interest occurs

#data section ends

#the likelihood function for an observed data, x1 in the unit interval is, is given by

ExpLik<-function(lam,x1){
  lk<-lam*exp(-lam*x1)
  return (lk)
}

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
dp<-0.01
lk<-array(0,integer(1/dp))
i=1
max1<- -10
lmax<-0
for(lam in seq(0,1,0.01)){
  lk[i]<-ExpLik(lam,x1)
  if(lk[i]>max1){
    max1<-lk[i]
    lmax<-lam
  }
  i=i+1
}
print(c(lmax,max1))
dlam<-seq(0,1,dp)
plot(dlam,lk,type='b',col='red')

#calculating where the maximum is reached can be tricky:
