# Project-ML-Movie-Maker

## Research Topic ##
Analysis of Movie trends and popularity among the masses. 
Movies are a big part of our lives. Whether we watch them to make us laugh, cry, or scream, it is a way for us to distract ourselves from our own problems.
In this project, we will be visiting the trends of movies throughout the past century and see if we can predict the next possible big hit for theaters.

## Processing/Collecting ##
The data provided by TMDB and Movielens was pre-processed and formatted with relational tables.
However, to expaned the scope of the project we moved to gather more movie data and stats from boxofficemojo with the appropriate values for each recent movie.
To do this we used a jupyter notebook and got a basic overview using pandas on the characteristics of the data brought in to find any high level patterns or correlations.
During the processs, using the data provided and cleaned within a jupyter notebook, as well as in tableau,
we determined trends genre and keywords held the highest correlation and impact to the successes of movies throughout the years.
<img src="/FlaskApp/static/assets/images/readme/ML Dataframe.png">

## Visualizations/Presentation ##
Through our analysis on movie trends, we found that many factors in our data did not have any correlation to a success of a movie, monetary or rating level.
In the correlation matrix below many of the genres were relative to the frequency of movies produced over the years, with the exception of *westerns* and *War*.
<img src="/FlaskApp/static/assets/images/readme/Corr DF to Years.png">

However, we can see that the genres that generated the highest profit for movies were **Action**, **Drama**, **Adventure**, and **Comedy**.
<img src= "/FlaskApp/static/assets/images/readme/Genres.png">

Although, we cannot dive more into the cause of these trends, we can assume by the word cloud and the total amount of movies that dramas and comedy's are not very profitable.
However, action and adventure draws in more audiences per movie.
<img src= "/FlaskApp/static/assets/images/readme/Wordcloud.png">
<img src= "/FlaskApp/static/assets/images/readme/Total Movies by Genre.png">

The visualizations of the trends and predictions are displayed in more detail on the web service on [heroku](https://ml-movie-maker.herokuapp.com/).

## Machine Learning Analysis and Models ##

The data was then cleaned and transformed for use within jupyter notebook using pandas before being sent to a machine learning model in azure to predict profit and movie popularity rating.
The cleaned data was then pulled into microsoft azure to develop a machine learning model with an external source not in python.

The goal of predicting the success of a movie, Profit or Rating, was difficualt to do with so many categories and factors.
We limited our predictive training scope of 20 years to date, or the current generation of people, to reflect a more accurate and modern prediction.
By doing so it reduced many of the outliers due to time and genre skew.

Going forward with testing models for predictive scores we attempted to use logistic and linear regression with very low scores and high number of iterations.
This is due to the high amount of variablity in the test data between movies and resulted in a change of models. 

We settled on Random forest and Neural Network models as the machine could find patterns that we could not.
This gave us very low scores in our confusion matrix and didn't predict outputs with data combinations it has not seen very well.

Binning was the solution we approached as an intermintant solution for now. It increased the predictive models scores and reduced the varability in outputs for a more standard prediction.
<img src= "/FlaskApp/static/assets/images/mlprocess/ML Model Process.JPG">

<img src= "/FlaskApp/static/assets/images/mlprocess/Rating Evaluation Stats.JPG">
<img src= "/FlaskApp/static/assets/images/mlprocess/Profit Evaluation Stats.JPG">


## Conclusion ##

Movies have always been a way for people to escape to another world and provide stress relief to those who watch them.
Each movie has so many factors - genres, tags, release dates, that make them successful and profitable. Some of them we did not get to explore
within this project scope. Though it does seem like people don't care about who is making them as long as they enjoy it and that what makes it profitable.
Whether its an action or romance or western or science fiction will effect how much is needed to produce the movie and how much it profits afterwards.

## Sources ##
Movie data originated from [TMDB](https://www.themoviedb.org/) and [Movielens data](https://movielens.org/) and parsed on demand basis from [boxofficemojo](https://www.boxofficemojo.com/).