from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    if request.method == 'POST':
        text = request.form.get("text", "")
        filename = 'output.mp3'
        
        # Convert text to audio
        tts = gTTS(text=text, lang='en')
        
        # Save the audio file
        tts.save(filename)

    return render_template('text_to_speak.html', filename=filename)

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5004)
