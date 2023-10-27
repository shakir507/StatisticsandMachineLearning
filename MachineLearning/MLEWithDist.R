#first we will construct the MLE for binomial/Bernoulli distribution


#data section begins
n<-20
x1<-4
#data section ends

#the likelihood function for an observed data, x1 in n trails, is given by

BinLik<-function(p,x1,n){
  lk<-choose(n,x1)*(p^x1)*((1-p)^(n-x1))
  return (lk)
}

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
dp<-0.05
lk<-array(0,integer(1/dp))
i=1
max1<- -10
pmax<-0
for(p in seq(0,1,0.05)){
  lk[i]<-BinLik(p,x1,n)
  if(lk[i]>max1){
    max1<-lk[i]
    pmax<-p
  }
  i=i+1
}
print(c(pmax,max1))
plot(seq(0,1,0.05),lk,type='b',col='red')