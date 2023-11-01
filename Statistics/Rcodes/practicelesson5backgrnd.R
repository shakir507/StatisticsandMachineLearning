#Q1 Let X~Pois(3) Find P(X=1)
#Slution involves geetting PDF at 1
dpois(1,3)
#Ans from running above 0.149 

#Q2 X~Pois(3) Find P(X<=1) X~Pois(rate) so rate=3

#Solution involves calculating CDF at 1

ppois(1,3)

#Ans is 0.199

#Q3 Find P(X>1)

#solution involves getting CDF for P(X>1)=1-P(X<=1)=1-0.199=0.801

#Q4 Let Y~Gamma(2,1/3). Find P(0.5<Y<1.5)=CDF(1.5)-CDF(0.5). Here shape=2 and rate=1/3. Y~Gamma(shape,rate)

pgamma(1.5,2,1/3.0)-pgamma(0.5,2,1/3.0)

#Ans=0.078