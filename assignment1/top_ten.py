import sys
import json
from __builtin__ import str

"""
@author: Ankit Patel

Calculates the top ten hashtag mentions from a file of tweets

Execution: $ python top_ten.py <tweet_file>
"""

#global variable that holds the word frequency
#format: {<hashtag word> : <# of occurances>}
hashtagFrequency =  {}

def lines(fp):
    print str(len(fp.readlines()))

"""
Process the tweets to find the top 10 hashtags

NOTE: this function could have been improved for better readability and maintainability if sections of
        the code were refactored into seperate functions
"""
def processTweets(tweet_file):
    
    global hashtagFrequency
    
    for line in tweet_file:
        tweet_json = json.loads(line)
        #print tweet_json
        if('text' in tweet_json):
            tweet_text_unicode = tweet_json['text']
            tweet_text = tweet_text_unicode.encode('utf-8')
#            print tweet_text
            #PROCESS
            if('text' in tweet_json and 'entities' in tweet_json):         #Valid tweet that has entities data
                entities = tweet_json['entities']
                hashtags = entities['hashtags']
                #print entities
                #print hashtags
                if(type(hashtags) is list and len(hashtags) > 0):           #Make sure hashtags has data to process
                    #print tweet_json['text'].encode('utf-8')
                    for data in hashtags:
                        hashtag = data['text'].encode('utf-8')
                        if(hashtag in hashtagFrequency):
                            currentNum = hashtagFrequency[hashtag]
                            hashtagFrequency[hashtag] = currentNum + 1
                            #print hashtagFrequency[hashtag] 
                        else:
                            hashtagFrequency[hashtag] = 1
                            #print hashtagFrequency[hashtag]
    #print hashtagFrequency
    sortedFrequency = sorted(hashtagFrequency, key=hashtagFrequency.get, reverse=True)             
    
    #Print the top 10 hashtags
    #numResults = len(sortedFrequency)
    #i = len(sortedFrequency)
    numResults = 10
    i = 10
    while(numResults >0):
        word = sortedFrequency[i-numResults]
        print word + " " +  str(hashtagFrequency[word])
        numResults= numResults -1


'''
Main program handler
'''
def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    processTweets(tweet_file)

if __name__ == '__main__':
    main()
