import pandas as pd
import plotly.express as px
import re

#this is for all of dorian hurricane data
dorian = pd.read_csv('dorian.csv')
date_reg = r'<[^>]*>([^<]*)</a>'
dorian['Social Media'] = dorian['source'].str.extract(date_reg)
#found the regex function via true online
#https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html 
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Twitter.*', 'Twitter', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Tweet.*', 'Twitter', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Instagram.*', 'Instagram', regex=True)
dorian['Social Media'] = dorian['Social Media'].str.replace('.*Facebook.*', 'Facebook', regex=True)
counts_dorian = dorian['Social Media'].value_counts().reset_index(name='Count')
#this is for all of florence hurricane data
florence = pd.read_csv('florencebias.csv')
date_reg1 = r'<[^>]*>([^<]*)</a>'
florence['Social Media'] = florence['source'].str.extract(date_reg1)
florence['Social Media'] = florence['Social Media'].str.replace('.*Twitter.*', 'Twitter', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Tweet.*', 'Twitter', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Instagram.*', 'Instagram', regex=True)
florence['Social Media'] = florence['Social Media'].str.replace('.*Facebook.*', 'Facebook', regex=True)
counts_florence = florence['Social Media'].value_counts().reset_index(name='Count')

#found nlargest online to only plot the top five highest
topfive_dorian = counts_dorian.nlargest(5, 'Count')
topfive_florence = counts_florence.nlargest(5, 'Count')
fig = px.bar(topfive_dorian, x='index', y='Count', color='index', title='Hurricane Dorian Media Count')
fig.show()
fig = px.bar(topfive_florence, x='index', y='Count', color='index', title='Hurricane Florence Media Count')
fig.show()
