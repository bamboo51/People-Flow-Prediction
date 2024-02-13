# Keywords

## Null Hypothesis

In scientific research, the null hypothesis (often denoted $H_{0}$) is the claim that the effect being studied does not exist. Note that the term "effect" here is not meant to imply a causative relationship.

The null hypothesis can also be described as the hypothesis in which no relationship exists between two sets of data or variables being analyzed. If the null hypothesis is true, any experimentally observed effect is due to chance alone, hence the term "null". In contrast with the null hypothesis, an alternative hypothesis is developed, which claims that a relationship does exist between two variables.

### 帰無仮説
帰無仮説（$H_{0}$）とは，“差がない（差は0）”，“関係がない（相関が0）”などの無（＝0）を意味する仮説です．

研究では通常，「運動療法前と比較して一定期間の運動療法後は，筋力が増強する」とか，「患者群の歩行速度は健常群の歩行速度よりも遅い」などの差（違い）を証明します．そのために統計的検定では“運動療法前後でも差がない”とか“患者群と健常群の歩行速度は差がない”などの帰無仮説を想定し，この仮説が成立する有意確率p値を求めます．

有意確率が有意水準よりも小さければ（p<0.05のとき），対立仮説（$H_{1}$）を採択する（差がある）という判断をします．

## p-value
The p value, or probability value, tells you how likely it is that your data could have occurred under the null hypothesis. It does this by calculating the likelihood of your test statistic, which is the number calculated by a statistical test using your data.

The p value tells you how often you would expect to see a test statistic as extreme or more extreme than the one calculated by your statistical test if the null hypothesis of that test was true. The p value gets smaller as the test statistic calculated from your data gets further away from the range of test statistics predicted by the null hypothesis.

The calculation of the p value depends on the statistical test you are using to test your hypothesis:
* Different statistical tests have different assumptions and generate different test statistics. You should choose the statistical test that best fits your data and matches the effect or relationship you want to test.
* The number of independent variables you include in your test changes how large or small the test statistic needs to be to generate the same p value.

### P値
統計学における「仮説検定」（自分が設定した仮説が正しいかどうかを統計的に判定する方法）において、元データの指標が、サンプルから観察された値と等しいか、それよりも大きな（小さな）値をとる確率のこと。P値のPは確率を表すProbabilityのP。

#### 仮説検定におけるP値の計算方法
* 統計的仮説検定の場合は、自分が設定した仮説と反対のことを棄却することで、自分の仮説が正しいことを証明します。
* 例えば、A群の平均値とB群の平均値には「差がある」ことを証明したい場合には、A群の平均値とB群の平均値には「差がない」という仮説をたて、それが間違っていることを証明します。差がないという仮説を棄却することで、差があることを証明するのです。
* P値とは、特定の値になる確率ではなく、それよりも大きくなる確率（実測された差よりも大きな差になる確率）です。その値が小さければ、実測された差よりも大きくなる確率はめったにないため、仮説が棄却されます。**どれぐらい小さい場合に棄却してよいかを決める水準を「有意水準」とよび、一般的には0.05をとることが多いですが、目的に応じて水準を設定する必要があります。**

## Test statistic
A test statistic describes how closely the distribution of your data matches the distribution predicted under the null hypothesis of the statistical test you are using.

The distribution of data is how often each observation occurs, and can be described by its central tendency and variation around that central tendency. Different statistical tests predict different types of distributions, so it’s important to choose the right statistical test for your hypothesis.

The test statistic summarizes your observed data into a single number using the central tendency, variation, sample size, and number of predictor variables in your statistical model.

Generally, the test statistic is calculated as the pattern in your data (i.e., the correlation between variables or difference between groups) divided by the variance in the data (i.e., the standard deviation).

### Example
You are testing the relationship between temperature and flowering date for a certain type of apple tree. You use a long-term data set that tracks temperature and flowering dates from the past 25 years by randomly sampling 100 trees every year in an experimental field.

* **Null hypothesis ($H_{0}$)**: There is no correlation between temperature and flowering date.
* **Alternative hypothesis ($H_{1} \text{or} H_{A}$)**: There is a correlation between temperature and flowering date.

To test this hypothesis you perform a regression test, which generates a t value as its test statistic. The t value compares the observed correlation between these variables to the null hypothesis of zero correlation.

### Types of test statistics
Different statistical tests will have slightly different ways of calculating these test statistics, but the underlying hypotheses and interpretations of the test statistic stay the same.

|Test statistic|Null and alternative hypotheses|Statistical tests that use it|
|:-------------|:------------------------------|:----------------------------|
|t value       |**Null**: The means of two groups are equal <br> **Alternative**: The means of two groups are not equal |  T test <br> Regression tests|
| z value| **Null**: The means of two groups are equal <br> **Alternative**: The means of two groups are not equal | Z test |
|F value| **Null**: The variation among two or more groups is greater than or equal to the variation between the groups <br> **Alternative**: The variation among two or more groups is smaller than the variation between the groups|  ANOVA <br>ANCOVA <br>MANOVA|
$X^{2}$-value|**Null**: Two samples are independent <br> **Alternative**: Two samples are not independent (i.e., they are correlated) | Chi-squared test <br> Non-parametric correlation tests