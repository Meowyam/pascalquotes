import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("PascalCrossing")\
                                           .setTopTweets(True)\
                                           .setMaxTweets(100)

tweetList = got.manager.TweetManager.getTweets(tweetCriteria)

quoteFile = open("allQuotes.txt", "a")

n = len(tweetList)
for n in tweetList:
    quoteFile.write(n.text)
    quoteFile.write("\n")

quoteFile.close()
