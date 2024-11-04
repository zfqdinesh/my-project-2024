from flask import Flask, request, render_template
from twilio.rest import Client
import os

app = Flask(__name__)

# Load Twilio credentials (consider using environment variables for security)
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_NUMBER')

# Initialize Twilio client
client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def index():
    message_sid = None
    if request.method == 'POST':
        body = request.form.get("body", "")
        to = request.form.get("to", "")
        
        # Send SMS
        message = client.messages.create(
            body=body,
            from_=twilio_number,
            to=to
        )
        message_sid = message.sid

    return render_template('sms.html', message_sid=message_sid)

if __name__ == '__main__':
    app.run(port=5002)
