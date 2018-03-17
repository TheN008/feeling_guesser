from __future__ import division
import tweepy
from textblob import TextBlob
import math
import sys

#Authenticating on twitter...
apikey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

auth = tweepy.OAuthHandler(apikey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth)



#Setting up the analyzer class
class Analyzer(object):

	def __init__(self, api, username):

		self.api = api
		self.username = username
		self.user = self.api.get_user(self.username)
		self.user_friends_posts = []
		self.times = 50 # number of posts you want to analyze for each friend
		self.all_polarities = [] #number of polarities for different posts
		self.all_subjectivities = [] #number of subjectivity for different posts
		print "The posts are now being crawled. Might take some time!."
		for friend in self.user.friends(): # this loop is set-up just to work, there has to very much more improvements here
			try:
				friend_user = self.api.user_timeline(friend.screen_name, count=self.times)
			except:
				continue
			for tweet in friend_user:
					try:
						tweet = TextBlob(tweet.text.encode("utf-8"))
						self.all_polarities.append((tweet.sentiment.polarity/1)*100)
						self.all_subjectivities.append((tweet.sentiment.subjectivity/1)*100)
					except:
						continue

	def mean_approach(self):


		def identify_feeling(avg_polarity, avg_subjectivity):

			polarity = ""
			subjectivity = ""
			if avg_polarity>=10:
				polarity = "positive"
			elif avg_polarity<=-10:
				polarity = "negative"
			else:
				polarity = "neutral"
			
			if avg_subjectivity >=10:
				subjectivity = "subjective"
			elif avg_subjectivity <=-10:
				subjectivity = "objective"
			else:
				subjectivity = "neutral"

			return [polarity, subjectivity]

		average_polarity = 0 # average polarity of all 
		average_subjectivity = 0 #average subjectivity of all
		total = 0 # total number of analyzed class
				
		#calculating average of all polarities. Since it's individual series we'll do EX/N 
		
		if len(self.all_polarities) == 0:
			print "No tweets found. exiting..."
			sys.exit(0)
		
		for polarity in self.all_polarities:
			average_polarity += polarity

		average_polarity /= len(self.all_polarities) # MEAN = ΣX/N WHERE N!=0

		for subjectivity in self.all_subjectivities:
			average_subjectivity += subjectivity

		average_subjectivity /= len(self.all_subjectivities) # MEAN = EX/N WHERE N!=0

		return identify_feeling(average_polarity, average_subjectivity)

	def mode_approach(self):
		positive_tweets = 0 # number of positive tweets
		negative_tweets = 0 # number of negative tweets
		neutral_tweets = 0 # number of neutral tweets
		subjective_tweets = 0 # number of subjective tweets
		objective_tweets = 0 # number of objective tweets
		so_neutral_tweets = 0 # number of neutral tweets
		polarity_status = [] # [% of positive tweets, % of negative tweets, % of neither positive nor negative]
		subjectivity_status = [] # [% of subjective tweets, % of objective tweets]

		
		for polarity in self.all_polarities:
			if polarity>10:
				positive_tweets += 1
			elif polarity<-10:
				negative_tweets += 1
			else:
				neutral_tweets += 1

		for subjectivity in self.all_subjectivities:

			if subjectivity>0.1:
				subjective_tweets += 1
			elif subjectivity<0.1:
				objective_tweets += 1

		polarityTweets_sum = positive_tweets + negative_tweets + neutral_tweets # sum of positive, negative and neutral tweets
		positive_tweets /= polarityTweets_sum
		negative_tweets /= polarityTweets_sum
		neutral_tweets /= polarityTweets_sum
		subjectivityTweets_sum  = subjective_tweets + objective_tweets
		subjective_tweets /= subjectivityTweets_sum
		objective_tweets /= subjectivityTweets_sum
		so_neutral_tweets /= subjectivityTweets_sum
		polarity_status.append([round(positive_tweets*100, 2),round(negative_tweets*100, 2),round(neutral_tweets*100, 2)])
		subjectivity_status.append([round(subjective_tweets*100),round(objective_tweets*100)])
		return [polarity_status, subjectivity_status]

	@staticmethod
	def comparePolarity(positive,negative):
		prediction = "positive" if positive > negative else "negative"
		return prediction

username = raw_input("Input the target\n>>>")
approach = raw_input("Input 1 for mode approach and 0 for mean approach\n>>>")
try:
	analyze = Analyzer(api, username)
except tweepy.error.TweepError as e:
	print e.message[0]["message"]
	sys.exit(0)
approach = int(approach)
if approach == 1:
	data = analyze.mode_approach()
	positivePercent = data[0][0][0]
	negativePercent = data[0][0][1]
	subjectivePercent = data[1][0][0]
	objectivePercent = data[1][0][1]
	print("More friends of the user %s have shared %s tweets overall, so %s might also be %s" % (username, analyze.comparePolarity(positivePercent, negativePercent),username, analyze.comparePolarity(positivePercent, negativePercent)))
	
else:
	data = analyze.mean_approach()
	print "%s might be %s and also should like more %s things." % (analyze.username, data[0], data[1])
