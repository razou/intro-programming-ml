# Hypothesis testing

## History

Ronald Fisher (British statistician), is considered to be (or one of) the pionner of the development of the theory of hypothesis testing the during the 20th century.

*"In the early part of the 20th century, Ronald Fisher developed an approach to
statistical hypothesis testing that has become the most commonly used approach
for evaluating the probability of an observed effect having occurred purely by
chance. Fisher claims to have invented the method in response to a claim by Dr.
Muriel Bristol-Roach that when she drank tea with milk in it she could detect
whether the tea or the milk was poured into the teacup first. Fisher challenged
her to a “tea test” in which she was given eight cups of tea (four for each order of
adding tea and milk), and asked to identify those cups into which the tea had
been poured before the milk. She did this perfectly. Fisher then calculated the
probability of her having done this purely by chance"* 

J. V. Guttag, Introduction to Computation and Programming using Python, Second Edition,  Page 328

## Vocabulary and notation

- **Null hypothesis ($H_0$):** A statement about the population parameter and assuming that there is no significant effect, relationship, or difference. Geneally formulated as an equality (e.g., $μ = μ_0$, where $μ$ is a population parameter and $μ_0$ is a specific value).

- **Alternative hypothesis ($H_a$ or $H_1$):** The assertion ($H_0$ `is False`) that we're trying to find evidence for (i.e, potential effect, relationship, ...). Generally formulated as a statement of inequality or difference (e.g., $μ≠μ_0$, $μ>μ_0$, $μ<μ_0$, ).

- **Type I error:**  Error made by rejecting the null hypothesis ($H_0$) when it's `true`.

- **Type II error:** Failing to reject the null hypothesis when it's `false`.

- **The significance level:** It represents the probability of making a **Type I error**, which is the error of rejecting $H_0$ when it's actually true. Some of common choices are 0.05 (5%) and 0.01 (1%)

- **Critical region (or Value):** The range of values of the test statistic that leads to `rejecting` **$H_0$**. It's determined based on the chosen significance level and the distribution of the test statistic **under $H_0$**.
  - Example: For one-tailed tests (i.e., $H1$ specifies a direction), the critical value is the point beyond which you would reject $H_0$. For two-tailed tests, there are two critical values that define the range of values for rejection.

- **p-value:** The probability of obtaining results as extreme as, or more extreme than, the observed data **under the assumption that $H_0$ is `true`**.
  - A small `p-value` indicates that the observed data is unlikely under the $H_0$.

- **Power of the Test:** The probability of correctly rejecting a false null hypothesis ($H_0$).

- **Effect Size:** A measure of the strength of the relationship or effect being studied.

- **Multiple Comparisons:** Adjusting significance levels when conducting multiple tests to reduce the risk of Type I errors.

- **Non-parametric Tests:** Tests that don't assume specific population distributions.

- **Bayesian Hypothesis Testing:** Incorporating prior beliefs and updating probabilities based on new evidence.

## Process

1. Formulate Hypotheses
   - Define and formulate $H_0$ and $H_1$

2. Select Significance Level ($α$)

3. Collect and Analyze Data
    - Collect a `representative` and `unbiased` sample from the population

4. Choose a Test and Calculate Test Statistic

    - The choice of test depends on the nature of your data and the hypothesis being tested. For example, `t-tests` (when ccomparing means), `chi-squared` ( for categorical data), `ANOVA` (when comparing multiple groups), ...
    - Calculate the test statistic based on the sample data and the chosen test. This statistic quantifies the difference between the sample results and what's expected **under the $H_0$**.

5. Determine Critical Region/Critical Value

6. Calculate P-value

7. Make a Decision

    - If the $p\!-\!value \lt \alpha$, then reject $H_0$.
        - Alternatively, if the test statistic falls within the critical region, we also reject $H_0$.

8. Draw Conclusion(s)

    - If we reject $H_0$, we conclude that there's enough evidence to support $H_1$.
    - If we fail to reject $H_0$, we acknowledge that there is not **enough evidence** to support $H_1$.

9. Interpret Results

    - Put findings into the context of the problem
    - Explain the practical implications of the results and discuss their significance.

    - It's important to note that:
        - Hypothesis testing doesn't prove the truth of $H_0$ or $H_1$; it only helps in assessing the **likelihood of the observed data given the assumptions of $H_0$**.
        - The failure to reject the $H_0$ **does not necessarily** mean the **$H_0$ is true**; it might indicate a **lack of evidence to support $H_1$**

### Beware of P-values

#### English version

- J. V. Guttag, Introduction to Computation and Programming using Python, Second Edition (page 334)

