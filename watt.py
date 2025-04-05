import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
st.sidebar.title("Wattsapp chat analyzer by NEXUS ML")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    #st.text(data)
    df =preprocessor.preprocess(data)
    #st.dataframe(df)
    # fetch unique user
    user_list=df['user'].unique().tolist()
   
    user_list.remove('group notification')
    user_list.sort()
    user_list.insert(0,"Overall") 
    selected_user=st.sidebar.selectbox("Show analysis wrt",user_list)
 
 
    if st.sidebar.button("Show analysis"):
      
      num_messages,words,num_media,links=helper.fetch_states(selected_user,df)
      st.title("TOP SATISTICS BY PURAV")
      col1,col2,col3,col4 =st.columns(4)
      
      with col1:
          st.header("Total Messages")
          st.title(num_messages)
      with col2:
          st.header("Total words")
          st.title(words)
      with col3:
          st.header("Media Shared")
          st.title(num_media)
      with col4:
          st.header("links")
          st.title(links)
      
        #monthly timeline
      st.title("Monthly chat analysis")
      timeline=helper.timeline(selected_user,df)
      fig,ax=plt.subplots()
      ax.plot(timeline['date'],timeline['message'],color='orange')
      plt.xticks(rotation='vertical')
      st.pyplot(fig)
      #daily timeline
      st.title("Daily chat analysis")
      dtimeline=helper.daytimeline(selected_user,df)
      fig,ax=plt.subplots()
      ax.plot(dtimeline['dmd'],dtimeline['message'],color='yellow')
      plt.xticks(rotation='vertical')
      st.pyplot(fig) 
      #busy mont analysis
      st.title("Busy month analysis")
      dd=helper.busy_month(selected_user,df)
      fig,ax=plt.subplots()
      ax.bar(dd['month'],dd['count'],color='green')
      
      st.pyplot(fig)
       #finding bussiest user in a group
      if selected_user == 'Overall':
          st.title('Most busy user')
          x,n_df= helper.most_busy_user(df)
          fig,ax=plt.subplots()
         
          col1,col2 = st.columns(2)
          with col1:
              
              ax.bar(x.index,x.values,color='red')
              st.pyplot(fig)
          with col2:
              st.dataframe(n_df)
      #word cloud
      st.title("Word cloud")
      df_wc=helper.create_wd(selected_user,df)
      fig,ax =plt.subplots()
      ax.imshow(df_wc)    
      st.pyplot(fig)
      #emoji analysis
      
      emoji_df=helper.emoji_helper(selected_user,df)
      st.title("Emoji Analysis")
      
      col1,col2 =st.columns(2)
      
      with col1:
          st.dataframe(emoji_df)
      with col2:
          fig,ax=plt.subplots()
          ax.pie(emoji_df[1].head(),labels=emoji_df[1].head(),autopct="%0.2f")
          st.pyplot(fig)
      
      
      
      
      
      