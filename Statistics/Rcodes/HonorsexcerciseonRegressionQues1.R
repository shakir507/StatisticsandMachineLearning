#this code implements muliple Linear Regression analysis from the Bayesian statistics:from concepts to data course
# The first column reports each player's average driving distance in yards. 
#The second column reports the percentage of the player's drives that finish in the fairway, measuring their accuracy. 
#The third and final column has a 1 to denote a female golfer (on the LPGA tour), and a 2 to denote male golfer (on the PGA tour).

#code for solving honor quiz
#golfdistance=read.table('http://users.stat.ufl.edu/~winner/data/pgalpga2008.dat',header=T)
golfdistance=read.table('~/gslprogrames/BaeysianDatatoAnalisisCoursera/Rcodes/pgalpga2008.dat',header=T)
golfdistance1<-golfdistance

attach(golfdistance1)
names(golfdistance1)

golfdistance1$X1[golfdistance1$X1 == 1] <- 0
golfdistance1$X1[golfdistance1$X1 == 2] <- 1
attach(golfdistance1)
names(golfdistance1)


#the height of children is more for taller paprents and less for shorter parents
golfdistance1.lm=lm(X67.0~X243.2+X1) #lm is the linear regression model with independent varial temperature and dependent variable Damage I
summary(golfdistance1.lm)

# Call:
#   lm(formula = X67.0 ~ X243.2 + X1)
# 
# Residuals:
#   Min       1Q   Median       3Q      Max 
# -25.0871  -2.8427   0.4869   3.3746  12.0241 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 147.3354     7.0460  20.911  < 2e-16 ***
#   X243.2       -0.3231     0.0285 -11.334  < 2e-16 ***
#   X1            8.9468     1.2714   7.037 1.04e-11 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 4.803 on 350 degrees of freedom
# Multiple R-squared:  0.359,	Adjusted R-squared:  0.3553 
# F-statistic:    98 on 2 and 350 DF,  p-value: < 2.2e-16

#The posterior mean for intercept is 102.88523
plot(fitted(golfdistance1.lm), residuals(golfdistance1.lm))#plotting residuals
