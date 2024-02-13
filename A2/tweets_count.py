from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MongoDB
client= MongoClient("localhost",27017)
# Select database and collection
db = client.test
collection = db.testcollection

pipeline = [{"$match":{"text":{"$regex":"han|hon|den|det|denna|denne|hen","$options":"i"}}},{"$project":{"_id":0, "pronouns":{"$split":["$text"," "]}}},{"$unwind":"$pronouns"},{"$match":{"pronouns":{"$in":["han","hon","den","det","denna","denne","hen"]}}},{"$group":{"_id":"$pronouns","count":{"$sum":1}}},{"$project":{"_id":0,"pronoun":"$_id","count":1}}]

# Perform aggregation
result = list(collection.aggregate(pipeline))

if result:
    print("the pronouns tweets count is")
    for entry in result:
        print(f"{entry['pronoun']} : {entry['count']}")

else:
    print("no output")

#below code is to plot graph for tweetcount
data_frame = pd.DataFrame(result)
#print(data_frame)

x=data_frame['count'].sum()#finding total word account value
percentage=[round((count/x)*100,2) for count in data_frame['count']] #calculating the percentage of each pronoun word count
print(percentage)

plt.figure(figsize=(10,6))
plt.bar(x=data_frame["pronoun"],height=percentage,color='#3B3B98')
plt.xlabel('pronouns tweets')
plt.ylabel('Counts of tweets %')
plt.title('count of tweets in percentage')

for i,j in enumerate(percentage):
    plt.text(i, j + 1, f'{j:.2f}%', ha='center')

plt.savefig('output_tweet_count.png')
plt.show()




