import sys
import json
from __builtin__ import str
from string import strip

"""
@author: Ankit Patel

Calculates the two happiest states in the United States based on twitter sentiment.
Based on the location where the tweet originated from

Execution: $ python happiest_state.py <sentiment_file> <tweet_file>
"""

#global variable that holds the sentiment analysis for states
#format: {<state> : [<total sentiment score>, <# of tweets from the state>]}
stateSentimentData =  {}

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

statesAbbr = {v:k for k, v in states.items()}


def lines(fp):
    print str(len(fp.readlines()))

'''
Assumes input file is tab-delimited in the format:

<WORD1>    <SentimentScore1>
<WORD2>    <SentimentScore2>
.
.
.
<WORDN>    <SentimentScoreN>

'''
def sentimentScoreFileToDictionary(sentimentFile):
    sentimentScores = {}
    for line in sentimentFile:
        #print line
        term,score = line.split("\t")
        sentimentScores[term] = int(score)
    return sentimentScores

def processTweets(tweet_file, sentimentDic):
    
    global stateSentimentData
    global statesAbbr
    
    for line in tweet_file:
        tweet_json = json.loads(line)
        #print tweet_json
        if('text' in tweet_json and 'place' in tweet_json):         #Valid tweet that has geo location data
            place = tweet_json['place']
            if(type(place) is dict and 'country_code' in place):    #Make sure geo location is valid format
                countryCode = place['country_code'].encode('utf-8')
                if("US" == countryCode):                            #Has to originate from US in order to process
                    #print tweet_json
                    #print place
                    tweet_text_unicode = tweet_json['text']
                    tweet_text = tweet_text_unicode.encode('utf-8')
        #            print tweet_text
                    #PROCESS
                    score = calculateSentimentScore(tweet_text, sentimentDic)   #Get sentiment score

                    #Now we have the score for the tweet, let's figure out what state
                    # the tweet is from
                    #getStateFromTweetIfPossible(countryCode = place['full_name'].encode('utf-8'))
                    state = getStateFromTweet(place)    #Get state
                    if(state in stateSentimentData):
                        currentScore = stateSentimentData[state][0]
                        numTweets = stateSentimentData[state][1]
                        stateSentimentData[state] = [currentScore + score, numTweets + 1]
                    else:
                        stateSentimentData[state] = [score, 1]
    #print stateSentimentData
    #build a dictionary based on sentiment analysis
    meanStateSentiment = {}
    for state in stateSentimentData:
        totalScore = stateSentimentData[state][0]
        numTweets = stateSentimentData[state][1]
        meanStateSentiment[state] = float(totalScore) / float(numTweets)
    
    #print meanStateSentiment
    sorted_stateSentiment = sorted(meanStateSentiment, key=meanStateSentiment.get, reverse=True)   #build a sorted dictionary based on sentiment score
    #print sorted_stateSentiment
    
    #Print the happiest states
    print statesAbbr[sorted_stateSentiment[0]]
    
    """
    numResults = len(sorted_stateSentiment)
    i = len(sorted_stateSentiment)
    while(numResults >0):
        state = sorted_stateSentiment[i-numResults]
        print state + " : " +  str("%.4f" % meanStateSentiment[state])
        numResults= numResults -1
    """    
        
def calculateSentimentScore(tweet_text, sentimentDic):
    
    totalScore = 0
    
    words = tweet_text.split() #split words
#    print "entering calculateSentimentScore with " + tweet_text
#    print words
    for word in words:
        if(word in sentimentDic):
            wordScore = sentimentDic[word]
            totalScore += wordScore
#            print word + " " + str(wordScore) + " " + str(totalScore) 
    return totalScore


'''
Expects place data from the tweet as the input
'''
def getStateFromTweet(placeData):
    location = placeData['full_name'].split(",")
    #print location
    """
    The location may be formatted in two ways
        1. City, State (short abbreviation)
        2. State (full name), USA
    """
    stateOrUSA = location[-1]
    #print stateOrUSA
    
    global states
    
    if len(strip(stateOrUSA)) == 2:
        #we know its a state (short abbreviation)
        return states[strip(stateOrUSA)] #return the full name of the state
    else:
        #we can assume its in the format: State, USA
        return strip(location[0])
    
'''
Main program handler
'''
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    sentimentDic = sentimentScoreFileToDictionary(sent_file)
    #print sentimentDic.items()  #PRINT THE DICTIONARY
    processTweets(tweet_file, sentimentDic)

if __name__ == '__main__':
    main()
