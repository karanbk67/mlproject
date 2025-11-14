from flask import Flask,request,render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

application=Flask(__name__)

app=application

## Route for Home 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=Custom