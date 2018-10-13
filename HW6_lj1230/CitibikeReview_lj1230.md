# PUI2018 HW6 Assignment1

## Authors
- Junru Lu

### a. Hypothesis:
- 1.There's no description of alternative hypothesis, which should be: The average tripduration of man using citibike is the lower than the tripduration of woman using citibike.
- 2.The formula can be written better: 
  - _$H_0$_ : $Tripduration_{\mathrm{woman}} - Tripduration_{\mathrm{man}} <= 0 $
  - _$H_1$_ : $Tripduration_{\mathrm{woman}} - Tripduration_{\mathrm{man}} > 0 $

### b. Data:
- According to [CitiBike Data](https://www.citibikenyc.com/system-data), the gender attribute has 3 values: Zero=unknown, 1=male and 2=female. Therefore, for your hypotheses, it is better to drop rows where gender=0 and only focus on gender-known data.

### c. Statistical test:
- Conclusion: Student's t test
- Reason: according to Central limit theorem, the distributions of both female and male's tripdurations should limit to Gaussian distribution. So, we can use Student's t test to test the difference between means of these two samples.

### d. Other suggestion:
- Adding time limits on original hypotheses may lead to a more significant difference
