# Finger Exercice

- Input knowledge
  - The prior probability of the mushrooms being poisonous is 0.8 (80%)
  - The probability of you being correct in your identification is 0.95 (95%)

- Solution design
  - Let A be the event that the mushrooms are safe to eat, and B be the event that we correctly identify the mushrooms as safe
  - Using Bayes' theorem to calculate the posterior probability of the mushrooms being safe to eat

- Solution
  - $P(A) = 0.2$, prior probability of the mushrooms `being safe`
  - $P(B|A) = 0.95$, probability of you `correctly identifying safe` mushrooms
  - $P(B|\bar{A}) = 0.05$, probability of `incorrectly identifying` poisonous mushrooms as safe
  - Using Bayes' theorem, we can calculate the posterior probability of the mushrooms being safe given that you have identified them as such:

$$P(A|B) = \frac{P(B|A) * P(A)}{P(B)}
= \frac{P(B|A)* P(A)}{P(B|A) *P(A) + P(B|\bar{A})* P(\bar{A})}
= \frac{0.95 *0.2}{0.95* 0.2 + 0.05 * 0.8} = 0.704
$$
  - Law of total probability: $P(B) = P(B|A)*P(A) + P(B|\bar{A})*P(\bar{A})$

- 70.4% of chance that they are actually safe to eat
