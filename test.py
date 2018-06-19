import tweepy
import pandas as pd
import numpy as np
import spacy
import geocoder
from collections import Counter
from spacy.attrs import ORTH, LIKE_URL, IS_OOV

################################################
# Natural Language Toolkit: code_suffix_pos_tag
#def pos_features(sentence, i): # [_suffix-pos-tag-fd]
    
#    if i == 0:
 #       features["prev-word"] = "<START>"
#    else:
#        features["prev-word"] = sentence[i-1]
#    return features
#################################################
#################################
## fetched reuters tweets #######
reuterstweets = pd.read_csv("reuterstweets2.csv")
status=reuterstweets["text"]

#Tryiing to make my own selection criteria
#Count_Row=reuterstweets.shape[0] #gives number of row count
#Count_Col=reuterstweets.shape[1] #gives number of col count
#i=0
#for i in xrange(0,Count_Row-1):
#	x=status[i]
#	words=x.split(" ")
#	if "in" in words: 
#  		place_name=words[words.index("in") + 1]
#		print place_name
#	else:
#		print 'There is no in in this sentence.'
###########################
#Using SPACY
attr_ids = [ORTH, LIKE_URL, IS_OOV]
#need to loop or list comprehension through all the tweets
for atweet in xrange(0,20):
	nlp = spacy.load('en')  # load model with shortcut link "en"
	onetweet=status[atweet]       #need to loop through all of them eventually              
	uctweet=onetweet.decode('utf-8') #convert tweet to unicode
	doc=nlp(uctweet)

	#this array is not recording the locations
	doc_array = doc.to_array(attr_ids)                   #the following lines save location results to a np array
#	assert doc_array.shape == (len(doc), len(attr_ids))
#	assert doc[0].orth == doc_array[0, 0]
#	assert doc[1].orth == doc_array[1, 0]
#	assert doc[0].like_url == doc_array[0, 1]
#	assert list(doc_array[:, 1]) == [t.like_url for t in doc]
	
	for location in filter(lambda w: w.ent_type_ == 'GPE', doc):
		print location
		

###########################
#Find latitude and longitude of location using Google's Geocode API or pkg geocode, cause its easier
print doc_array
hash_place = doc_array[:,0]
place=nlp.vocab.strings[hash_place[0]]
print place
for k in xrange(0, hash_place.shape[0]- 1):
	place=nlp.vocab.strings[hash_place[k]]
	uplace=place.decode('utf-8')
	print uplace
	print type(uplace)
	g=geocoder.google(uplace)
	print g.latlng


#write df to json format for globe
#pandas_df = df.toPandas()
#pandas_df.to_json("C:\Users\caroline\Analysis\worldnews\test.JSON")
###########################
#Plot latitude and longitude on WebGL globe ( use pandas to convert to json format first)
# ```javascript
#var data = [
 #   [
  #  'seriesA', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
  #  ],
   # [
   # 'seriesB', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
   # ]
#];
#```











