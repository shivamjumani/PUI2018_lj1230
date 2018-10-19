Question a) verify that their Null and alternative hypotheses are formulated correctly
    I really like the idea of comparing the usage rate between customers and subscribers. We often think that subscribers will use the service more than random customers do, however, I often doubt if this really is the case. This idea allows a test that would find out if the subscribers really use the service more or not. 
    
    The Original NULL HYPOTHESIS: The proportion of suscriber biking on weekends is the same or higher than the proportion of customer biking on weekends and the Original ALTERNATIVE HYPOTHESIS: The proportion of suscriber biking on weekends is lower than the proportion of customer biking on weekends. The original null hypothesis and the original alternative hypothesis look good. The correct formalt of the formula for null hypothesis and alternative hypothesis were provided as well in markdown format. A significance level alpha = 0.05 is chosen as well. 
    
    Further comments: This is an interesting idea and there can be more than that. A statistics test on weekdays instead of weekends may result in a slightly different results, as there might be more subscribers' trips than customers' trips. 
    
    
Question b) verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

    Before looking at the data, I assume that this test would predominantly focus on counting the trips for different types of users, which are either the customers or subscribers. I see that all the columns have being dropped except user type and date of the trip. There are also steps completed to extract out the correct type of users. These two columns of data along with the separated usertypes should be sufficient for this test. The visualization, which are the graphs, are well made. They allow us to see the huge disparity between the amount of customers' trips and amount of subscribers' trips. The graphs have shown that the necessary steps of data-processing is completed. I like the way that to include the word 'absolute' in 'user absolute count.' The formula used in the graph section, which is about 'customer/subscriber' groupby. count seems alright.  


c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

    According to 'How to choose the right statistical test?' by Barun K Nayak and Avijit Hazra, the groups are unpaired, that is, values in one of the datasets, customers or subscribers, would not be related to or being impacted by the other dataset. This is definitely going to fall under numerical category. I would suggest to use non-parametric tests since we are not quite sure if the data is gonna be in Gaussian distribution. However, parametric tests such as t-test, ANOVA, or F-test seem more practical to think about since we are more familiar with them comparing to non-parametric tests such as Mann-Whitnney U-test or Wilcoxon's rank sum test. In the end, I would suggest a T-test to do the comparison over one variable that we are looking at. 
    
Do not perform the test yet.
Submit a pull request to the original repository to share your markdown.

