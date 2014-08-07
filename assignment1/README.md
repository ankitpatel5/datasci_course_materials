Twitter Sentiment Analysis in Python: Instructions
==================================================

Twitter represents a fundamentally new instrument to make social measurements. Millions of people voluntarily express opinions across any topic imaginable --- this data source is incredibly valuable for both research and business.

For example, researchers have shown that the "mood" of communication on twitter reflects biological rhythms and can even used to predict the stock market. A student here at UW used geocoded tweets to plot a map of locations where "thunder" was mentioned in the context of a storm system in Summer 2012.

Researchers from Northeastern University and Harvard University studying the characteristics and dynamics of Twitter have an excellent resource for learning more about how Twitter can be used to analyze moods at national scale.

In this assignment, you will access the twitter Application Programming Interface(API) using python estimate the public's perception (the sentiment) of a particular term or phrase analyze the relationship between location and mood based on a sample of twitter data Some points to keep in mind:

This assignment is open-ended in several ways. You'll need to make some decisions about how best to solve the problem and implement them carefully.

Problem 1: Get Twitter Data
---------------------------
Simple grabbing data from Twitter's public stream
Problem 2: Derive the sentiment of each tweet
--------------------------------------------
For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. See the file AFINN-README.txt for more information.

Problem 3: Derive the sentiment of new terms
--------------------------------------------
In this part you will be creating a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.


Problem 4: Compute Term Frequency
---------------------------------

Write a Python script frequency.py to compute the term frequency histogram of the livestream data you harvested from Problem 1.

Problem 5: Which State is happiest?
-----------------------------------
Write a Python script happiest_state.py that returns the name of the happiest state as a string.

Your script happiest_state.py should take a file of tweets as input.

There are different ways you might assign a location to a tweet. Here are three:

Use the coordinates field (a part of the place object, if it exists, to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into a state.

Use the other metadata in the place field. Much of this information is hand-entered by the twitter user and may not always be present or reliable, and may not typically contain a state name. 

Use the user field to determine the twitter user's home city and state. This location does not necessarily correspond to the location where the tweet was posted, but it's reasonable to use it as a proxy.

Problem 6: Top ten hash tags
------------------------------

Write a Python script top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered in Problem 1.
