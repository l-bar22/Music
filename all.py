import streamlit as st
import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
from dotenv import load_dotenv
load_dotenv()
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


cid = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

st.title('Music recommendation system')
st.sidebar.title('Music recommendation system')
st.markdown('Tired of listening to the same music all the time? We discover you new songs!'"Try it now!!")
st.sidebar.markdown('Tired of listening to the same music all the time? We discover you new songs!'"Try it now!!")

sentence = st.text_input('Your playlist Id here:')



@st.cache(persist = True)
def analyze_playlist(*args):
    
    
    playlist_features_list = ["artist","track_name","track_id","danceability","energy","key","loudness","mode", "speechiness",'acousticness',"instrumentalness","liveness","valence","tempo", "duration_ms"]
    
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
   
    
    playlist_tracks = sp.playlist_tracks(*args)["items"]
    for track in playlist_tracks:
        
        playlist_features = {}
        
        playlist_features["artist"] = track["track"]["artists"][0]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
    
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[3:]:
            playlist_features[feature] = audio_features[feature]
        
        
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df
    
if sentence:
    st.write(analyze_playlist(sentence))
@st.cache
def load_data(nrows):
    spotify=pd.read_csv('../OUTPUT/spotify.csv')
    spotify.drop(columns=['Unnamed: 0'],inplace=True)
    return spotify


    

@st.cache(persist = True)
def classify_playlist(*args):
    spotify=pd.read_csv('../OUTPUT/spotify.csv')
    spotify.drop(columns=['Unnamed: 0'],inplace=True)
    
    y = spotify['intervals'].values
    X = spotify[['danceability', 'energy',
            'loudness',  'speechiness', 'acousticness',
           'instrumentalness', 'liveness', 'valence']].values
    X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.2)


    forest = RandomForestClassifier(n_estimators=200)
    forest.fit(X_train, y_train)
    tx=p[['danceability', 'energy',
            'loudness',  'speechiness', 'acousticness',
           'instrumentalness', 'liveness', 'valence']].values
    testdata= forest.predict(tx)
    return testdata

p=st.write(analyze_playlist(sentence))


b=st.write(classify_playlist(p))
@st.cache(persist = True)
def recommend(*args):
    spotify=pd.read_csv('../OUTPUT/spotify.csv')
    spotify.drop(columns=['Unnamed: 0'],inplace=True)
    a=spotify.set_index('intervals')
    return a['track_name'].sample(n=50, random_state=1).tolist()

recommend(b)

