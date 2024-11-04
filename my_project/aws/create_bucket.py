from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

# Initialize the S3 client
s3 = boto3.client('s3')

@app.route('/', methods=['GET', 'POST'])
def create_bucket():
    if request.method == 'POST':
        bucket_name = request.form.get("bucket_name")
        try:
            response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'})  # Replace with your preferred region
            return render_template('create_bucket.html', status=f"S3 bucket '{bucket_name}' created successfully.")
        except ClientError as e:
            return render_template('create_bucket.html', status=f"Error: {str(e)}")
    return render_template('create_bucket.html')

if __name__ == '__main__':
    app.run(port=5001)
