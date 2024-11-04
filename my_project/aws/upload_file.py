from flask import Flask, request, render_template
import boto3
import os

app = Flask(__name__)

# Initialize the S3 client
s3 = boto3.client('s3')

@app.route('/', methods=['GET', 'POST'])

def upload_to_s3():
    if request.method=='POST':
        bucket_name=request.form.get("bucket_name")
        file_path = request.form.get("file_path")
        file_name = os.path.basename(file_path)
        try:
            s3.upload_file(file_path, bucket_name, file_name)
            return render_template('uplode_file.html', status=f"File  {file_name} uploaded to {bucket_name}.")

        except ClientError as e:
            return render_template('uplode_file.html', status=f"Error uploading file: {e}")

    return render_template('uplode_file.html')

if __name__ == '__main__':
    app.run(port=5002)
