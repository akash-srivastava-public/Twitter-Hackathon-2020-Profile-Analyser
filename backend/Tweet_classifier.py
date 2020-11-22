import requests
import json


def category(text):
	url = ' http://api.datumbox.com/1.0/SentimentAnalysis.json'
	url_classification='http://api.datumbox.com/1.0/TopicClassification.json'
	myobj = {'api_key': '0a9248081701d640261b05545b715276','text':text}
	return requests.post(url_classification, data = myobj).json()["output"]["result"]
