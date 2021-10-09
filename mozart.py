import os
from dotenv import load_dotenv

from discord.ext import commands

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix = '!')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( client_id = os.getenv('CLIENT_ID'),
                                               client_secret = os.getenv('CLIENT_SECRET'),
                                               redirect_uri = os.getenv('REDIRECT_URI'),
                                                scope = "playlist-modify-public"))

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'add')
async def add(ctx, song_id):
    tracks = [song_id]
    sp.playlist_add_items("5FZviWMbPvn9o5ldwRKhf0", tracks)
    song_name = sp.track(song_id)['name']
    await ctx.send(f'Added "{song_name}" successfully')

bot.run(TOKEN)
