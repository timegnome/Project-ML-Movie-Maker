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

The visualizations of the trends are displayed on the web service on [heroku](https://ml-movie-maker.herokuapp.com/).

The data was then cleaned and transformed for use within a machine learning model in azure to predict profit and movie popularity rating.

## Sources ##
Movie data originated from [TMDB](https://www.themoviedb.org/) and [Movielens data](https://movielens.org/) and parsed on demand basis from [boxofficemojo](https://www.boxofficemojo.com/).