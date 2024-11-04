from flask import Flask, render_template
import boto3


app = Flask(__name__)

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def delete_all_ec2_instances():
    instances = ec2.describe_instances()
    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    if instance_ids:
        ec2.terminate_instances(InstanceIds=instance_ids)
        return render_template('terminate_all_secices.html', status=f"Terminating instances: {instance_ids}")
    else:
        return render_template('terminate_all_secices.html', status="No EC2 instances to terminate.")

# Function to delete all S3 buckets and their objects
def delete_all_s3_buckets():
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        # Delete all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            object_keys = [obj['Key'] for obj in objects['Contents']]
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': [{'Key': key} for key in object_keys]})
            return render_template('terminate_all_secices.html', status=f"Deleted objects in bucket: {bucket_name}")
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return render_template('terminate_all_secices.html', status=f"Deleted bucket: {bucket_name}")

# Function to delete all transcription jobs
def delete_all_transcription_jobs():
    jobs = transcribe.list_transcription_jobs()
    for job in jobs['TranscriptionJobSummaries']:
        job_name = job['TranscriptionJobName']
        transcribe.delete_transcription_job(TranscriptionJobName=job_name)
        return render_template('terminate_all_secices.html', status=f"Deleted transcription job: {job_name}")

# Function to clear all EC2 instances, S3 buckets, and transcription jobs


@app.route('/')

def clear_all_resources():
    delete_all_ec2_instances()
    delete_all_s3_buckets()
    delete_all_transcription_jobs()
    print("All resources cleared.")
    return render_template('terminate_all_secices.html', status=f"All resources cleared.")
    

if __name__ == '__main__':
    app.run(port=5007)
