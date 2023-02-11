import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify


class EnhanceSpotify():
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = "playlist-modify-public"
        self.sp: Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, scope=self.scope))

        def generate_chatgpt_prompt(self, playlist_url):
            playlist = self.sp.playlist(playlist_url)
            playlist_name = playlist["name"]
            playlist_tracks = playlist["tracks"]["items"]
            playlist_tracks = [track["track"]["name"]
                               for track in playlist_tracks]
            prompt = f"Playlist Name: {playlist_name}\n"
            for track in playlist_tracks:
                prompt += f"{track}\n"
            return prompt

        def enhance(self, playlist_url, create_playlist=True, keep_original_playlist=True):
            original_playlist = self.sp.playlist(playlist_url)


if __name__ == "__main__":
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    redirect_uri = "your_redirect_uri"
    es = EnhanceSpotify(client_id, client_secret, redirect_uri)
    es.enhance(playlist_url="your_playlist_url",
               create_playlist=True, keep_original_playlist=True)
