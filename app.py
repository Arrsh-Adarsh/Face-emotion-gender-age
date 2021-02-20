import os
from flask import Flask, render_template, request, redirect, url_for, flash
from webcam import video
from image import image

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def log():
    return render_template('login.html')


# calling function to open webcam
@app.route("/live prediction")
def video_pred():
    video()
    return render_template('index.html')


@app.route("/photoUpload", methods=['GET', 'POST'])
def image_pred():
    # if request.method == 'POST':
    #     if 'file1' not in request.files:
    #         return 'there is no file in form!'
    #     file1 = request.files['file1']
    #     path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    #     file1.save(path)
    #     return 'image uploaded'
    # image()
    # return render_template('index.html')
    return 'This function is not available yet.'


if __name__ == '__main__':
    app.run(debug=True)