*"The null hypothesis is analogous to a defendant in the Anglo-American
criminal justice system. That system is based on a principle called `presumption
of innocence` i.e., innocent until proven guilty. Analogously, we assume that the
null hypothesis is true unless we see enough evidence to the contrary. In a trial, a
jury can rule that a defendant is “guilty” or “not guilty.” A “not guilty” verdict
implies that the evidence was insufficient to convince the jury that the defendant
was guilty “beyond a reasonable doubt.”. Think of it as equivalent to “guilt was
not proven.” A verdict of “not guilty” does not imply that the evidence was sufficient to convince the jury that the defendant was innocent. And it says nothing
about what the jury would have concluded had it seen different evidence. Think
of a p-value as a jury verdict where the standard “beyond a reasonable doubt”
corresponds to choosing a very small α, and the evidence is the data from which
the t-statistic was constructed"*

*"A small p-value indicates that a particular sample is unlikely if the null hypothesis is true. It is analogous to a jury concluding that it was unlikely that it
would have been presented with this set of evidence if the defendant were innocent, and therefore reaching a guilty verdict. Of course, that doesn’t mean that
the defendant is actually guilty. Perhaps the jury was presented with misleading
evidence. Analogously, a low p-value might be attributable to the null hypothesis
actually being false, or it could simply be that the sample is unrepresentative of
the population from which it is drawn, i.e., the evidence is misleading"*

#### French translation

L'hypothése $H_0$ est analogue à un accusé dans le système judiciare pénale anglo-américain. Ce système repose sur un principe appelé "présomption d'innocence", c'est-à-dire l'innocence jusqu'à preuve du contraire. De manière analogue, nous supposons que l'hypothèse $H_0$ est vraie à moins que nous ne voyions `suffisamment de preuves` du contraire. Lors d'un procès, un jury peut statuer qu'un accusé est **"coupable"** ou **"non coupable"**. Un verdict de **"non coupable"** implique que les preuves étaient **insuffisantes** pour convaincre le jury que l'accusé était coupable "au-delà de tout doute raisonnable". Pensez-y comme équivalent à **"la culpabilité n'a pas été prouvée"**. Un verdict de **"non coupable"** n'implique pas que les preuves étaient suffisantes pour convaincre le jury que l'accusé était innocent. Et cela ne dit rien sur ce que le jury aurait conclu s'il avait vu des preuves différentes. Pensez à une valeur de p comme un verdict de jury où la norme "au-delà de tout doute raisonnable" correspond au choix d'un α très faible, et les preuves sont les données à partir desquelles la statistique t a été construite.

Une petite valeur de la `p-value` indique qu'un échantillon particulier est peu probable si $H_0$ est vraie. Cela est analogue à un jury concluant qu'il était peu probable qu'il aurait été présenté avec cet ensemble de preuves si l'accusé était innocent, et par conséquent prononçant un verdict de culpabilité. Bien sûr, cela ne signifie pas nécessairement que l'accusé est réellement coupable. Peut-être que le jury a été présenté avec des preuves trompeuses. De manière analogue, une faible valeur de la `p-value` pourrait être attribuable au fait que $H_0$ est en réalité fausse, ou cela pourrait simplement être dû au fait que l'échantillon n'est pas représentatif de la population à partir de laquelle il est tiré, c'est-à-dire que les preuves sont trompeuses.

#### Wrap Up

- p-values is not the <span style="color:blue">probability of $H_0$ being true </span>

- Justice Analogy
  - $H_0$ is like <spane style="color:red"> "innocent until proven guilty"</span> in criminal justice.
  - We assume $H_0$ is true until evidence suggests otherwise.

- Trial Analogy
  - In a trial (procès in french), **"not guilty"** doesn't mean **"innocent"** just that guilt wasn't proven beyond doubt.
  - Similarly, rejecting $H_0$ doesn't prove $H_1$.

- P-value as verdict
  - Think of a p-value like a jury's verdict.
  - "Beyond a reasonable doubt" corresponds to a small significance level $\alpha$.
  - Evidence (preuves in french) is the data used to calculate the test statistic.

- Small P-value Interpretation
  - A small p-value suggests that the sample is unlikely under $H_0$.
  - Similar to a jury concluding that evidence is unlikely if the defendant were innocent.

- Limited Conclusions
  - Just as a "guilty" verdict doesn't mean the defendant is guilty, a low p-value doesn't prove the $H_1$.
  - Low p-value might result from actual falseness of $H_0$ or misleading evidence (unrepresentative sample).

- The analogy to the legal system helps emphasize that p-values don't directly provide the probability that a hypothesis is true or false; they reflect <span style="color:red;font-weight:bold" > the strength of evidence against $H_0$ based on the observed data</span>.
