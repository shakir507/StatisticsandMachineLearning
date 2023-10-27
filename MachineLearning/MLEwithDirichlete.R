#first we will construct the MLE for Dirichlete distribution


#data section begins
n<-199*2
x<-c()
#data section ends

#the likelihood function for an observed data with three variables, x1,x2,x3 is given by

DirLik<-function(p,x,n){
  lk<-p[1]^x[1]*p[2]^x[2]*p[3]^x[3]
  return (lk)
}

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
dp<-0.01
lk<-array(0,integer(1/dp))
i=1
max1<- -10
pmax<-0
for(p in seq(0,1,0.01)){
    p=c(p1,p2,p3)

  lk[i]<-DirLik(p,x1,n)
  if(lk[i]>max1){
    max1<-lk[i]
    pmax<-p
  }
  i=i+1
}
print(c(pmax,max1))
plot(seq(0,1,0.01),lk,type='b',col='red')