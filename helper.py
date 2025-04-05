import emoji
import pandas as pd
from collections import Counter
from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud
ex=URLExtract()
def lw(df):
  lis=list(df['message'])
  return lis.count('<Media omitted>\n')  


def fetch_states(selected_user,df):
    if selected_user == 'Overall':
        
       num_messages= df.shape[0]
       words=[]
       for message in df['message']:
           words.extend(message.split())   
       num_media=lw(df)
       links=[]
       for message in df['message']:
         links.extend(ex.find_urls(message))
       return num_messages,len(words),num_media,len(links)
    else:
        new_df =df[df['user'] == selected_user]
        num_messages= new_df.shape[0]
        words=[]
        for message in new_df['message']:
           words.extend(message.split()) 
       
        
        #media 
        num_media=lw(new_df)
        #links
        links=[]
        for message in new_df['message']:
         links.extend(ex.find_urls(message))
        return num_messages,len(words),num_media,len(links)
def most_busy_user(df):
  x=df['user'].value_counts().head()
  df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percent'})
  return x,df

def create_wd(selected_user,df):
  if selected_user != 'Overall':
    df =df[df['user'] == selected_user]
  wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
  df_wc =wc.generate(df['message'].str.cat(sep=" "))
  return df_wc
def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df =df[df['user'] == selected_user]
    emojis=[]
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    temp=pd .DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return temp
def timeline(selected_user,df):
  if selected_user != 'Overall':
        df =df[df['user'] == selected_user]
  t=df.groupby(['year','month']).count()['message'].reset_index()
  time=[]
  for i in range(t.shape[0]):
    
    time.append(t['month'][i]+"/"+str(t['year'][i]))
  t['date']=time 
  return t
def daytimeline(selected_user,df):  
  if selected_user != 'Overall':
        df =df[df['user'] == selected_user]
  dme=[]
  dm=df.groupby(['day','month']).count()['message'].reset_index()
  for i in range(dm.shape[0]):
    dme.append(dm['day'][i]+"/"+str(dm['month'][i]))
  dm['dmd']=dme
  return dm
def busy_month(selected_user,df):
  if selected_user != 'Overall':
        df =df[df['user'] == selected_user]
  da=pd.DataFrame(df['month'].value_counts()).reset_index()
  
  return da
  
  
  
    