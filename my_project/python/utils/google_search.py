from flask import Flask, request, render_template
from googlesearch import search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        num_results = request.form.get("num_results", 10)
        query = request.form.get("query", "")
        
        for i, result in enumerate(search(query, num_results=int(num_results)), start=1):
            results.append(f"{i}. {result}")

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(port=5003)
