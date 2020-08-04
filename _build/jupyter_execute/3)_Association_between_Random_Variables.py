# 3) Association between Random Variables

Vitor Kamada

econometrics.methods@gmail.com

Last updated 7-18-2020

#### 3.1) If \$6000 is invested in Amazon, and \$2000 in Intel, what is the expected return? 

 Suppose Amazon and Intel stocks have recently been rising 2.1% and 0.4% per month, respectively.

 Let's $Z$ be the portfolio composed by stocks X and Y:

 $$Z=aX+bY$$
 $$E(Z)=aE(X)+bE(Y)$$

Then:

$$E(6000X+2000Y)$$

$$=6000(0.021)+2000(0.004)$$

$$ =\$134 $$


#### 3.2) What is the variance of the portfolio Z?

Based on previous question:

 $$Z=aX+bY$$
$$Var(Z)=Var(aX+bY)$$

If X and Y are independent:

$$Var(aX+bY)=a^2Var(X)+b^2Var(Y)$$

 Suppose that the variance of Amazon and Intel stocks are respectively 0.72% and 0.27% per month.

$$Var(6000X+2000Y)$$
$$=6000^2(0.0072)+2000^2(0.0027)$$
$$=270,000$$

This value is hard to interpret, because the measurement unit is a square term.

#### 3.3) What is the standard deviation of the portfolio Z?

$$SD(Z) = \sqrt{Var(Z)}$$

$$=\sqrt{\$^2270,000}$$

$$ = \$520 $$

An outcome in the range of \$520 above or below the expected return is very likely to occur.

#### 3.4) What is the covariance between Random Variables?

The covariance between random variables is the expected value of the product of deviations from the means.

$$ \sigma_{xy}= Cov(X,Y)=E[(X-\mu_x)(Y-\mu_y)]$$

It is hard to interpret, because the units of random variables X and Y are multiplied.

#### 3.5) What is $Cov(X,X)$?

By definition:

$$ Cov(X,Y)=E[(X-\mu_x)(Y-\mu_y)]$$

Then:

$$ Cov(X,X)=E[(X-\mu_x)(X-\mu_x)]$$

$$ =E[(X-\mu_x)^2] $$

$$ =Var(X) $$

Therefore, variance is a special case of covariance.

#### 3.6) Show that $Cov(X,Y)=E(XY)-\mu_x\mu_y$.

By definition:

$$ Cov(X,Y)=E[(X-\mu_x)(Y-\mu_y)]$$

Then:

$$=E(XY-X\mu_y-\mu_xY +\mu_x\mu_y)$$

$$=E(XY)-\mu_yE(X)-\mu_xE(Y) +\mu_x\mu_y$$

$$=E(XY)-\mu_x\mu_y-\mu_x\mu_y +\mu_x\mu_y$$

$$=E(XY)-\mu_x\mu_y$$

#### 3.7) Prove that if $X$ and $Y$ are independent, then $Cov(X,Y)=0$.

 Remember the definition of two independent events A and B:
 
 $$ P(A\cap B) = P(A) \cdot P(B) $$ 

 If $X$ and $Y$ are independent random variables, then:

 $$E(XY)= E(X) \cdot E(Y)$$


 From previous question:

 $$Cov(X,Y)=E(XY)-\mu_x\mu_y$$

 $$ = E(X) \cdot E(Y)-\mu_x\mu_y$$

 $$ =\mu_x\mu_y-\mu_x\mu_y$$
 $$ 0$$

 **Intuition**: If X and Y are independent random variables, knowledge or information of random variable X doesn't help in predicting the outcome of random variable Y, and vice-versa. Therefore, there is no linear association between these two variables: $Cov(X,Y)=0$. 


#### 3.8) Show that $Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$.

By definition:

$$ Var(X)=E[(X-\mu_x)^2] $$

Then:

$$ Var(X+Y)=E[(X+Y-\mu_x-\mu_y)^2] $$

