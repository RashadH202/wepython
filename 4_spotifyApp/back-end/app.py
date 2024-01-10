# app.py
from flask import Flask, session, redirect, send_from_directory
from flask_session import Session
from flask_cors import CORS  # Import CORS

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

# Spotify authentication setup
cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
auth_manager = spotipy.oauth2.SpotifyOAuth(
    scope='user-read-currently-playing playlist-modify-private',
    cache_handler=cache_handler,
    show_dialog=True
)

@app.route('/')
def login():
    auth_url = auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')

@app.route('/playlists')
def playlists():
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/login')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify.current_user_playlists()

@app.route('/currently_playing')
def currently_playing():
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/login')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    track = spotify.current_user_playing_track()
    return track if track else "No track currently playing."

@app.route('/current_user')
def current_user():
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/login')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify.current_user()

@app.route('/')
@app.route('/<path:path>')
def serve_static(path='index.html'):
    return send_from_directory('build', path)

if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", 3001)))