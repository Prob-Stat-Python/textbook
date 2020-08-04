# 2) Random Variables

Vitor Kamada

econometrics.methods@gmail.com

Last updated 7-18-2020

#### 2.1) What is a random variable?

It is a statistical model that describes uncertain outcome of a random process. 

Let's model stock price as a random variable X:

stock = ['Increases', 'Stays same','Decreases']
x = [10, 0, -9]
prob = [0.3, 0.5, 0.2]
table = {'Stock Price':stock, 'x': x, 'P(X=x)':prob }
import pandas as pd
X = pd.DataFrame(table)
X

The capital "X" stands for the random variable; whereas the lower case "x" indicates the possible outcomes (10, 0, -9). The statement $P(X=x_i)$ means the probability of the outcome $x_i$. For example, $P(X=x_0) = P(X=10) = 0.3$.

#### 2.2) How to calculate the expected value of a random variable X, denoted by E(X)?

Expected value is a weighted average that uses probabilities to weight the possible outcomes.

Let's calculate the mean ($\mu$) or expected value of the previous example random variable (X):

$$ \mu = E(X) = \sum_{i=0}^{n} x_iP(X=x_i) $$

$$ x_0P(X=x_0)+...+x_nP(X=x_n)$$

$$ 10*0.3+0*0.5-9*0.2$$

$$ 3+0-1.8 = 1.2$$

Therefore, the average return of this stock X is $1.2.

Let's show the calculations step by step:

X['x*P(X=x)'] = X['x']*X['P(X=x)']
X

Sum up the rows of 'x*P(X=x)':

sum(X['x*P(X=x)'])

#### 2.3) How to calculate the variance of X, denoted by Var(X)?

The variance of a random variable X is the expected value of the squared deviation from its mean $\mu$:

$$ \sigma^2=E[(X-\mu)^2] = Var(X)$$

$$ \sum_{i=0}^{n} (x_i - \mu)^2 P(X=x_i) $$

$$  (x_0 - \mu)^2 P(X=x_0)+...+(x_n - \mu)^2 P(X=x_n)   $$

$$ 77.44*0.3+1.44*0.5+104.04*0.2 $$

$$ 23.232 + 0.720 + 20.808 $$

$$ 44.76$$

X['x-mu'] = X['x'] - sum(X['x*P(X=x)'])
X['(x-mu)^2'] = X['x-mu']*X['x-mu']
X['[(x-mu)^2]*P(X=x)'] =  X['(x-mu)^2']*X['P(X=x)']
X

varX = sum(X['[(x-mu)^2]*P(X=x)'])
varX

Variance is a measure of variability around the mean. It is hard to interpret 44.76, because the measurement unit is the square of the measurement unit (\$) of the random variable.

#### 2.4) How to calculate the standard deviation of X, denoted by SD(X) or $\sigma$?

Standard Deviation is the square root of the variance.

$$ \sigma = \sqrt{\sigma^2}=\sqrt{Var(X)}$$

$$ \sqrt{44.76)} $$ 

$$ \$6.7 $$

sdX = varX**(1/2)
sdX

The standard deviation, $\sigma = 6.7$, has the same unit (\$) of the random variable. Therefore, it is easy to interpret. 

One $\sigma$ above the mean ($\mu$) or below the mean ($\mu$) is a very likely outcome.

The standard deviation is a measure of variability around the mean. Bigger the number, bigger the variation.

 In Finance, it is a proxy for risk. You want to minimize risk ($\sigma$) and maximize return ($\mu$).

#### 2.5) Prove that $E(cX) = cE(X)$, where c is a constant.

By definition:

$$ E(X) = x_0p_0+x_1p_1+...+x_np_n$$

Then:

$$ E(cX) = cx_0p_0+cx_1p_1+...+cx_np_n$$

$$  c(x_0p_0+x_1p_1+...+x_np_n)$$

$$ cE(X)$$




#### 2.6) Prove that $Var(cX)=c^2Var(X)$, where c is a constant.

By definition:

$$ Var(X)=E[(X-\mu_x)^2] $$

Then:

$$ Var(cX)=E[(cX-c\mu_x)^2] $$

$$ E[c^2(X-\mu_x)^2] $$

$$ c^2E[(X-\mu_x)^2] $$

$$ c^2Var(X) $$


#### 2.7) Prove that $E(X+c)=E(X)+c$, where c is a constant.


$$ E(X+c) = (x_0+c)p_0+(x_1+c)p_1+...+(x_n+c)p_n$$

$$  x_0p_0+cp_0+x_1p_1+cp_1...+x_np_n+cp_n$$

$$  (x_0p_0+x_1p_1+...+x_np_n) + c(p_0+p_1+...+p_n)$$


As probability must sum up to 1:

 $$ \sum_{i=0}^{n}p_i=1 $$

Then:

$$ E(X) + c$$



#### 2.8) Prove that $E(c)=c$, where c is constant.

By definition:
$$ E(X) = x_0p_0+x_1p_1+...+x_np_n$$

Then:

$$ E(c) = cp_0+cp_1+...+cp_n$$

$$ c(p_0+p_1+...+p_n)$$
$$c$$

#### 2.9) Prove that $Var(c) = 0$, where c is a constant.

By definition:

$$ Var(X)=E[(X-\mu_x)^2] $$

Then:

$$ Var(c)=E[(c-\mu_c)^2] $$

$$ E[(c-c)^2] $$

$$ E[(0)^2] $$

$$0$$

**Intuition:** By definition a constant has no variation.



## Exercises

1| Calculate the E(Y).

stock = ['Increases', 'Stays same','Decreases']
y = [5, 0, -3]
prob = [0.4, 0.1, 0.5]
table = {'Stock Price':stock, 'y': y, 'P(Y=y)':prob }
import pandas as pd
Y = pd.DataFrame(table)
Y

2| Calculate Var(Y).

3| Calculate the SD(Y).

4| Prove that $Var(X+c)=Var(X)$, where c is a constant.

## Reference

Adhikari, A., Pitman, J. (2020). Probability for Data Science. [Link](http://prob140.org/textbook/README.html) 

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link]( https://www.textbook.ds100.org/intro) 