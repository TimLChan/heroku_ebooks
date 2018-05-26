import csv
f = open('tweets.csv', 'r', encoding='utf-8')
tweets = []
reader = csv.reader(f,quotechar='"')
next(reader)
#for row in reader:
#    tweets.append((row[5]))

thefile = open('tweetdata.csv', 'w')
for row in reader:
    thefile.write("'%s'," % (row[5]))
#with open('filename.text', 'w') as myfile:
#    wr = csv.writer(myfile, delimiter=",",quotechar="'")
#    for val in tweets:
#        wr.writerow([val])
