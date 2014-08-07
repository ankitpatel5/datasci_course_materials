import sys
import json
from __builtin__ import str

"""
@author: Ankit Patel

Calculates sentiment scores on tweets collected from twitter's public stream

Execution: $ python tweet_sentiment.py AFINN-111.txt output.txt
"""

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
    '''open file to write sentiment results to'''
    resultFileFull = open("tweet_sentiment_results_full.txt","w")

    for line in tweet_file:
        tweet_json = json.loads(line)
        #print tweet_json
        if('text' not in tweet_json):
#            print 'no text'
            #PROCESS
            print "0"
            resultFileFull.write("0\t<Not a tweet>\n")
        else:
            tweet_text_unicode = tweet_json['text']
            tweet_text = tweet_text_unicode.encode('utf-8')
#            print tweet_text
            #PROCESS
            score = calculateSentimentScore(tweet_text, sentimentDic)
            print score
            resultFileFull.write(str(score) + "\t" + tweet_text + "\n")

    '''close the file handlers'''
    resultFileFull.close()
    
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
