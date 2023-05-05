from flask import Flask, render_template, request
from pytube import YouTube
import streamlit as st

if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')


    app = Flask(__name__)

    @app.route('/',methods = ['POST', 'GET'])
    def homepage():
        if request.method == 'POST':
            video_URL = request.form['youtube_url'].replace('watch?v=', 'embed/')
            text = "Abc"
            return render_template('index.html', url=video_URL, transcription = text)
        else:
            url =""
            text=""
            return render_template('index.html', url=url, transcription = text)
        
    app.run(port=8888)