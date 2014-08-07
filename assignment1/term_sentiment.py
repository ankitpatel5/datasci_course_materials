import sys
import json
from __builtin__ import str

"""
@author: Ankit Patel

Calculates sentiment score of words not found in AFINN-111.txt based on mean concept:

Each word is given the sentiment of the tweet and the sentiment score accumulates
based on # of tweets the word shows up in. At the end, that score is divided by 
the # of tweets the word showed up in.

Execution: $ python term_sentiment.py <sentiment_file> <tweet_file>
"""

#global variable that holds the sentiment analysis for new words
#format: {<new word> : [<total sentiment score>, <# of tweets it appears in>]}
newWordsDic =  {}

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
    
    global newWordsDic
    
    for line in tweet_file:
        tweet_json = json.loads(line)
        #print tweet_json
        if('text' in tweet_json):
            tweet_text_unicode = tweet_json['text']
            tweet_text = tweet_text_unicode.encode('utf-8')
#            print tweet_text
            #PROCESS
            calculateSentimentScore(tweet_text, sentimentDic)
    
    #Calculate New words sentiment score
    for key in newWordsDic:
        totalScore = newWordsDic[key][0]
        occurances = newWordsDic[key][1]
        finalSentimentScore = float(totalScore/occurances)
        print key + " " + str(finalSentimentScore)

    
def calculateSentimentScore(tweet_text, sentimentDic):
    global newWordsDic
    totalScore = 0
    
    words = tweet_text.split() #split words
#    print "entering calculateSentimentScore with " + tweet_text
#    print words
    wordsNotFound = []
    for word in words:
        if(word in sentimentDic):
            wordScore = sentimentDic[word]
            totalScore += wordScore
        else:
            wordsNotFound.append(word)
        
#    print "Did not find the following words: "
#    print wordsNotFound
    
    #ignore duplicates in word sentiment analysis
    wordSet = set(wordsNotFound)
    wordsNotFound = list(wordSet)   
    
    #Process
    for word in wordsNotFound:
         if(word in newWordsDic):
             currentSentimentScore = newWordsDic[word][0]
             currentNumOfOccurances = newWordsDic[word][1]
#             print "Before: " + word
#             print newWordsDic[word]
             newWordsDic[word] = [currentSentimentScore + totalScore, currentNumOfOccurances+1]
#             print "Tweet score: " + str(totalScore)
#             print "After: " + word
#             print newWordsDic[word]
         else:
            newWordsDic[word] = [totalScore, 1]
#            print "Tweet score: " + str(totalScore)
#            print "New word: " + word
#            print newWordsDic[word]


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
