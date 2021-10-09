import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

print(sp.user("txtjt76u4n5m2q0mal1njen5x"))
