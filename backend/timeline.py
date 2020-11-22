import tweepy
import yaml
from pprint import pprint
import json
import sys
import datetime
import Tweet_classifier as classify

def credentials():
	with open ('config.yml') as f:
		data=yaml.full_load(f.read())
		return data.get("CONSUMER_KEY") , data.get("CONSUMER_SECRET_KEY") , data.get("ACCESS_TOKEN") , data.get("ACCESS_TOKEN_SECRET")


def get_timeline_tweets(screen_name,api):
	all_tweets=list()
	first_chunk=api.user_timeline(screen_name,exclude_replies='True',count=100,tweet_mode='extended')
	all_tweets.extend(first_chunk)
	last_id=int(all_tweets[-1].id)
	for i in range(10):
		#`print(i 'current_chunk')
		current_chunk=api.user_timeline(screen_name,exclude_replies=True,count=100,tweet_mode='extended')
		print(len(current_chunk))
		if(len(current_chunk)>0):
			all_tweets.extend(current_chunk)
			last_id=current_chunk[-1].id
		else:
			break
	return all_tweets

def top_timeline_tweets(screen_name,api):## For the prototype
	return api.user_timeline(screen_name,count=200,exclude_replies=True,tweet_mode='extended')



def clean_hashtags(hashtags):

	cleaned = []
	if len(hashtags) >= 1:
		for i in range(len(hashtags)):
			cleaned.append(hashtags[i].text)        
	return cleaned

def format_created_at(date_str):
	'''
	List of formatted creation time metadata object,
	return ===>	

		[DAY , 
		MONTH , 
		YEAR]
	'''
	datetime_object=(datetime.datetime.strptime(date_str, '%a %b %d %H:%M:%S %z %Y'))
	return [datetime_object.day,datetime_object.month,datetime_object.year]


def user_info(tweet):
	user={

	"screen_name":tweet["user"]["screen_name"],
	"recent_tweet":format_created_at(tweet["created_at"]),
	"joining_date":format_created_at(tweet["user"]["created_at"]),
	"followers_count":tweet["user"]["followers_count"],
	"profile_image_url":tweet["user"]["profile_image_url"],
	"profile_background_image_url":tweet["user"]["profile_background_image_url"],
	"total_likes":tweet["user"]["favourites_count"]
	}
	return user



def create_dict(tweets):
	result = {}
	user=user_info(tweets[0]._json)
	print(len(tweets))
	for i in range(len(tweets)):
		item=tweets[i]._json
		full_text=item["full_text"]
		category=classify.category(item["full_text"])
		print(category)
		unit = {
			"id": item["id_str"],
			'full_text': item["full_text"],
			'created_at': format_created_at(item["created_at"]),
			'favorite_count': item["favorite_count"],
			'retweet_count' : item["retweet_count"]
		}
		if category not in result :
			result.update({category:[unit]})
		else:
			result[category].append(unit)


	category=[]
	for cat in result:
		cur={"name":cat,"count":len(result[cat])}
		arr=result[cat]
		sorted(arr,key=lambda e:(int(e["favorite_count"])+int(e["retweet_count"])))
		cur.update({"to_tweet_id":arr[0]["id"]})
		category.append(cur)
	category=sorted(category,key=lambda e:(int(e["count"])))

	user.update({"category":category})
	return user

def main():
	screen_name='jack'
	consumer_key,consumer_secret,access_token,access_token_secret=credentials()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	tweets=top_timeline_tweets(screen_name,api)


	with open ('sample.json','w') as f:
		json.dump(create_dict(tweets),f)


if __name__ == "__main__":
	main()



# consumer_key,consumer_secret,access_token,access_token_secret=credentials()

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
# timeline=api.user_timeline(screen_name='nasa',exclude_replies='True',count=1000)

# data=list()
# for tweets in timeline:
#     json_object=tweets._json
#     data.append(json_object)
   

# print(len(data)) 


# with open('nasa.json','w')as f:
#     json.dump(data,f)
# first=res[0]
# print(sys.getsizeof(first._json))
# #print(json.dumps((first._json),indent=4))

