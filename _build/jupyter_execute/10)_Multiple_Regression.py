# 10) Multiple Regression

Vitor Kamada

econometrics.methods@gmail.com

Last updated 8-2-2020

#### 10.1) What is a multiple regression model?

Multiple regression is a model that measures how explanatory variables $X_1, X_2,...,X_k$ are associated with a response variable $Y$.

$$  Y = \beta_0 + \beta_1X_1 + \beta_2X_2 +...+ \beta_kX_k  +  \epsilon$$

where the error term ($\epsilon$) follows normal distribution with mean 0 and variance $\sigma^2_\epsilon$:

$$ \epsilon \sim N(0, \sigma^2_\epsilon) $$

#### 10.2) What is the consequence of running a simple regression rather than a multiple regression?

Assume the real model is: 

$$  Y = \beta_{0m} + \beta_{1m}X_1 + \beta_{2m}X_{2} +...+ \beta_{km}X_k  +  \epsilon_m$$
where, $m$ stands for multiple regression.

A simple regression assumes that all other explanatory variables are inside the error term:

$$  Y = \beta_{0s}  +  \beta_{1s}X_1 +  \epsilon_s$$

$$  \epsilon_s = \beta_2X_2 +...+ \beta_kX_k $$

where $s$ stands for simple regression.

The error term is the sum of all omitted variables in the regression. If these omitted variables are uncorrelated with the explanatory variable of interest ($X_1$), then $\beta_{1s} = \beta_{1m}$.

Note that this is a special case:

$$  Cov(X_1,X_j) =0, \  \ \forall \ j \ne 1$$

where $X_1$ is randomized.

Therefore, for observational studies,  $\beta_{1s}$ is likely to be different than $\beta_{1m}$. In this case, we say that $\beta_{1s}$ is biased and captures spurious effects.

#### 10.3) How to use a multiple regression to check if an experimental study is reliable?

Based on theory, if the treatment variable (T) was randomized, then the treatment variable (T) will be independent of other factors:

$$T \perp Other \ Factors$$

In an experiment, the addition of other factors in the regression cannot affect the estimation of the coefficient of the treatment variable ($\beta_{1s}$). If you see substantial changes in $\beta_{1m}$, you can infer that you are not working with experimental data.

Note that in observational studies, you must always control for other factors. Otherwise, you will have the omitted variable bias problem. 

We run simple and multiple regressions using the experimental data from Bertrand & Mullainathan (2004), and we can conclude that the treatment variable was in fact randomized:

$$\beta_{1s} = -0.032 $$

$$\beta_{1m} = -0.031 $$


# Open data set from Bertrand & Mullainathan (2004)
import numpy as np
import pandas as pd
path = "https://github.com/causal-methods/Data/raw/master/" 
df = pd.read_stata(path + "lakisha_aer.dta")

# Simple Regression
df['Intercept'] = 1
df['Treatment'] = np.where(df['race'] =='b', 1, 0)
import statsmodels.api as sm
simple = sm.OLS(df['call'], df[['Intercept', 'Treatment']],
                    missing='drop').fit()
print(simple.summary().tables[1])                    

# Multiple Regression
other_factors = ['yearsexp', 'volunteer', 'military',
          'email', 'workinschool', 'honors',
          'computerskills', 'specialskills']
multiple_reg = sm.OLS(df['call'],
                      df[['Intercept', 'Treatment'] + other_factors],
                      missing='drop').fit()
print(multiple_reg.summary().tables[1])                      

#### 10.4) In an observational study, are the results from multiple regression more credible than simple regression?

Overall, the results of a multiple regression are more credible in the sense of suffering less from the problem of omitted variable bias. However, even controlling for many factors, the estimated coefficients are likely to be biased. 

#### 10.5) In an observational study, comparing simple and multiple regressions, how different might be the coefficients?

It might be a big difference, a change of sign, leading to completely divergent explanations. 

For example, using data from Meyersson (2014), a simple regression indicates that in regions controlled by the Islamic party in Turkey, 2.58% less females complete high school compared to regions controlled by a secular party. You might believe that religion limits the educational opportunities of females. 

However, a multiple regression indicates the opposite, in regions controlled by the Islamic party in Turkey, 1.44% more females complete high school compared to regions controlled by a secular party. One explanation is that Islamic religion in fact improves the female high school completion. Maybe poverty is a confound factor that drives higher level of religiosity and poor educational outcome. Therefore, in the simple regression, maybe the religion variable is capturing the poverty effect rather than the true direct effect of religion. 

Note that both results from simple and multiple regression are statistically significant. The magnitudes of the coefficients are also relevant, as the proportion of females between 15 to 20 years old that completes high school is about only 15.4% in Turkey.

# Load data from Meyersson (2014)
df1 = pd.read_stata(path + "regdata0.dta")

# Simple Regression
df1['Intercept'] = 1
simple_reg = sm.OLS(df1['hischshr1520f'], df1[['Intercept', 'i94']],
                    missing='drop').fit()
print(simple_reg.summary().tables[1])

# Multiple Regression
control = ['lpop1994', 'ageshr19', 'merkezi']
mult_reg = sm.OLS(df1['hischshr1520f'],
                      df1[['Intercept', 'i94', 'vshr_islam1994'] + control],
                      missing='drop').fit()
print(mult_reg.summary().tables[1])   

# Proportion of females between 15 to 20 year that completes high school
df1['hischshr1520f'].mean()

## Exercises

1| Interpret the 4 values of the contingency table below. Specifically, state the meaning and compare the values.

The variable 'h': 1 = higher quality curriculum vitae; 0 = lower quality curriculum vitae. This variable was randomized.

Other variables were previously defined.

contingency_table = pd.crosstab(df['Treatment'], df['h'], 
                                values=df['call'], aggfunc='mean')
contingency_table

2| I created an interaction variable 'h_Treatment' that is the pairwise multiplication of the variable 'h' and 'treatment'. 

How can you use the coefficients of the regression below to get the values of the contingency table in exercise 1? Show the calculations. 

df['h_Treatment'] = df['h']*df['Treatment']
interaction = sm.OLS(df['call'],
                      df[['Intercept', 'Treatment', 'h', 'h_Treatment'] ],
                      missing='drop').fit()
print(interaction.summary().tables[1])     

3| Write a code to get a contingency table below:

|firstname\ h |    0.0   |    1.0   | 
|-------------|----------|----------|
|Aisha        | 0.010000 | 0.037500 | 
|Allison      | 0.121739 | 0.068376 | 

Inside the table are the callback rates broken by Curriculum Vitae quality.
What is the callback rate for Kristen and Lakisha? Why the rates are so different? Could we justify the rate difference, arguing that one is more educated and qualified than other? 

## Reference

Adhikari, A., DeNero, J. (2020). Computational and Inferential Thinking: The Foundations of Data Science. [Link](https://www.inferentialthinking.com/chapters/intro.html) 

Bertrand, Marianne, and Sendhil Mullainathan. (2004). Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination. American Economic Review, 94 (4): 991-1013.

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link](https://www.textbook.ds100.org/intro)

Meyersson, Erik. 2014. "Islamic Rule and the Empowerment of the Poor and Pious". Econometrica, 82(1), 229-269.