$$ =E[(X-\mu_x+Y-\mu_y)^2] $$

$$ =E[(X-\mu_x)^2+(Y-\mu_y)^2 +2(X-\mu_x)(Y-\mu_y)] $$

$$ =E[(X-\mu_x)^2]+E[(Y-\mu_y)^2] +2E[(X-\mu_x)(Y-\mu_y)] $$

 $$=Var(X)+Var(Y)+2Cov(X,Y)$$


#### 3.9) What is correlation, $\rho$?

The correlation is the covariance divided by the product of standard deviations:

$$ \rho = \frac{Cov(X,Y)}{\sqrt{Var(X)\cdot Var(Y)}} =\frac{\sigma_{xy}}{\sigma_x \sigma_y} $$

The correlation is easy to interpret. It ranges from -1 to +1. 

$$ -1 \leq \rho \leq 1 $$

It is unit free. The units from covariance are removed by the division of the product of standard deviations.

#### 3.10) If $X$ and $Y$ are uncorrelated ($\rho =0$), it is possible to conclude that $X$ and $Y$ are independent?

Suppose that the joint probability distribution,  $P(X,Y)$, is given by the table below.

![alt text](https://github.com/causal-methods/Data/raw/master/figures/JointProb.PNG)

The random variables X and Y are independent if:

$$P(X,Y)=P(X)\cdot P(Y)$$

$P(X=10, Y=0)=1/2$

$P(X=10) = 0+\frac{1}{2} +0$

$P(Y=0) = \frac{1}{2} + 0$

Therefore, X and Y are dependent:

$$P(X=10,Y=0)\neq P(X=10)\cdot P(Y=0)$$

$$\frac{1}{2} \neq \frac{1}{4} $$

Let's convert the table in a format useful for calculations:

x = [10, 10, 10, -10, -10, -10]
y = [-10, 0, 10, -10, 0, 10]
probXY = [0, 1/2, 0, 1/4, 0, 1/4]

dictionary = {'x': x, 'y': y, 'P':probXY }
import pandas as pd
table = pd.DataFrame(dictionary)
table

We calculated that $\mu_x=0$, and $\mu_y=0$.

table['x*P'] = table['x']*table['P']
table['y*P'] = table['y']*table['P']
table

sum(table['x*P'])

sum(table['y*P'])

We get that $E(XY) =0$.

table['x*y'] = table['x']*table['y']
table['x*y*P'] = table['x*y']*table['P']
table

sum(table['x*y*P'])

 Therefore: $Cov(X,Y)=E(XY)-\mu_x\mu_y = 0$

$$ \rho = \frac{Cov(X,Y)}{\sqrt{Var(X)\cdot Var(Y)}} =0$$

We cannot conclude that if correlation is zero, the two random variables are independent.

**Intuition**: Dependency is a stronger concept than correlation. Dependency capture any relationship between variables, ex: quadratic relationship; whereas, correlation only capture linear relationship. 

## Exercises

1| If you want a portfolio with small risk (variance), should you look for investments that have positive covariance, have negative covariance, or are uncorrelated? Justify.

2| When $Var(X+Y)=Var(X)+Var(Y)$? Explain.

3| Does a portfolio formed from the mix of three investments have more risk (variance) than a portfolio formed from two? Make assumptions and justify you reasoning.

4| What is the covariance between a random variable and itself? 

5|  What is the correlation between a random variable and itself?

6| What's the covariance between a random variable X and a constant?

7| Suppose a random  variable $X$ can take only the three values -1, 0,
and 1, and that each of these three values has the
same probability. Let $Y = X^2$.


a) Show that $Correlation(X,Y) = 0$.

b) Are X and Y independent? Justify.

## Reference

Adhikari, A., Pitman, J. (2020). Probability for Data Science. [Link](http://prob140.org/textbook/README.html) 

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link]( https://www.textbook.ds100.org/intro) 