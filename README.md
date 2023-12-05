# Overview Bayesian Average

Inspired by this [reddit](https://www.reddit.com/r/Cricket/comments/647njn/bayesian_analysis_of_steve_smiths_average_over/) post where the bayesian average is calculated for different test match batters. The bayesian average of a batter attempts to solve the issues of the classical average used for batters. The formula to work out the classical average is the $\frac{\text{no. runs scored}}{\text{dismissals}}$. Suppose Player1 after 2 innings has scores of 100, 10 resulting in an average of 55. Would this player be better than Player2 who averaged 47 after 50 innings. 

If you were looking purely at their averages you would say so, highlighting the two main issues with the classical average: it doesn't take into account the variance in the scores or the longevity of their career. Using the bayesian method allows us to evaluate the distribution of a players scores and see how much better/worse they are compared to an average players distribution. The prior belief, based of the reddit post, is that a test match batter averages is normally distributed with a mean of 39.15 and a standard deviation 8.78. The prior is then updated with the new average after each dismissal resulting in the new posterior, which also has a normal distribution. 

The data is gathered from [Howstat](http://www.howstat.com/cricket/statistics/players/PlayerProgressBat.asp?PlayerID=3463) and the requests and BeautifulSoup libraries are used to scrape the data into a Pandas dataframe. The technique used to scrape the data from the website was found from this [Medium](https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e) article. Relevant columns are extracted, cleaned and from that variance and standard error are calculated. 

The formulas to calculate the posterior mean and standard deviations (shown later) were found in the 'Bayesian Data Analysis' textbook. The new posterior values are calculated in a for loop. The distributions for the prior, likelihood and posterior are plotted using seaborn and are then animated to see how it changes with each dismissal. Below is an example of the animation produced.
![Adam Voges.gif](https://github.com/jkrishna12/Cricket_Bayesian_Average/blob/main/Adam%20Voges.gif)
## Techniques
- Used requests and BeautifulSoup libraries to scrape data from website and turn into a Pandas dataframe
- Cleaned dataframe removing missing/eroneous values
- Performed feature engineering to generate relevant data needed for analysis
- Implemented a bayesian analysis of a normal model with multiple observations
- Matplotlib and Seaborn libraries used to create visualisation of data
- Arviz used to calculate the 90% HDI of the posterior distribution
