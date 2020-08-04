# 8) Experiment 

Vitor Kamada

econometrics.methods@gmail.com

Last updated 8-2-2020

#### 8.1) What is an experiment?

Experiment is a method that uses randomization to produce data that reveal causation. 

A typical experiment consists in:
1.   Selecting a random sample from a population
2.   Assigning subjects at random to treatments
3.   Comparing the responses of subjects among the treatments

The treatment is the variable manipulated by the experimenter, in order to see its effect on subjects. 

In observational studies, the treatment variable is not randomized. Without randomization, it is not possible to know if observed difference in the response is due to the treatment or to confounding factors. 

An observational study cannot answer if a drug cure or not a disease. The treatment group might be composed by younger, sport enthusiasts, healthy patients; whereas the control group by old, lazy, and unhealthy patients. There is no way to separate the effects of the drug from the effects of age, practicing physical exercise, and initial health status.

However, when the treatment variable is randomized, control group and treatment group are on average like to each other. Therefore, automatically all confounding factors are eliminated.


#### 8.2) What is average causal effect? 

As far as the treatment variable is randomized, the average causal effect is the difference in group means between the treatment ($T=1$) and control group ($T=0$). Let's assume that $Y$ is the outcome variable. 

$$ E[Y|T=1]-E[Y|T=0] $$

$$ \frac{1}{n} \sum_{i=1}^{n}[y_{t=1,i}-y_{t=0,i}] $$

$$ \frac{1}{n} \sum_{i=1}^{n}y_{t=1,i} - \frac{1}{n} \sum_{i=1}^{n}y_{t=0,i} $$


$$ \bar{y}_{t} - \bar{y}_{c} $$

where $c$ is the control group, that is, when $T=0$.

#### 8.3) Why is easy to establish the causal effect of a drug, but hard to establish if racial discrimination is real?

A drug can be assigned at random to subjects, but in practical terms, a skin color not, because it is a property of the subjects. The drug question represents the typical research question in Hard Science; while the racial discrimination is the typical question of Human Science. 

When we see lower wages among Blacks, it is hard to distinguish if this is an effect of racial discrimination, or lower level of education, networking, etc.

However, Bertrand & Mullainathan (2004) have a clever idea of manipulating race on curriculum vitae (CVs). They randomly assigned a Black sounding name (ex: Lakish or Jamal) to half of the CVs and a White sounding name (ex: Emily or Greg) to the other half. They sent the CVs for real jobs in Chicago and Boston. The result was that only 6.4% of Blacks received a callback for interview; whereas 9.6% of Whites received a callback.

Let's open the dataset from Bertrand & Mullainathan (2004).

import pandas as pd
path = "https://github.com/causal-methods/Data/raw/master/" 
df = pd.read_stata(path + "lakisha_aer.dta")
df

Let's restrict the analysis to the variables 'call' and 'race'. 

call: 1 = applicant was called back to interview; and 0 otherwise.

race: w = White, and b = Black.

import numpy as np
callback = df.loc[:, ('call', 'race')]
callback.groupby('race').agg([np.size, np.mean])

#### 8.4) How to check the integrity of an experimental study?

Based on theory, we know that the randomization of the treatment variable will produce a control group like the treatment group. 

Let's check the proportion of Blacks and Whites with college degree in the dataset from Bertrand & Mullainathan (2004)

Originally, college graduate was coded as 4 in the variable 'education'. 3 = some college. 2 = high school graduate. 1 = some high school. 0 not reported.

Let's create the variable 'college' = 1, if a person completes a college degree; and 0 otherwise.

df['college'] = np.where(df['education'] == 4, 1, 0)

We can see that 72.2% of Black Applicants have a college degree. The proportion of Whites with college degree is very similar 71.6%. 

college = df.loc[:, ('college', 'race')]
college.groupby('race').agg([np.size, np.mean])

Let's check this statement for other factors in the CVs. The names of the variables are self-explanatory, and more information can be obtained reading the paper from Bertrand & Mullainathan (2004).

resume = ['college', 'yearsexp', 'volunteer', 'military',
          'email', 'workinschool', 'honors',
          'computerskills', 'specialskills']
both = df.loc[:, resume]
both.head()

Let's use a different code to calculate the mean of the variables for the whole sample (both Whites and Blacks) and broken samples between Blacks and Whites.

See that the average years of experience (yearsexp) is 7.84 for the whole sample, 7.82 for Blacks, and 7.85 for Whites.

If you check all variables the mean values for Blacks are very closer to the mean values for Whites. This is the consequence of randomization.

We also calculate the standard deviation (std), a measure of variation around the mean. Note that the standard deviation is pretty much the same between the whole sample and split samples. Like the mean, you don't suppose to see much difference among standard deviations in the case of experimental data.

The standard deviation of the variable years of experience is 5 years. We can state roughly the most part of observations (about 68%) is between 1 std below the mean and 1 std above the mean, that is, between [2.84, 12.84].

