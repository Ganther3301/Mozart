import os
from dotenv import load_dotenv

import discord

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( client_id = os.getenv('CLIENT_ID'),
                                               client_secret = os.getenv('CLIENT_SECRET'),
                                               redirect_uri = os.getenv('REDIRECT_URI'),
                                                scope = "playlist-modify-public"))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    msg = message.content.split(" ")
    if len(msg) == 2 and msg[0] == '!add':
        song_id = msg[1]
        tracks = [song_id]
        sp.playlist_add_items("5FZviWMbPvn9o5ldwRKhf0", tracks)
        song_name = sp.track(song_id)['name']
        await message.channel.send(f'Added "{song_name}" successfully!')

client.run(TOKEN)