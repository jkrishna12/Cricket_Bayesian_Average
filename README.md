# Overview Bayesian Average

Inspired by this [reddit](https://www.reddit.com/r/Cricket/comments/647njn/bayesian_analysis_of_steve_smiths_average_over/) post where the bayesian average is calculated for different test match batters. The bayesian average of a batter attempts to solve the issues of the classical average used for batters. The formula to work out the classical average is the $\frac{\text{no. runs scored}}{\text{dismissals}}$. Suppose Player1 after 2 innings has scores of 100, 10 resulting in an average of 55. Would this player be better than Player2 who averaged 47 after 50 innings. 

If you were looking purely at their averages you would say so, highlighting the two main issues with the classical average: it doesn't take into account the variance in the scores or the longevity of their career. Using the bayesian method allows us to evaluate the distribution of a players scores and see how much better/worse they are compared to an average players distribution. The prior belief, based of the reddit post, is that a test match batter averages is normally distributed with a mean of 39.15 and a standard deviation 8.78. The prior is then updated with the new average after each dismissal resulting in the new posterior, which also has a normal distribution. 

The data is gathered from [Howstat](http://www.howstat.com/cricket/statistics/players/PlayerProgressBat.asp?PlayerID=3463) and the requests and BeautifulSoup libraries are used to scrape the data into a Pandas dataframe. The technique used to scrape the data from the website was found from this [Medium](https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e) article. Relevant columns are extracted, cleaned and from that variance and standard error are calculated. 

The formulas to calculate the posterior mean and standard deviations (shown later) were found in the 'Bayesian Data Analysis' textbook. The new posterior values are calculated in a for loop. The distributions for the prior, likelihood and posterior are plotted using seaborn and are then animated to see how it changes with each dismissal. Below is an example of the animation produced. The code used for this can be found in the Batters folder
![Adam Voges.gif](https://github.com/jkrishna12/Cricket_Bayesian_Average/blob/main/Adam%20Voges.gif)

# Extending Bayesian Average to Bowlers

To calculate the prior assumption of an average test match bowler we need all the players who have taken a wicket in test match cricket. The data is scraped from ESPNCricinfo's website. To remove outliers only players who have taken more than 50 wickets are included. Seaborn is used to create a histogram of all the bowlers averages. Pingouin is then used to confirm that the distribution is normal. After confirming that it is the mean and standard deviation were calculated, 31.03 and 6.52 respectively. The same process as the batters is used to calculate the bayesian average for the bowlers. The functions used for this can be found in the Bowlers folder

# Using Bayesian Statistics to find the Best Test XI

While this XI is based on the work above if there was an instance where there was no clear standout, I have gone with my own opinion on the player :) 

### Best XI
1. Sunil Gavaskar
2. Matthew Hayden
3. Kumar Sangakarra * (Wk)
4. Steve Smith
5. Sachin Tendulkar
6. Brian Lara
7. Jacques Kallis
8. Shane Warne
9. Curtly Ambrose
10. Glenn Mcgrath
11. Dale Steyn / 	Muthiah Muralidaran

Sunil Gavaskar opened in an era where there no helmets and despite this still has some ridiculous numbers even when compared to modern day players, supported by a bayesian average of 49.44. Partnering him is Matthew Hayden, whose aggressive style would be a nice contrast to Gavaskar's more solid approach. In at 3 is Kumar Sangakarra who possesses a bayesian average of 54.2 a crazy stat for someone coming in first down. Steve Smith is a modern day great having a bayesian average of 55.12, clear of his contemporaries in Test matches. Sachin Tendulkar comes in at 5, can't not have him in and his bayesian of 52.30 supports that. Jacques Kallis at 7 an amazing batter who would provide valuable lower order runs and is also be a solid 4th seamer. His bowling bayesian average is 32.48, slightly higher than average bowler, but is remarkably consistent with a standard error of 1.15. I decided for Shane Warne as my primary spinner despite the fact there are players with a lower bowling bayesian average than him. However, all those players are from the subcontinent and Warne has comparable numbers despite playing mostly on Australian wickets. The pace bowlers will be Curtly Ambrose, a menace with his bounce, Glenn Mcgrath, providing incredible control with a standard error of 1.13 and Dale Steyn with his pace. However, on spinning tracks I would substitute Steyn for Murali. The code used for this can be found in the Best_XI folder.

## Techniques
- Used requests and BeautifulSoup libraries to scrape data from website and turn into a Pandas dataframe
- Cleaned dataframe removing missing/eroneous values
- Performed feature engineering to generate relevant data needed for analysis
- Implemented a bayesian analysis of a normal model with multiple observations
- Matplotlib and Seaborn libraries used to create visualisation of data
- Arviz used to calculate the 90% HDI of the posterior distribution
