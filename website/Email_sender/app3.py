from flask import Flask,render_template,url_for,request
import pandas as pd
from email1 import user_email
#from dotenv import load
app=Flask(__name__)

#home url"/" ,url or root
@app.route('/')
def home():
    return render_template('gui.html')
    #return "MY HOME PAGE!"
@app.route('/useremail', methods=['GET','POST']) 
def useremail():
     if request.method=='POST':
         Name=request.form['Name']
         reciever_email=request.form['reciever_email']
         subject=request.form['subject']
         message=request.form['message']
         user_data=[[Name,reciever_email,subject,message]]
         user_email("arushimathur14@gmail.com",reciever_email,"arih cujq pnwb kact",subject,message)
         return render_template('render.html')
if __name__=="__main__":
    app.run(debug=True)