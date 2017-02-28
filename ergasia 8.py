#O KODIKAS GRAFTIKE SE PYTHON 2.7.13
import time
import tweepy
from tweepy import OAuthHandler

consumer_key ='11VYM05OMqh44pTkSfTuTHvkh'
consumer_secret ='fdHUbreK2Ysnyuvg1jIPv0CVPGczLE6xhT8PtilTgqhpImIUTg'
access_token ='725954117722607617-eEQCM1BGrOac0kluoqTY63ItCT4Jx8k'
access_secret ='92p5qYvK4XzN1mg8qXYE6u53kBtidvAy8Dl2uACKurOaU'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "Grapse to proto onoma"
user1=raw_input("ONOMA PROTOU: ")
user2=raw_input("ONOMA DEUTEROU: ")
ids1 = []
for page in tweepy.Cursor(api.followers_ids, screen_name=user1,count=200).pages():
    ids1.extend(page)
ids2 = []
for page in tweepy.Cursor(api.followers_ids, screen_name=user2,count=200).pages():
    ids2.extend(page)
for i in range(len(ids1)):
    for j in range(len(ids2)):
        if ids1[i]==ids2[j]:
            print ids1[i]
