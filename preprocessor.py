import re
import pandas as pd 
def preprocess(data):
    pattern ='\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages= re.split(pattern,data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'user_message':messages, 'message_date': dates})
    users= []
    messages =[]
    for message in df['user_message']:
        entry= re.split('([\w\W]+?):\s',message)
        if entry[1:]:
           users.append(entry[1])
           messages.append(entry[2])
        else:
           users.append('group notification')
           messages.append(entry[0])
    df['user']= users
    df['message']= messages
    df=df.drop(columns='user_message')
#print(df.head())
    df['sear']=df['message_date'].str.split(',').str.get(0)
    df['year']=df['sear'].str.split('/').str.get(2)
    df['month']=df['sear'].str.split('/').str.get(1)
    df['day']=df['sear'].str.split('/').str.get(0)
    df['tame']=df['message_date'].str.split(',').str.get(1)
    df['ttime']=df['tame'].str.split('-').str.get(0)
    df= df.drop(columns='tame')
    df= df.drop(columns='sear')
    df= df.drop(columns='message_date')
    df['hour']=df['ttime'].str.split(':').str.get(0)
    df['minute']=df['ttime'].str.split(':').str.get(1)
    return df
    import matplotlib.pyplot as plt
    
    