# 1) Foundations of Probability

Vitor Kamada

econometrics.methods@gmail.com

Last updated 7-17-2020

#### 1.1) What is the probability of getting a Head (H) or Tail (T), when you flip a coin? 

Let's visualize the concept of mutually exclusive, using Venn diagrams.

First, let's import Python library to draw Venn diagrams.

from matplotlib import pyplot as plt
from matplotlib_venn import venn2

Let's plot the events Head (H) and Tail (T) with respective probabilities:

$$P(H)=\frac{1}{2}$$ 

$$P(T)=\frac{1}{2}$$


venn2( (1/2, 1/2, 0), set_labels = ('Head', 'Tail'))

Disjoint events are mutually exclusive, if they have no outcomes in common.

When you flip a coin, the events Head (H) and Tail (T) are mutually exclusive. 

If $H$ and $T$ are disjoint events, then 

$$ P(H\cup T) = P(H) + P(T) $$

$$ = \frac{1}{2} + \frac{1}{2}$$

$$ = 1 $$

#### 1.2) In a regular deck, what is the probability of getting a diamond card or face card?

For any two events A and B, the probability that one or the other occurs is the sum of the probability minus the probability ot their intersection:

$$ P(A\cup B) = P(A) + P(B) - P(A\cap B) $$



venn2( (10, 9, 3) )

$$ P(\diamondsuit) + P(face\ card) - P(\diamondsuit \cap face\ card)$$

$$ \frac{13}{52} + \frac{12}{52} - \frac{3}{52} $$

13/52 + 12/52 - 3/52

#### 1.3) In a regular deck, is the event getting a heart card independent from the event getting an Ace? 


Two events are independent if the occurrence of one does not affect the chances for the occurrence of the other. 

There is no reason to believe that getting a heart card can affect the probability of getting an Ace, and vice-versa.

Two events A and B are independent if the probability that both A and B occur is the product of the probabilities of the two events:

$$ P(A\cap B) = P(A)\cdot P(B) $$ 

$$ P(\heartsuit \cap Ace) = P(\heartsuit)\cdot P(Ace) $$

$$ \frac{1}{52} = \frac{1}{4}\cdot \frac{1}{13} $$


$P(\heartsuit \cap Ace) = P(Ace\ of\ Hearts) = \frac{1}{52}$

$P(\heartsuit) = \frac{13}{52} = \frac{1}{4}$

$P(Ace) = \frac{4}{52} = \frac{1}{13}$

Therefore, these two events are independent and can be written:

$$ P(\heartsuit) \perp P(Ace)$$

#### 1.4) According with Venn diagram below, events A and B are independent?

venn2( (1/2, 1/2, 0) )

No. Events A and B are dependents.

If I have the information that event A occurred, I know for sure that event B didn't occur, and vice-versa. 

$P(A) = 0.5$ and $P(B) = 0.5$

$$0 = P(A\cap B) \neq P(A)\cdot P(B) = \frac{1}{4}$$

#### 1.5) When P(A|B) = P(A)?

By definition, the probability of event A given that the event B occurs is:

  $$ P(A|B) = \frac{P(A\cap B)}{P(B)}  $$

If A and B are independent, then $P(A\cap B) = P(A)\cdot P(B)$


  $$ P(A|B) = \frac{P(A)\cdot P(B)}{P(B)}  $$

  $$ =P(A)$$

**Intuition**: Knowledge of event B doesn't affect the probability of event A.

#### 1.6) Why do you believe that the probability of getting a Tail in a fair coin is equal to $\frac{1}{2}$?

Probability = Long Run Relative Frequency

The Law of Large Numbers (LLN): The relative frequency of an outcome converges to a number, as the number of observed outcomes increases.

LLN assumes that events are independent.

If you toss a coin thousand of times, the proportion of Tails will be likely closer to $\frac{1}{2}$.

Let's toss a coin 10,000 times and count how many Tails:

import random 
result= []

for toss in range(10000):
   coin = random.choice(['Head', 'Tail']) 
   result.append(coin)

result.count('Tail')

#### 1.7) If a female tests positive for breast cancer, what is the probability that she in fact has cancer? 




The question asked what is the probabilty of a female has breast cancer conditional on she tested positive:


  $$P(Cancer|Test\ Positive) $$

  $$ = \frac{P(Cancer\cap Test  \ Positive)}{P(Test \  Positive)}$$

Based on data from Banks et al. (2004), the probability of a mammography detects cancer is 0.87. Among females without cancer, the probability for a negative result is 0.97. The overall incidence of breast cancer is 0.003. 

We can calculate that:

$$ P(Cancer\cap Test  \ Positive) $$

$$ = P(Cancer)\cdot P(Test \ Positive|Cancer)$$

$$ = 0.003\cdot 0.87 $$ 
$$ = 0.00261 $$

$$ P(No \ Cancer\cap Test \ Negative) $$

$$ = P(No \ Cancer)\cdot P(Test \ Negative\ |No \ Cancer)$$

$$ = 0.997\cdot 0.97 $$ 
$$ = 0.96709 $$

It is easy to organize the information in a table:


|          | Positive | Negative | Total  |
|----------|----------|----------|--------|
|Cancer    | 0.00261  |          | 0.003  |
|No Cancer |          | 0.96709  | 0.997  |
|Total     |          |          |    1   |


We can infer the other values of the table, as the sum of the joint probabilities (inside) is equal to the marginal probability on the border. 


|          | Positive | Negative | Total |
|----------|----------|----------|-------|
|Cancer    | 0.00261  | 0.00039  | 0.003 |
|No Cancer | 0.02991  | 0.96709  | 0.997 |
|Total     | 0.03252  | 0.96748  |    1  |

  $$P(Cancer|Test\ Positive) $$

 $$ = \frac{0.00261}{0.03252}$$

  $$ =0.0803 $$

The probability that a female, who tested positive, has breast cancer is only 8%. This result is counter-intuitive, because humans do not process well events with very low probability. Unless, a person is educated in the probability laws, she might believe that she was cured by a divine force.

## Exercises

1| Disjoint events are not equal independent events. Define in plain English the difference between both concepts.

2| Assume a fair coin: P(H) = 0.5 and P(T) = 0.5. Is the event getting a Tail independent from the event getting a Head? Justify your answer rigorously.

3| Write a code to roll a die 60,000 times and count how many times the face 3 show up.

4| Events A and B are independent. Draw both events, using the function 'venn2'. 

5| Let A = {student is absent} and C = {student has coronavirus}. Decide if each statement is True or False. Justify your choice.

a) If the probability for a student to be absent is greater than the probability for a student has coronavirus, then $P(A|C) > P(C|A)$.

b) The probability that a student has coronavirus when it is known that the student is absent is equal to the probability that a student is absent when it is known that the student has coronavirus.

c) If the probability for a student to be absent is greater than the probability for a student to be sick, then A and C are dependent events.

d) The probability of a student being absent is greater than the probability that the student is absent given that the student has coronavirus.

## Reference

Adhikari, A., Pitman, J. (2020). Probability for Data Science. [Link](http://prob140.org/textbook/README.html) 

Banks, Emily et al. (2004). Influence of personal characteristics of individual women on sensitivity and specificity of mammography in the Million Women Study: cohort study. BMJ (Clinical research ed.) vol. 329,7464: 477. doi:10.1136/bmj.329.7464.477

Diez, D. M., Barr, C. D., Çetinkaya-Rundel, M. (2014). Introductory Statistics with Randomization and Simulation. [Link](https://www.openintro.org/stat/textbook.php?stat_book=isrs) 