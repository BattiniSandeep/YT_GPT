from flask import Flask, render_template, request
from pytube import YouTube

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


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)