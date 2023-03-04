import plotly.express as px
import pandas as pd
import datetime as dt 
import ast
#dorian hurricane data read from csv previously created
dorian = pd.read_csv('dorian.csv')
#regex finds source after the hyperlink
date_reg = r'<[^>]*>([^<]*)</a>'
#creates new column with the regex extracted using string extract function
dorian['Social Media'] = dorian['source'].str.extract(date_reg)
#these four replacement codes, helps facilitate the accuracy of the major platforms
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Twitter.*', 'Twitter', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Tweet.*', 'Twitter', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Instagram.*', 'Instagram', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Facebook.*', 'Facebook', regex=True)

#this is for all of florence hurricane data and the same code as above
florence = pd.read_csv('florencebias.csv')
date_reg1 = r'<[^>]*>([^<]*)</a>'
florence['Social Media'] = florence['source'].str.extract(date_reg1)
florence['Social Media'] = florence['Social Media'].str.replace('.*Twitter.*', 'Twitter', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Tweet.*', 'Twitter', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Instagram.*', 'Instagram', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Facebook.*', 'Facebook', regex=True)

#introduced apply code with professor and used a definition
def neutral_score(x):
    #Noah Moufarrij created the literal evaluation code
    dictionary = ast.literal_eval(x)
    return dictionary['neu']

#creating dorian list
dorian_sentiment_list = dorian['text score'].apply(neutral_score).tolist()
dorian['Sentiment Score'] = dorian_sentiment_list

#creating florence list
florence_sentiment_list = florence['text score'].apply(neutral_score).tolist()
florence['Sentiment Score'] = florence_sentiment_list

#groupby function is extremely useful to find the mean
#https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.mean.html
dorian_mean = dorian.groupby('Social Media')['Sentiment Score'].mean()
#needed to reset index so merge works
reset_dorian = dorian_mean.reset_index()
#creates a count value of the social media sources
counts_dorian = dorian['Social Media'].value_counts().reset_index(name='Count')
#rename index column to match
counts_dorian = counts_dorian.rename(columns={'index': 'Social Media'})
dorian_merge = counts_dorian.merge(reset_dorian, on='Social Media')
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html 
topfive_dorian = dorian_merge.nlargest(5, 'Count')

#plot dorian
fig_dorian = px.bar(topfive_dorian, x='Social Media', y='Sentiment Score', color="Social Media", title='Dorian Sentiment Scores vs Social Media')
fig_dorian.show()

florence_mean = florence.groupby('Social Media')['Sentiment Score'].mean()
reset_florence = florence_mean.reset_index()
counts_florence = florence['Social Media'].value_counts().reset_index(name='Count')
#rename index column to match
counts_florence = counts_florence.rename(columns={'index': 'Social Media'})
florence_merge = counts_florence.merge(reset_florence, on='Social Media')
topfive_florence = florence_merge.nlargest(5, 'Count')

#plot florence
fig_dorian = px.bar(topfive_florence, x='Social Media', y='Sentiment Score', color="Social Media", 
                    title='Florence Sentiment Scores vs Social Media')
fig_dorian.update_layout(xaxis={'categoryorder': 'array', 'categoryarray':['IFTTT',"SocialNewsDesk","Instagram",'Twitter',"Facebook"]})
fig_dorian.show()