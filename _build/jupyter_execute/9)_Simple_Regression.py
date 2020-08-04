# 9) Simple Regression

Vitor Kamada

econometrics.methods@gmail.com

Last updated 8-2-2020

#### 9.1) What is a simple regression model?

Simple regression is a model that measures how an explanatory variable $X$ is associated with a response variable $Y$.

$$  Y = \beta_0 + \beta_1X + \epsilon$$

where $\beta_0$ is the intercept, $\beta_1$ the slope, and $\epsilon$ is the error term.

#### 9.2) What is the conditional mean, $E(Y|X=x)$?

Conditional mean is the average of one variable ($Y$) given that another variable ($X$) takes on a specific value ($x$).

Let's calculate the conditional mean of the simple regression:

$$  Y = \beta_0 + \beta_1X + \epsilon $$

Take the conditional expectation:

$$ E(Y|X=x) = E[(\beta_0 + \beta_1X + \epsilon)|X=x] $$ 

$$ = E(\beta_0|X=x) +  E(\beta_1X|X=x) + E(\epsilon|X=x)  $$

$$ = \beta_0  + \beta_1X + 0$$

Therefore:

$$ E(Y|X=x) = \mu_{y|x} = \beta_0  + \beta_1X$$ 

The main assumption of simple regression is that:

$$ E(\epsilon|X=x) =0  $$

The expression above holds if the error term ($\epsilon$) is independent of the explanatory variable ($X$).

#### 9.3) What are the properties of the error term, $\epsilon$? 

The error term ($\epsilon$) is the deviation from the conditional mean.

We cannot observe the error term ($\epsilon$), but we know that:

$$ \epsilon = Y - E(Y|X=x) $$ 


We assume that the errors:
1.   are independent of one another:

$$   \epsilon_i \perp \epsilon_j, \  \forall \ i \ne j  $$

2.   have equal variance: 

 $$Var(\epsilon) = \sigma^2_\epsilon$$

Therefore, the errors follow normal distribution with mean 0 and variance $\sigma^2_\epsilon$:

$$ \epsilon \sim N(0, \sigma^2_\epsilon) $$

These assumptions are necessary for classical inference (statistical test and confidence interval).



#### 9.4) When the simple regression can be used to establish causality?  

Simple regression can be used to establish causality, when the treatment variable ($T$) is randomized.

$$ Y = \beta_0 + \beta_1T + \epsilon $$

Let's see if 'race' affects the probability of receive a 'call' to an interview, using experimental data from Bertrand & Mullainathan (2004). In this study, 'race' was randomized. They randomly assigned a Black sounding name (ex: Lakish or Jamal) to half of the CVs and a White sounding name (ex: Emily or Greg) to the other half.

$$ call = \beta_0 + \beta_1race + \epsilon $$

The result from simple regression is: 

$$ \widehat{call} = 0.0965-0.032\widehat{race} $$

The value of intercept is 9.6%. This is the proportion of White applicants that received a callback for interview. 

The coefficient of 'race' is 3.2%. The interpretation is that being a Black applicant "causes" to receive 3.2% less callbacks for interview.

Remember that 3.2% is a big magnitude, as it represents about 50% differential. In practical terms, Black applicants has to send 15 CVs to secure one interview rather than 10 CVs for White applicants.

The coefficient of the treatment variable is also statistically significant at level of significance ($\alpha$ = 1%).

The t-value of -4.115 is the ratio:

 $$t = \frac{coefficient}{standard\ error} =\frac{-0.032}{0.008} = -4.115$$

 The null hypothesis is:
 
$$H_0: \beta=0$$

The t-value of -4 means that the observed value (-3.2%) is 4 standard deviation below the mean ($\beta=0$). The p-value or probability  of getting this value at chance is virtually 0. Therefore, we reject the null hypothesis that the magnitude of treatment is 0.

We would also reject the null hypothesis based on the 95% confidence interval [-4.7% to -1.7%]. See that the $\beta=0$ is not inside the confidence interval.

# Import Data from Bertrand & Mullainathan (2004)
import pandas as pd
path = "https://github.com/causal-methods/Data/raw/master/" 
df = pd.read_stata(path + "lakisha_aer.dta")

# Create intercept
df['Intercept'] = 1

# Create treatment variable
import numpy as np
df['Treatment'] = np.where(df['race'] =='b', 1, 0)

# Fit simple regression model
import statsmodels.api as sm
ols = sm.OLS(df['call'], df[['Intercept', 'Treatment']],
                    missing='drop').fit()

# Print the results                    
print(ols.summary().tables[1])

#### 9.5) Is it necessary to run a regression to establish causality?

