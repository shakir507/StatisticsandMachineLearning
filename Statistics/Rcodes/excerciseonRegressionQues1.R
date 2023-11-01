#this code implements muliple Linear Regression analysis from the Bayesian statistics:from concepts to data course
# The first column reports each player's average driving distance in yards. 
#The second column reports the percentage of the player's drives that finish in the fairway, measuring their accuracy. 
#The third and final column has a 1 to denote a female golfer (on the LPGA tour), and a 2 to denote male golfer (on the PGA tour).

#golfdistance=read.table('http://users.stat.ufl.edu/~winner/data/pgalpga2008.dat',header=T)
golfdistance=read.table('~/gslprogrames/BaeysianDatatoAnalisisCoursera/Rcodes/pgalpga2008.dat',header=T)
datF <- subset(golfdistance, X1==1, select=1:2)
attach(datF)
names(datF)
#the height of children is more for taller paprents and less for shorter parents
datF.lm=lm(X67.0~X243.2) #lm is the linear regression model with independent varial temperature and dependent variable Damage I
summary(datF.lm)

# Call:
#   lm(formula = X67.0 ~ X243.2)
# 
# Residuals:
#   Min       1Q   Median       3Q      Max 
# -22.0495  -3.2083   0.3039   3.4218  15.5168 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 102.88523    3.33020   30.89   <2e-16 ***
#   X243.2       -0.13966    0.01231  -11.34   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 5.124 on 351 degrees of freedom
# Multiple R-squared:  0.2683,	Adjusted R-squared:  0.2662 
# F-statistic: 128.7 on 1 and 351 DF,  p-value: < 2.2e-16

#The posterior mean for intercept is 102.88523

yhat1=coef(datF.lm)[1]+coef(datF.lm)[2]*260

lines(T,fitted(oring1.lm))

#note that these are same as frequentist confidence intervals



#posterior predictive interval (same as frequentist)

#if we are going to launch at 31 deg F, what is the 95% interval for what we might see in damage?
#use predict command to achieve thix objective
predict(datF.lm,data.frame(X243.2=260),interval="predict")  


#equivalently
10.82052-2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))
10.82052+2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))

#we an also calculate the posterior probability that the damage is greater zero if we launch at 31 deg F.
1-pt((0-10.82052)/(2.102*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))),21)

#this give 
