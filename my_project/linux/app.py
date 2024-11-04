from flask import Flask, render_template, send_file, abort

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def home():
    return render_template('linux.html')

# Route to handle file download
@app.route('/download')
def download_file():
    try:
        return send_file('linux_code.txt', as_attachment=True)
    except FileNotFoundError:
        abort(404)  # Returns a 404 error if the file is not found

if __name__ == '__main__':
    app.run()
