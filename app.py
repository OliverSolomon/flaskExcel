from flask import Flask, render_template, url_for, request, send_file
# import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        upload_file = request.files['file-upload']
        upload_file.save(os.path.join('uploads', upload_file.filename))
        return render_template('index.html', message = "Success !")
    return render_template('index.html', message = "Upload")

@app.route('/data')
def data():
    location = './uploads/data-file.xlsx'
    return send_file(location, as_attachment=True)

if __name__ == "__main__":
    app.run(debug = True)