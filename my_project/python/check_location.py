from flask import Flask, render_template
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    coords, location = get_location()
    return render_template('location.html', coords=coords, location=location)

def get_location():
    # Get the current location
    g = geocoder.ip('me')  # 'me' uses your public IP to determine location

    # Extract coordinates and location
    coords = g.latlng
    location = g.address

    return coords, location

if __name__ == '__main__':
    app.run(port=5006)
