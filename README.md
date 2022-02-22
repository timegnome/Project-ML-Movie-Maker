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

The data was then cleaned and transformed for use within a machine learning model in azure to predict profit and movie popularity rating.

## Sources ##
Movie data originated from [TMDB](https://www.themoviedb.org/) and [Movielens data](https://movielens.org/) and parsed on demand basis from [boxofficemojo](https://www.boxofficemojo.com/).