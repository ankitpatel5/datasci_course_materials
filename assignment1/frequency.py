import sys
import json
from __builtin__ import str

"""
@author: Ankit Patel

Calculates term frequency of all words in all the tweets

Execution: $ python frequency.py <tweet_file>
"""

#global variable that holds the word frequency
#format: {<new word> : <# of occurances>}
termFrequency =  {}
totalWords = 0  #total # of words in all the tweets

def lines(fp):
    print str(len(fp.readlines()))

def processTweets(tweet_file):
    
    global termFrequency
    global totalWords
    
    for line in tweet_file:
        tweet_json = json.loads(line)
        #print tweet_json
        if('text' in tweet_json):
            tweet_text_unicode = tweet_json['text']
            tweet_text = tweet_text_unicode.encode('utf-8')
#            print tweet_text
            #PROCESS
            processText(tweet_text)
    
    #Calculate word frequency
    for key in termFrequency:
        #print "word: " + key + ", " + str(termFrequency[key])
        occurances = termFrequency[key]
        frequency = float(occurances)/float(totalWords)
        print key + " " + str("%0.6f" % frequency)
        #print key + " " + str(frequency)
    #print "Total # of words: " + str(totalWords)
    
def processText(tweet_text):
    global termFrequency
    global totalWords

    words = tweet_text.split() #split words

#    print "entering calculateSentimentScore with " + tweet_text
#    print words
    for word in words:
        #ignore if its empty string
        if(word.strip() != ""):
             word = word.strip()
             totalWords = totalWords + 1
             if(word in termFrequency):
                 termFrequency[word] = termFrequency[word] + 1
             else:
                termFrequency[word] = 1
        


'''
Main program handler
'''
def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    processTweets(tweet_file)

if __name__ == '__main__':
    main()
