from pathlib import Path 
import os
import json
import pandas as pd 
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#creates a stop words list including our own custom words
#work from Alex Taylor
stopwords = nltk.corpus.stopwords.words('english')
additional_stops = ['disaster','hurricane','death','damage']
stopwords.extend(additional_stops)
#set up sentiment analysis
sia = SentimentIntensityAnalyzer()
florencedir = Path('hurricane_florence.2018')
json_files = [pos_json for pos_json in os.listdir(florencedir) if pos_json.endswith('.json')]

df2 = pd.DataFrame(columns=['text', 'created_at'])

dates = []
for file in json_files: 
    with open('hurricane_florence.2018/'+file, 'r') as f:
        try:
            for line in f:
                x = json.loads(line)
                #extracting columns from json files: text, polarity scores, identity, source, and time
                text=(x['text'])
                sent_score= sia.polarity_scores(text)
                identify = (x['id'])
                source =(x['source'])
                time=(x["created_at"])
                row_dict = {'id': identify, 'created_at': time, 'source': source, 'text score': sent_score}
                #creating list withh each column
                dates.append(row_dict)
        except KeyError:
            continue
#sorted data with key lambda
#https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python 
data_sorted2 = sorted(dates, key=lambda x: x['created_at'])
#the time frame was extremely long, so I converted the dataframe to a csv to interpret it faster
df2 = pd.DataFrame(data_sorted2)
df2.to_csv('florencebias.csv', index=False)