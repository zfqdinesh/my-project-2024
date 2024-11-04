from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text')
def speech_to_text():
    return render_template('speech_to_text.html')

@app.route('/camera-photo')
def camera_photo():
    return render_template('camera_photo.html')

@app.route('/live-camera')
def live_camera():
    return render_template('live_camera.html')

@app.route('/video-record')
def video_record():
    return render_template('video_record.html')

@app.route('/search-engine')
def search_engine():
    return render_template('search_engine.html')

@app.route('/chatgpt-voice')
def chatgpt_voice():
    return render_template('chatgpt_voice.html')

if __name__ == '__main__':
    app.run(debug=True)
