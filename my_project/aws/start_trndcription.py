from flask import Flask, request, render_template
import boto3
import os
import time

app = Flask(__name__)

transcribe = boto3.client('transcribe')

@app.route('/', methods=['GET', 'POST'])

def start_transcription_job():
    if request.method=='POST':
        bucket_name = request.form.get("bucket_name")
        audio_file_name = request.form.get("audio_file_name")
        audio_file_uri = f"s3://{bucket_name}/{audio_file_name}"
        try:
            job_name = 'transcribe-job-' + str(int(time.time()))
            response = transcribe.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={'MediaFileUri': audio_file_uri},
                MediaFormat='mp3',
                LanguageCode='en-US'  # Adjust as needed
            )  
            return render_template('start_transcription.html',status= f"Transcription Job Name: {job_name}")
        except ClientError as e:
            return render_template('start_transcription.html', status=f"Error Transcription: {e}")
        
    return render_template('start_transcription.html')

if __name__ == '__main__':
    app.run(port=5003)
