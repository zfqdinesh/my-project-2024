from flask import Flask, render_template, request
import pyautogui
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get("action")
        steps = request.form.get("steps", type=int)

        if action == 'up':
            volume_up(steps)
        elif action == 'down':
            volume_down(steps)
        elif action == 'mute':
            mute_volume()
        elif action == 'unmute':
            unmute_volume()
        
        return render_template('volume.html', message=f"Executed action: {action}")

    return render_template('volume.html')

def volume_up(steps):
    for _ in range(steps):
        pyautogui.press('volumeup')
        time.sleep(0.1)

def volume_down(steps):
    for _ in range(steps):
        pyautogui.press('volumedown')
        time.sleep(0.1)

def mute_volume():
    pyautogui.press('volumemute')

def unmute_volume():
    pyautogui.press('volumeunmute')

if __name__ == '__main__':
    app.run(port=5005)
