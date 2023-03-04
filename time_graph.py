import plotly.express as px
import pandas as pd
import datetime as dt 
import ast
#dorian hurricane data
dorian = pd.read_csv('dorian.csv')
#create a new column absed on the date time
dorian['Day']=pd.to_datetime(dorian['created_at'], errors = "coerce").dt.date

 #this is for all of florence hurricane data
florence = pd.read_csv('florencebias.csv')
florence['Day']=pd.to_datetime(florence['created_at'], errors = "coerce").dt.date

def neutral_score(x):
    dictionary = ast.literal_eval(x)
    return dictionary['neu']

dorian_sentiment_list = dorian['text score'].apply(neutral_score).tolist()
dorian['Sentiment Score'] = dorian_sentiment_list

#creating florence list
florence_sentiment_list = florence['text score'].apply(neutral_score).tolist()
florence['Sentiment Score'] = florence_sentiment_list

dorian_mean = dorian.groupby('Day')['Sentiment Score'].mean()
reset_dorian = dorian_mean.reset_index()
#dorian_merge=dorian_mean.memory_usage
florence_mean = florence.groupby('Day')['Sentiment Score'].mean()
reset_florence = florence_mean.reset_index()

fig_dorian = px.bar(reset_florence, x='Day', y='Sentiment Score', title='Sentiment Scores vs Time')
fig_dorian.show()