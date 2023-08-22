# pip install google-api-python-client
# **NOTE** ENV VARs
# SPOTIPY_CLIENT_ID=ce6eba2ff071448991c0e6a4eb0d8f3f
# SPOTIPY_REDIRECT_URI=http://localhost:7777/callback
# SPOTIPY_CLIENT_SECRET=f79df155d906449f8947087e4bfbb59c

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import sys

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
scope = "playlist-modify-public"

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    #Initializing Youtube API
    os.environ.get('AIzaSyDdDh-0819yrRpPL9ZHKWpKopiEIAtT0KU')

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    playlist_request = youtube.playlists().list(
        part="snippet",
        maxResults=10,
        mine=True
    )
    response = playlist_request.execute()

    #Gets list of YT Playlist ID [1 for each playist owned by user (mine=True)]
    playlist_ids = [x['id'] for x in response['items']]

    #pulling 10 songs from the 3rd playlist
    #**NOTE** CHANGE max Results for number of songs added
    #**NOTE** Change playlist id number to change which playlist pulling-- [1] is Saved for refference (i think alphabetical)
    song_request = youtube.playlistItems().list(
        part="snippet",
        maxResults=10,
        playlistId= playlist_ids[2]
    )
    songs_data = song_request.execute()

  
    ##SPOTIFY API USING SPOTIPY
    songs_list = []
    filtered_songs_list = []

    #LIST OF WORDS dont want in search
    filler_words = ['free', 'official', 'music', 'video']
    for i in songs_data['items']:
        songs_list.append(i['snippet']['title'])
        print(i['snippet']['title'])

    for item in reversed(songs_list):
        if "Private video" not in item:
            for filler_word in filler_words:
                item = item.lower().replace(filler_word, "")
            filtered_songs_list.append(item)
    print(filtered_songs_list)



    songs = [] 

    #Create playlist title poopi
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, 'poopi')

    # add songs to the new playlist
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    for track_name in filtered_songs_list:
        result = sp.search(track_name)
        songs.append(result['tracks']['items'][0]['uri'])
    sp.playlist_add_items(playlist['id'], songs)





if __name__ == "__main__":
    main()