from flask import Flask,url_for,render_template,request
import joblib
import sqlite3
models=joblib.load('./models/linear_model.lb')
app=Flask(__name__)
data_insert_query = """
insert into project (age,sex,bmi,children,region,smoker,health,prediction)
values(?,?,?,?,?,?,?,?)
"""
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/project')
def contact():
    return render_template('project.html')
@app.route('/prediction', methods=['GET','POST'])#by defaultm get if method not specified
def prediction():
    if request.method=='POST':
        region=request.form['region']
        children=int(request.form['children'])
        health=int(request.form['health'])
        sex=int(request.form['sex'])
        smoker=int(request.form['smoker'])
        age=int(request.form['age'])
        bmi=int(request.form['bmi'])
        if region=="se":
            region_southeast=1
            region_northeast=0
            region_northwest=0
            region_southwest=0
        elif region=="sw":
            region_southeast=0
            region_northeast=0
            region_northwest=0
            region_southwest=1
        elif region=="ne":
            region_southeast=0
            region_northeast=1
            region_northwest=0
            region_southwest=0
        elif region=="nw":
            region_southeast=0
            region_northeast=0
            region_northwest=1
            region_southwest=0
        unseen_data=[[age,sex,bmi,children,smoker,health,region_northeast,region_northwest,region_southeast,region_southwest]]
        prediction=models.predict(unseen_data)[0]
        conn = sqlite3.connect('insurance.db')
        cur = conn.cursor()
        Data = (age,sex,bmi,children,region,smoker,health,prediction)
        cur.execute(data_insert_query,Data)
        print("Your data is inserted into database : ",Data)
        conn.commit()
        cur.close()
        conn.close()
        return render_template('final.html',output=prediction)

       # return str(round(prediction[0],2))
if __name__ == '__main__':
    app.run(debug=True)