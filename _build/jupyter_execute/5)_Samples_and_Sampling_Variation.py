# 5) Samples and Sampling Variation

Vitor Kamada

econometrics.methods@gmail.com

Last updated 7-20-2020

#### 5.1) What is the difference between population and sample?

Population is the entire collection of interest; whereas sample is a subset of the population.

A representative sample reflect the mix in the entire population. If a sample distorts the population, for example, omitting a portion of the population, we say that the sample has bias.

#### 5.2) What is best way to get a representative sample of the population?

The best way is randomization, that is, pick members of the population at random.

Randomization guarantees that on average a sample mimics the population.

Let's assume that the dataset from Bertrand & Mullainathan (2004) is the population. 

import pandas as pd
path = "https://github.com/causal-methods/Data/raw/master/" 
population = pd.read_stata(path + "lakisha_aer.dta")
population.head(4)

Let's focus on only three variables of the dataset. The population is composed by 4870 individuals. The average year of experience ('yearsexp') is 7.84 years. Among these individuals, 41.15% has volunteer experience, and 9.7% was a military.

population = population.loc[:, ['yearsexp', 'volunteer', 'military']]
population.describe()[0:2]

Let's extract a random sample of 300 individuals from the population (4870 individuals).

The mean of each variable of the sample is closer to the mean of the population. 

Among the three samples, the means vary slightly. We call this sampling variation.

sampple1 = population.sample(300)
sampple1.describe()[0:2]

sampple2 = population.sample(300)
sampple2.describe()[0:2]

sampple3 = population.sample(300)
sampple3.describe()[0:2]

#### 5.3) Is a large non-random sample more likely to be representative of the population than a small random sample?

No. A large non-random sample is bias and useless.

#### 5.4) Are voluntary response samples representative of the population? 

Voluntary response sample is a sample consisting of individuals who volunteer when given the opportunity to participate in a survey.

Voluntary response samples are usually biased toward those with strong negative opinions. 

#### 5.5) How reliable is the U.S. Census?

U.S. Census is designed to be a comprehensive survey of the entire population. It is too costly to interview everybody, then they extract random samples of the population. 

U.S. Census is not perfect, but reasonable. It is likely to undercount homeless and illegal immigrants.

Overall, all surveys have a high rate of nonresponse. The problem with nonresponse is that those who don't respond may differ from those who do.

#### 5.6) What is the difference between population parameter and sample statistic?

Population parameter is a characteristic, usually unknown, of the population; whereas sample statistic is an observed characteristic of a sample.

![alt text](https://github.com/causal-methods/Data/raw/master/figures/PopVsStat.PNG)

#### 5.7) What is sampling variation?


Sampling variation is the variability in the value of a statistic from sample to sample. A population has a fixed set of parameters, but each sample has its own statistic.

From question 5.2, we know that in the population, the average year of experience is 7.84 years ($\mu = 7.84$). Let's extract 5000 random samples of size 100, and calculate the mean of these 5000 random samples.


import numpy as np
result = []
for i in np.arange(5000):
  sample_mean = population.sample(100).yearsexp.mean()
  result = np.append(result, sample_mean)

result.mean()   

See the variation of the sample means.

result

Let's visualize these 5000 random samples.

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Histogram(x=result))
fig.show()

Formally, 5000 random sample extractions can be represented by 5000 iid random variables ($X_1, X_2,...,X_{5000}$) that follows normal distribution: $X\sim N(\mu,\sigma^{2})$. Let $\bar{X}$ be the mean of these random variables:

$$ \bar{X} = \frac{1}{5000}(X_1 + X_2 +...+X_{5000}) $$

$$ E[\bar{X}] = E[\frac{1}{5000}(X_1 + X_2 +...+X_{5000})] $$

$$ = \frac{1}{5000}[E(X_1) + E(X_2) +...+E(X_{5000})] $$

$$ =\frac{1}{5000}(5000\cdot \mu)$$

$$=\mu $$

$$=7.84 $$

#### 5.8) What is the standard error of the mean, $SE(\bar{X}) $?

The sample-to-sample standard deviation of $\bar{X}$, is known as the standard error of the mean.

Let's calculate $Var(\bar{X})$, assuming that $ \bar{X}$ is the mean of $n$ iid random variables ($X_1, X_2,...,X_{n}$).


$$Var(\bar{X}) =Var[\frac{1}{n}(X_1 + X_2 +...+X_{n}]$$

$$ =\frac{1}{n^2}Var[(X_1 + X_2 +...+X_{n}] $$ 

$$ =\frac{1}{n^2}[Var(X_1) + Var(X_2) +...+Var(X_{n}] $$ 

$$ =\frac{1}{n^2}(n\cdot \sigma^2)$$ 

$$ =\frac{1}{n}\sigma^2$$ 

By definition, standard deviation,  $SD(\bar{X})$, is the square root of the variance. Therefore, the  standard error of the mean of a simple random sample of $n$ measurements from a population with variance $\sigma^2$ is:

$$  SD(\bar{X})= SE(\bar{X}) = \sqrt{Var(\bar{X})}$$

$$   = \sqrt{\frac{1}{n}\sigma^2}$$

$$  = {\frac{\sigma}{\sqrt{n}}}$$



## Exercises

1| The population of Sweden in 2019 is about 10 million, and the population of China is about 1.4 billion. I want to estimate the average income of these two countries. Do the random samples of the Chinese population need to be larger than random samples of the Swedish population? Justify.

2| Evaluate each statement True or False, and justify.

a) Randomization produces samples that mimic the characteristics of the population without systematic bias.

b) Every member of the population is equally likely to be in a simple random sample.

c| The customer reviews that you read at Amazon.com is likely to be representative of the population.

3| Do you agree with the statement: "Certain studies that test therapies/drugs looked too good because the subjects were never those who had severe cases". Justify.

4| Let $\bar{X}$ be the mean of $n$ iid random variables ($X_1, X_2,...,X_{n}$). Show that $E(\bar{X})=\mu$

## Reference

Adhikari, A., DeNero, J. (2020). Computational and Inferential Thinking: The Foundations of Data Science. [Link](https://www.inferentialthinking.com/chapters/intro.html) 

Adhikari, A., Pitman, J. (2020). Probability for Data Science. [Link](http://prob140.org/textbook/README.html) 

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link](https://www.textbook.ds100.org/intro) 