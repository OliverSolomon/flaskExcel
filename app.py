from flask import Flask, render_template, url_for, request, send_file
import os

from reporter import report

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        upload_file = request.files['file-upload']
        upload_file.save(os.path.join('uploads', upload_file.filename))

        report(upload_file)

        return render_template('index.html', message = "Success !")
    return render_template('index.html', message = "Upload")

@app.route('/data')
def data():
    location = './downloads/report.xlsx'
    return send_file(location, as_attachment=True)

@app.route('/sw.js')
def sw():
    return app.send_static_file('static/sw.js')

if __name__ == "__main__":
    app.run(debug = True)