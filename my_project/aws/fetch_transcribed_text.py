from flask import Flask, request, render_template
import boto3
import os
import time
import requests  # For fetching the transcription result

app = Flask(__name__)

transcribe = boto3.client('transcribe')

@app.route('/', methods=['GET', 'POST'])

def fetch_transcription_text():
    if request.method=='POST':

        job_name = request.form.get("job_name")
        response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        status = response['TranscriptionJob']['TranscriptionJobStatus']
        if status == 'COMPLETED':
            print("Transcription completed.")
            transcript_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
            # Fetch the transcribed text from the URI
            transcript_response = requests.get(transcript_uri)
            if transcript_response.status_code == 200:
                transcript_data = transcript_response.json()
                return render_template('fetch_transcribed_text.html',status= ("Transcribed text:", transcript_data['results']['transcripts'][0]['transcript']))

                print("Transcribed text:", transcript_data['results']['transcripts'][0]['transcript'])
            else:
                print("Failed to fetch transcription text:", transcript_response.status_code)
        elif status == 'FAILED':
            print("Transcription failed:", response['TranscriptionJob']['FailureReason'])
            return render_template('fetch_transcribed_text.html', status=("Transcription failed:", response['TranscriptionJob']['FailureReason']))

        else:
            return render_template('fetch_transcribed_text.html', status=(f"Job {job_name} is still {status}."))
            print(f"Job {job_name} is still {status}.")

            
    return render_template('fetch_transcribed_text.html')

if __name__ == '__main__':
    app.run(port=5006)
