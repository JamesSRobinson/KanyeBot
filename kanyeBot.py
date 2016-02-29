helloworld.pyPython

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from Twitter application:
CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# use apis or something to get most recent data on userbase
spotifyUsers = #get users here
tidalUsers = #get users here

# set up kanye user here
kanye = api.get_user('KAYNEDEETS')
kanyeScreenName = kanye.user.screen_name
 
while(true):
    # get the latest tweet
    status = api.user_timeline(['KANYEDEETS'],,, 1,)
    for i in status: 
	message =  "@%s %s Spotify Users VS %s Tidal Users" %(kanye) %(spotifyUsers) %(tidalUsers)
	i = api.update_status(message, i.id) #update with message in response to kanye status
    # repeat every hour, until banned.
    time.sleep(3600)
