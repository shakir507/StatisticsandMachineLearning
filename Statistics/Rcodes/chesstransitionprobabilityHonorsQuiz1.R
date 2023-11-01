# Which of the following gives the transition probability matrix for the chess example in the previous question? The first row and column correspond to X=0X=0 (player A not playing) while the second row and column correspond to X=1X=1 (player A playing).
# (0 1;0.30.7)
Q=matrix(c(0.0, 1,0.3,0.7),nrow=2,byrow = TRUE)

# Continuing the chess example, suppose that the first game is between Players B and C. What is the probability that Player A will play in Game 4? Round your answer to two decimal places.
#in the first game the probality of playing is 0 and second is 1

#Ans:The distribution for XX in Game 4 in this case is (1,0) Q^3(1,0) (using the initial distribution and three transitions).

c(1,0)%*%Q%*%Q%*%Q#pick second element for prob of playing this is 0.79

#Which of the following is the stationary distribution for XX in the chess example?
Qn=Q
for(i in 2:1000){
  Qn=Qn%*%Q
}
c(1,0)%*%Qn #this give (0.231,0.769)
