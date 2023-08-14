# pip install google-api-python-client
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
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

    # print(type(response))
    # print(response)

    playlist_ids = [x['id'] for x in response['items']]


    song_request = youtube.playlistItems().list(
        part="snippet",
        maxResults=10,
        playlistId= playlist_ids[0]
    )
    songs_data = song_request.execute()

    print(songs_data)





if __name__ == "__main__":
    main()