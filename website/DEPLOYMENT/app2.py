from flask import Flask,render_template,url_for,request
import pandas as pd
import joblib
model=joblib.load('linear_regression_model.lb')
app=Flask(__name__)

#home url"/" ,url or root
@app.route('/')
def home():
    return render_template('index.html')
    #return "MY HOME PAGE!"
@app.route('/prediction', methods=['GET','POST']) 
def prediction():
    if request.method=='POST':
        brand=int(request.form['brand_name'])
        owner=int(request.form['owner'])
        kms_driven=int(request.form['kms_driven'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        unseen_data=[[owner,brand,kms_driven,age,power]]
        prediction=model.predict(unseen_data)[0]#passing the data to the model#numpy array
        #flask str,list,int,float,tuple,dict
        prediction
        return str(round(prediction[0],2))
if __name__=="__main__":
    app.run(debug=True)