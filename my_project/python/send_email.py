from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender_email = os.environ.get('EMAIL_ID')
        email_passwd = os.environ.get('EMAIL_PASSWD')

        receiver_email_id = request.form.get("receiver_email")
        msg = request.form.get("message")

        try:
            # Create SMTP session
            s= smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls()  # Start TLS for security
            s.login(sender_email,email_passwd )  # Replace with your email password

                # Send the mail
            s.sendmail(sender_email, receiver_email_id, msg)

            return render_template('email.html', status="Email sent successfully!")
        
        except Exception as e:
            return render_template('email.html', status=f"Error: {str(e)}")

    return render_template('email.html')

if __name__ == '__main__':
    app.run(port=5001)
