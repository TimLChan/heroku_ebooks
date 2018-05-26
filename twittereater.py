import csv
f = open('tweets.csv', 'r', encoding='utf-8')
tweets = []
reader = csv.reader(f,quotechar='"')
next(reader) #get rid of the twitter header


tweetarchive = open('tweetdata.csv', 'w')
for row in reader:
    tweetarchive.write("'%s'," % (row[5]))

