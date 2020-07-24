def analyze_playlist(*args):
    
    
    playlist_features_list = ["artist","track_name","track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms"]
    
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