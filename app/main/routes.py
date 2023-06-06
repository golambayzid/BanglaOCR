# from flask import render_template, request
import os
from os.path import join, dirname, realpath
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from fileinput import filename
from app.main import bp
from app import allowed_file
import cv2
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

UPLOADS_PATH = join(dirname(realpath(__file__)), '..','upload')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.abspath(os.path.join(UPLOADS_PATH, secure_filename(filename))))
            # photo_n = file.filename
    # if request.method == 'POST':  
    #     f = request.files['file']
    #     # f.save(f.filename)  
        #     f.save(os.path.join(f.filename))
            # image = cv2.imread(r'F:\Project\Image2text\test222.jpg')
            # image = cv2.imread(filename)
            # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            #     # Blur and perform text extraction(you can use raw image)
            # thresh = cv2.GaussianBlur(thresh, (3,3), 0)
            image = Image.open(f"F:\\Project\\Image2text\\app\\upload\\{filename}")
            # data = pytesseract.image_to_string(thresh, lang='Bengali', config='--psm 6')
            data = pytesseract.image_to_string(image, lang='Bengali', config='--psm 6')
            return render_template('output.html', data=data)
            # flash ('upload successfully')
            # return render_template('index.html')
    return render_template('index.html')

@bp.route('/application')
def application():
        return render_template('appinfo.html')
    
@bp.route('/me')
def me():
    return render_template('me.html')