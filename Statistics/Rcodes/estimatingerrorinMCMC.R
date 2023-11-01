#We can use central limit theoremt to approximate how accurate onte carlo estimates are
set.seed(32)
m=10000
a=2
b=1/3

theta=rgamma(m,a,b)

se=sd(theta)/sqrt(m)

#CI of 95 % of expected value of theta

CI1=mean(theta)-1.96*se
CI2=mean(theta)+1.96*se

#this shows that true mean is between these values

ind=theta<5

mean(ind)

pgamma(5,a,b)


se=sd(ind)/sqrt(m)#this number give how confident are we that the theta<5 in our monte carlo simulation, giving a error of 0.01. i.e a 90% accuracy


