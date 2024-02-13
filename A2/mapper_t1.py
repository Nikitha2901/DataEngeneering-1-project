import sys
import json
import fileinput
# input comes from STDIN (standard input)
for line_tweet in fileinput.input():
    try:
        data_tweet = json.loads(line_tweet)#loads the json text into line_tweet
        if "retweeted_status" in  data_tweet: # checking if retweet_status is present 
            continue
         # split the line into words
        text=data_tweet["text"]#assigining text value in jason to a variable text
         # increase counters
        words = text.split()#splitting the text
        tweets = []
        for word in words:
        
            #checking for if pronouns is present in Jason text and also changing them to lowercase to make case insensitive    
            if word.lower() == 'han' or  word.lower() == 'hon' or  word.lower() == 'den' or  word.lower()=='det' or  word.lower()=='denna' or word.lower() =='denne' or word.lower() =='hen':
                if word.lower() not in tweets:
                    tweets.append(word.lower())
                    print(word.lower(),1)
    except:
        continue #if there is a space then it will execute this
