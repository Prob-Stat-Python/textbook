# 6) Confidence Intervals

Vitor Kamada

econometrics.methods@gmail.com

Last updated 7-21-2020

#### 6.1) What is the confidence interval?

 Confidence interval is a range of values for a parameter of the sampled population. 

 Narrow confidence interval suggests precise estimate. Wide confidence interval suggests that little is known about the population.

#### 6.2) What is the z-interval for proportion ($p$)?

A confidence interval that assumes a normal model for the sampling distribution.

Confidence interval for proportion ($p$) is:

$$ \hat{p}\pm z_{\frac{\alpha}{2}} \cdot se(\hat{p}) $$

$$ \hat{p}\pm z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} $$

where $P(Z>z_{\alpha})=\alpha$ for $Z\sim N(0,1)$. For a 95% confidence interval, the level of significance ($\alpha$) is 5%, then $z_{2.5\%} = 1.96$.

#### 6.3) Microsoft believes that 75% of Windows users are super satisfied with the operational system. If that's the case, what range holds 95% of all sample proportions if $n=225$?

$$ \hat{p}\pm z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} $$

$$ 0.75\pm 1.96\sqrt{\frac{0.75(1-{0.75})}{225}} $$

$$ 0.693 \leq p \leq  0.807 $$

#### 6.4) What is Student's t-distribution?

Student's t-distribution is a model for the sampling distribution that compensates for substituting the standard deviation of the sample ($s$) for the standard deviation of the population ($\sigma$) in the standard error.

Student's t-distribution is the exact sampling distribution of the random variable:

$$T_{n-1} = \frac{\bar{X}-\mu}{\frac{S}{\sqrt{n}}}$$

where $(n-1)$ is the degrees of freedom (df). As $n \rightarrow \infty$, t-distribution converge to normal distribution. 

See in the chart that t-distribution with degrees of freedom ($df=5$) has thick tails that accommodates more numbers of outliers than the normal distribution. Note that t-distribution with degrees of freedom ($df=30$) is indistinguishable from normal distribution.


import numpy as np
from scipy.stats import t, norm
import matplotlib.pyplot as plt
%matplotlib inline

x = np.linspace(-4, 4, 100)

t_dist5 = plt.plot(x, t(5).pdf(x), 'b', label='t, df=5')
t_dist30 = plt.plot(x, t(30).pdf(x), 'g--', label='t, df=30')

normal_dist = plt.plot(x, norm.pdf(x), 'r--',label='Normal')

plt.legend()
plt.show()

#### 6.5) What is the t-interval for the mean ($\mu$)?

The $100(1-\alpha)\%$ confidence t-interval for $\mu$ is:

$$ \bar{x}\ \pm t_{\frac{\alpha}{2},n-1}\frac{s}{\sqrt{n}}$$

where $P(T_{n-1} > t_{\frac{\alpha}{2},n-1}) = \frac{\alpha}{2}$ for $T_{n-1}$ distributed as a student's t-random variable with degrees of freedom ($df = n-1$).

#### 6.6) A manager claims that the clients have on average $6,200 in the bank. How reasonable is the claim?

A random sample of 49 clients shows the average $\bar{x}=4,200$ with standard deviation ($s = 3,500$).


We can use the code below to get:

$$t_{\frac{\alpha}{2},n-1} =
 t_{2.5\%,48} =-2.01 $$

t.ppf(0.025,48)

The 95% confidence interval for $\mu$ is:

$$ \bar{x}\ \pm t_{\frac{\alpha}{2},n-1}\frac{s}{\sqrt{n}}$$

$$ 4,200 \pm 2.01 \frac{3,500}{\sqrt{49}} $$

$$ \$3,195 \leq \mu \leq \$5,205 $$ 

The manager' claim is not compatible with the data. The average $6,200 is far above the confidence interval.

#### 6.7) What is the margin of error?

Margin of error (ME) of 95% confidence interval for $\mu$:

$$ ME = t_{2.5\%,n-1}\frac{s}{\sqrt{n}}$$ 

Margin of error (ME) of 95% confidence interval for $p$:

$$ ME = z_{2.5\%}\frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{n}}$$ 

It is very common to round and replace the $t_{2.5\%,n-1}$ and $z_{2.5\%}$ by 2. 


#### 6.8) Justify the numbers below:
![alt text](https://github.com/causal-methods/Data/raw/master/figures/MarginError.PNG)

$$ ME = z_{2.5\%}\frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{n}}$$ 

Replace $z_{2.5\%}$ by 2. The variance, $\hat{p}(1-\hat{p})$, is maximum, when $\hat{p} = \frac{1}{2}$

$$ ME = 2\frac{\sqrt{\frac{1}{2}(1-\frac
{1}{2})}}{\sqrt{n}}$$ 

$$ ME = 2\frac{\sqrt{\frac{1}{2}(1-\frac
{1}{2})}}{\sqrt{n}}$$ 

$$ ME = 2\frac{(\frac
{1}{2})}{\sqrt{n}}$$ 

$$ ME = \frac{1}{\sqrt{n}}$$

Let's test $n=400$:

$$ ME = \frac{1}{\sqrt{400}} $$

$$= \frac{1}{20} $$

$$= 0.05 $$

$$=5\% $$

## Exercises

1| Find the 95% z-interval for the parameter $p$, given $\hat{p}=0.5$, $n=36$.

2| A school claims that the students have on average a score of 690 in SAT Math Test. How reasonable is the claim? A random sample of 36 students from this school has average $\bar{x}= 650$, with standard deviation ($s=100$).

3| Do you agree with the statement: "All other things the same, a 90% confidence interval is narrow than a 95% confidence interval." Justify.

4| What is the probability that $\bar{X}>\mu?$

5|  What is the coverage of the confidence interval $[\hat{p}$ to $1]$?

6| Fox News interviewed 500 voters and claimed that the margin of error is less than 3% to predict the outcome of the election. Do you agree? Justify.

## Reference

Adhikari, A., DeNero, J. (2020). Computational and Inferential Thinking: The Foundations of Data Science. [Link](https://www.inferentialthinking.com/chapters/intro.html) 

Adhikari, A., Pitman, J. (2020). Probability for Data Science. [Link](http://prob140.org/textbook/README.html) 

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link](https://www.textbook.ds100.org/intro) 