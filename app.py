from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_csv(file)
            return render_template('index.html', table=df.to_html())
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
