#this code implements muliple Linear Regression analysis from the Bayesian statistics:from concepts to data course
#height of children inches predicted from height of children

#heightdist=read.table('http://www.randomservices.org/random/data/Galton.txt',header=T)
heightdist1=read.table('~/gslprogrames/BaeysianDatatoAnalisisCoursera/Rcodes/Galton.txt',header=T)
attach(heightdist1)
names(heightdist1)
#the height of children is more for taller paprents and less for shorter parents

heightdist1.lm=lm(Height~Father+Mother+Gender+Kids) #lm is the linear regression model with independent varial temperature and dependent variable Damage I
summary(heightdist1.lm)

# Call:
#   lm(formula = Height ~ Father + Mother + Gender + Kids)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -9.4748 -1.4500  0.0889  1.4716  9.1656 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 16.18771    2.79387   5.794 9.52e-09 ***
#   Father       0.39831    0.02957  13.472  < 2e-16 ***
#   Mother       0.32096    0.03126  10.269  < 2e-16 ***
#   GenderM      5.20995    0.14422  36.125  < 2e-16 ***
#   Kids        -0.04382    0.02718  -1.612    0.107    
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 2.152 on 893 degrees of freedom
# Multiple R-squared:  0.6407,	Adjusted R-squared:  0.6391 
# F-statistic: 398.1 on 4 and 893 DF,  p-value: < 2.2e-16

#Father, Mother, Gender have strong effects but number of kids in the family doesnot have much effect.
#so we remove Kids from the model
heightdist1.lm=lm(Height~Father+Mother+Gender)
summary(heightdist1.lm)

# Call:
#   lm(formula = Height ~ Father + Mother + Gender)
# 
# Residuals:
#   Min     1Q Median     3Q    Max 
# -9.523 -1.440  0.117  1.473  9.114 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 15.34476    2.74696   5.586 3.08e-08 ***
#   Father       0.40598    0.02921  13.900  < 2e-16 ***
#   Mother       0.32150    0.03128  10.277  < 2e-16 ***
#   GenderM      5.22595    0.14401  36.289  < 2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 2.154 on 894 degrees of freedom
# Multiple R-squared:  0.6397,	Adjusted R-squared:  0.6385 
# F-statistic:   529 on 3 and 894 DF,  p-value: < 2.2e-16

# R-squared value doesnt change much so we will keep the later model to predict height of the child as a funciton of father mother and gende of the child

#95% posterior interval for the difference in height by gender
5.226-.14401*qt(0.975,894)
5.226+.14401*qt(0.975,894)
lines(T,fitted(oring1.lm))

#note that these are same as frequentist confidence intervals



#posterior predictive interval (same as frequentist)

#if we are going to launch at 31 deg F, what is the 95% interval for what we might see in damage?
#use predict command to achieve thix objective

predict(heightdist1.lm,data.frame(Father=68, Mother=64,Gender="M"),interval="predict")
predict(heightdist1.lm,data.frame(Father=68, Mother=64,Gender="F"),interval="predict")

#equivalently
10.82052-2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))
10.82052+2.012*qt(0.975,21)*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))

#we an also calculate the posterior probability that the damage is greater zero if we launch at 31 deg F.
1-pt((0-10.82052)/(2.102*sqrt(1+1/23+((31-mean(T))^2/22/var(T)))),21)

#this give 