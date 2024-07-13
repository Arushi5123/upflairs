from flask import Flask,render_template,url_for,request
import pandas as pd
app=Flask(__name__)

#home url"/" ,url or root
@app.route('/')
def home():
    #return "MY HOME PAGE!"
    return render_template('home.html')
@app.route('/contact')# https://127.0.0.1.5000/contact
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/bio')
def bio():
    return render_template('bio.html')
@app.route('/userdata' , methods=['GET','POST'])
def userdata():
    if request.method=='POST':
        user_name=request.form['user_name']
        user_email=request.form['user_email']
        user_message=request.form['user_message']
        
        user_data={'user_name':[user_name],'user_email':[user_email],'user_message':[user_message]}
        #df=pd.DataFrame(user_data)
        #df.to_csv('user_data.csv',index=False)
        #file handling ,pandas
        return user_data
@app.route('/userhello' , methods=['GET','POST'])
def userhello():
    if request.method == 'POST':
        User_Name=request.form['User_Name']
        #User_Data={'User_name':[User_Name]}
        #return f"Hiii {User_Name} welcome to you in upflairs"
        return render_template('render_data.html',User_Name=User_Name)
if __name__=="__main__":
    app.run(debug=True)