It is not necessary to run a regression to establish causality. The same results of the regression above can be obtained by mean comparison. See the table below.

Only 6.4% of Blacks received a callback; whereas 9.6% of Whites received a callback.

The slope is 0.064 - 0.096 = -0.032

df.loc[:, ('call', 'race')].groupby('race').agg([np.mean])

The practical advantage of regression is that the computer automatically provides the standard errors, t-statistic, p-value, and 95% confidence interval.

We also can get the same t-statistic and p-value from the regression. Note that pvalue=3.940802103128886e-05 is 0, as e-05 = $\frac{1}{10^5}$

from scipy.stats import *
white = df[df['race'] == 'w'] 
black = df[df['race'] == 'b'] 
TwoTail=ttest_ind(white['call'],black['call'], equal_var=True)
TwoTail

#### 9.6) Is the slope $\beta_1$ equal to the correlation between $X$ and $Y$?

The formula for the slope $\beta_1$ in a simple regression is:

$$ \beta_1 = \rho \cdot \frac{SD(Y)}{SD(X)}$$

The slope $\beta_1$ is equal to the correlation $\rho$, when the standard deviation of $Y$ is equal to the standard deviation of $X$: 

$$SD(Y) = SD(Y)$$

As $SD(X)$ and $SD(Y)$ can only be a positive number, a positive correlation ($\rho >0$) means a positive slope; while a negative correlation ($\rho <0$) means a negative slope.

Let's reproduce the result of the regression table in 8.4:

$$  \hat{\beta_1} = -0.058 \cdot \frac{0.272}{0.5}    $$

$$ = -0.032$$ 

correlation = np.corrcoef(df['Treatment'], df['call'])
correlation

sdx = np.std(df['Treatment'])
sdx

sdy = np.std(df['call'])
sdy

beta1 = correlation[0,1]*sdy/sdx
beta1

#### 9.7) What is the formula for the intercept, $\beta_0$?

The formula for the intercept, $\beta_0$ is:

$$ \beta_0 = E[Y] - \beta_1E(X) $$

For data notation:

$$ \hat\beta_0 = \bar{y} - \hat\beta_1 \bar{x} $$ 

$$ =0.0804-(0.032\cdot0.5)  $$

$$ =0.0965  $$

ymean = np.mean(df['call'])
ymean

xmean = np.mean(df['Treatment'])
xmean

beta0 = ymean - (beta1*xmean)
beta0

#### 9.8) What is the R-squared, $R^2$ in a simple regression?

 R-squared is the square of the correlation between $X$ and $Y$. It measures the percentage of "explained" variation in $Y$ by using $X$.

 Let's calculate the $R^2$ for the regression in 8.4:

 $$ R^2 = \rho^2_{XY}$$

$$ =-0.058^2 $$

 $$ = 0.0034$$

 The explanatory variable 'race' explains 0.34% of the variation in the response variable 'call'.

r2 = correlation[0,1]*correlation[0,1]
r2 

ols.rsquared

#### 9.9) Should I care about $R^2$ to establish causality?

$R^2$ is irrelevant to establish causality. The previous example shows that 'race' and 'call' were pretty much uncorrelated ($r = -0.058$) and $R^2$ was below 1%. However, 'race' was randomized, and the coefficient of the 'race' was statistically significant. Therefore, we can rigorously claim that being Black causes a lower callback for interview. In other words, racial discrimination is real. 

Note that $R^2$ only captures linear association, that is, how the data points are closer to the line. When both explanatory and response variable only vary from 0 to 1, the data points don't fit well to the line.

## Exercises

1| Explain what is the difference between correlation and causation in the context of simple regression?

2| Bertrand & Mullainathan (2004) randomized another variable 'h'. The variable 'h': 1 = higher quality curriculum vitae; 0 = lower quality curriculum vitae. What is the proportion of callback for an interview broken by quality of curriculum vitae? 

3| Run a simple regression with response variable 'call' and explanatory variable 'h'. 

a) Interpret the intercept and slope. 

b) What is the p-value of the variable 'h'?

c) Is the quality curriculum vitae statistically significant at $\alpha = 5\%$? and  $\alpha = 10\%$?

d) What is the range of the 95% confidence interval of the intercept?

e) Is the intercept statistically significant? Adopt a level of significance $\alpha$ and justify.

f) Calculate the $R^2$. Interpret the obtained value.

## Reference

Adhikari, A., DeNero, J. (2020). Computational and Inferential Thinking: The Foundations of Data Science. [Link](https://www.inferentialthinking.com/chapters/intro.html) 

Bertrand, Marianne, and Sendhil Mullainathan. (2004). Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination. American Economic Review, 94 (4): 991-1013.

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link](https://www.textbook.ds100.org/intro)