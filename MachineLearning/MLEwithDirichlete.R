#first we will construct the MLE for Dirichlete distribution


#data section begins
#observed data is the dengue serotype proportions,
#where only three serotypes are assumes in a year for example
observed_data<-c(0.1,0.5,0.4)
#data section ends
alpha1<-c(0,0,0)
#the likelihood function for an observed data with three variables, x1,x2,x3 is given by
alpha<-c(2,3,4)
DirLik<-function(alpha,observed_data){
  nrm<-gamma(sum(alpha))
  lk<-prod(observed_data^alpha /gamma(alpha))/nrm
  return (lk)
}

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
dp<-0.01
lk<-matrix(0,nrow=5,ncol=5)
i1<-1
max1<- -10
pmax<-c(0,0,0)
for(p1 in seq(1,5,1)){
    j1<-1
    for(p2 in seq(1,5,1)){
        p3=11-p1-p2
    alpha=c(p1,p2,p3)

  lk[i1,j1]<-DirLik(alpha,observed_data)
  if(lk[i1,j1]>max1){
    max1<-lk[i1,j1]
    alpha1<-alpha
  }
  print(c(i1,j1,lk[i1,j1]))

  j1=j1+1
    }
  i1=i1+1
}
print(lk)
print("The most likely parameters that will produce the given data from a dirichlter distribution are")
print(c(alpha1,max1))
# plot(seq(0,1,0.01),lk,type='b',col='red')