from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from PIL import Image
from pytesseract import*

import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/SIT')
def Hello_sit_world():  # put application's code here
    return 'Hello SIT World!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        filepath = 'C:/Users/park/Desktop/pythonFile'
        # 저장할 경로 지정
        file.save(os.path.join(filepath, filename))

        image =Image.open(filepath + '/' + filename)
        text=image_to_string(image,lang="kor")
        with open("sample.txt","w")as f:
            f.write(text)

        return text



if __name__ == '__main__':
    app.run()
