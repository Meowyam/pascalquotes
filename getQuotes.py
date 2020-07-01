# coding: utf-8

import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("PascalCrossing")\
                                           .setTopTweets(True)\
                                           .setMaxTweets(100)

tweetList = got.manager.TweetManager.getTweets(tweetCriteria)

quoteFile = open("allQuotes.txt", "a")

wrong_punc = ['’', '‘', '…', '—']
fixed_punc = ['\'', '\'', '...', '-']

n = len(tweetList)
for n in tweetList:
    for idx, punc in enumerate(wrong_punc):
        n.text = n.text.replace(punc, fixed_punc[idx])
    quoteFile.write(n.text)
    quoteFile.write("\n")

quoteFile.close()
