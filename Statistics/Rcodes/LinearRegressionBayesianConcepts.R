#this code implements Linear Regression analysis from the Bayesian statistics:from concepts to data course

#oring=read.table('http://www.randomservices.org/random/data/Challenger2.txt',header=T)
oring1=read.table('~/gslprogrames/BaeysianDatatoAnalisisCoursera/Rcodes/Challenger2.txt',header=T)
attach(oring1)
plot(T,I)
oring1.lm=lm(I~T) #lm is the linear regression model with independent varial temperature and dependent variable Damage I
summary(oring1.lm)

# Call:
#   lm(formula = I ~ T)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -2.3025 -1.4507 -0.4928  0.7397  5.5337 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 18.36508    4.43859   4.138 0.000468 ***
#   T           -0.24337    0.06349  -3.833 0.000968 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 2.102 on 21 degrees of freedom
# Multiple R-squared:  0.4116,	Adjusted R-squared:  0.3836 
# F-statistic: 14.69 on 1 and 21 DF,  p-value: 0.0009677
#plotting lines through fitted data

lines(T,fitted(oring1.lm))

#Calculating 95% confidence interval for the fitted slope -0.24337 based on t-distribution with 21 degrees of freedom

CI1=-0.24337-0.06349*qt(0.975,21)
CI2=-0.24337+0.06349*qt(0.975,21)
#note that these are same as frequentist confidence intervals

#the challenger launch was at 31 degrees Fahrenheit. 
#How much damage do you predict to the orings?

#y-hat=intercept+slope*31
yhat=18.36508-0.24337*31

#this turns out to be 10.82061

yhat1=coef(oring1.lm)[1]+coef(oring1.lm)[2]*31


#posterior predictive interval (same as frequentist)

#if we are going to launch at 31 deg F, what is the 95% interval for what we might see in damage?
#use predict command to achieve thix objective

predict(oring1.lm,data.frame(T=31),interval="predict")

#equivalently
10.82052-2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))
10.82052+2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))

#we an also calculate the posterior probability that the damage is greater zero if we launch at 31 deg F.
1-pt((0-10.82052)/(2.102*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))),21)

#this give 