import cv2
import numpy as np
from flask import Flask,render_template,request
import os

#How to upload using flask
#image resize
#display the download
app=Flask(__name__)

# declaring a global variable
img=None

#app.config['IMAGE_PATH']="static"
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload',methods=['GET','POST'])
def upload():
    global img
    #fetch the file
    image=request.files['myfile']
    #print(image.filename)
    image.save(os.path.join("static",image.filename))
    img=cv2.imread("static/" + image.filename)
    return render_template("display.html",filename=image.filename)



@app.route('/resize',methods=['POST'])
def resize():
    width=int(request.form.get('width'))
    height=int(request.form.get('Height'))
    resized=cv2.resize(img,(width,height))
    cv2.imwrite("static/abc.png",resized)
    return '<h4> download <a href="static/abc.png" here</a> Right click here to save</h4>'


@app.route('/flip',methods=['POST'])
def flip():
    flip_num=int(request.form.get('number'))
    flipped=cv2.flip(img,flip_num)
    cv2.imwrite("static/r.png",flipped)
    return '<h4> download <a href="static/r.png" here</a> Right click here to save</h4>'






if __name__=="__main__":
    app.run(debug=True)