black = both[df['race']=='b']
white = both[df['race']=='w']
summary = {'mean_both': both.mean(),   'std_both': both.std(),
           'mean_black': black.mean(), 'std_black': black.std(),
           'mean_white': white.mean(), 'std_white': white.std()}
pd.DataFrame(summary)

#### 8.5) Test if Whites and Blacks have the same average years of experience.  

The average years of experience for Whites is
 7.82, while for Blacks is 7.85. We can see that they are pretty much the same, but let's be formal and carry out a statistical test:

 $$  H_0: \mu_w= \mu_b $$ vs $$ H_a:\mu_w \ne \mu_b $$

 $$  t =  \frac{\bar{x}_w - \bar{x}_b}{s_p \sqrt{\frac{1}{n_w} + \frac{1}{n_b} }}   $$

 where the pool standard deviation ($s_p$) is:

 $$ \sqrt{\frac{ \sum_{i=1}^{n_w}(x_{wi} - \bar{x} _w)^2  +  \sum_{i=1}^{n_b}(x_{bi} - \bar{x} _b)^2 }{n_w + n_b -2}}  $$

The t-statistic is 0.18 and respective p-value is 0.85. Therefore, we cannot reject the $H_0$.  

from scipy.stats import *
white = df[df['race'] == 'w'] 
black = df[df['race'] == 'b'] 
TwoTail=ttest_ind(white['yearsexp'],black['yearsexp'], equal_var=True)
TwoTail

#### 8.6) Why the randomization of the treatment variable makes control group and treatment group similar?

The answer is the Law of Large Numbers (LLN). 

A sample average can be brought as close as the
average in the population from which it is drawn
simply by enlarging the sample.

If the samples are large enough, those in randomly
assigned treatment and control samples will be
similar, because both groups come from the same
population.

#### 8.7) When the difference in group means is biased and not capture the average causal effect?

Unless the treatment variable (T) is randomized, the difference in group means will be upward or downward biased.

Let's assume that for a person $i$ the treatment outcome ($Y_{ti}$) is equal to the control outcome ($Y_{ci}$) plus the causal effect ($\alpha$). 

$$ Y_{ti} = Y_{ci} + \kappa $$ 

Then, the difference in group means is:

$$ E[Y_{ti}|T=1] - E[Y_{ci}|T=0] $$ 

$$ \alpha + E[Y_{ci}|T=1] - E[Y_{ci}|T=0] $$ 

Therefore: 

$$Difference\ in\ group\ means = Average \ causal \ effect + Bias$$ 

If the treatment variable ($T$) is randomized, the outcome variable ($Y$) will be independent of the treatment ($T$).

$$ Y \perp T$$

Consequently, the bias term vanishes:

$$ E[Y_{ci}|T=1] - E[Y_{ci}|T=0] $$

$$ = E[Y_{ci}] - E[Y_{ci}] $$

$$ = 0 $$


#### 8.8) Does association imply causation?

No. Causation can only be
inferred from a randomized experiment. Consumption of ice cream is positive correlated with skin cancer, but consumption of ice cream is not a major factor to cause skin cancer. It looks that sun light increases both the consumption of ice cream and the incidence of skin cancer.

## Exercises

1| In the literature of racial discrimination, there are more than 1000 observational studies for each experimental study. Suppose you read 100 observational studies that indicate that racial discrimination is real. Suppose that you also read 1 experimental study that claims no evidence of racial discrimination. Are you more inclined to accept the result of 100 observational studies or the result of the experimental study? Justify your answer.

2| Interpret the 4 values of the contingency table below. Specifically, state the meaning and compare the values. Argue if there is or not a stronger evidence of racial discrimination.

'race': w = White, and b = Black.

'h': 1 = higher quality curriculum vitae; 0 = lower quality curriculum vitae. This variable was randomized as well.

contingency_table = pd.crosstab(df['race'], df['h'], 
                                values=df['call'], aggfunc='mean')
contingency_table

3| A student is worried about the time she spends in traffic getting to the university. She times the drive for a couple of weeks and finds that it averages 30 minutes.

a) The next day, she tries public transit and it takes 35 minutes. The next day, she's back on the roads, convinced that driving is quicker. Does her decision make sense?

b) If the student decides to do more testing, how should she decide on the mode of transportation? Should she, for example, drive for a week and then take public transit for a week? What advice would you offer?

## Reference

Adhikari, A., DeNero, J. (2020). Computational and Inferential Thinking: The Foundations of Data Science. [Link](https://www.inferentialthinking.com/chapters/intro.html) 

Bertrand, Marianne, and Sendhil Mullainathan. (2004). Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination. American Economic Review, 94 (4): 991-1013.

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 

Lau, S., Gonzalez, J., Nolan, D. (2020). Principles and Techniques of Data Science.  [Link](https://www.textbook.ds100.org/intro)

