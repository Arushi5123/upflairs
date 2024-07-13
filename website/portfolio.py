from flask import Flask,render_template
portfolio = Flask(__name__)
@portfolio.route('/')
def home():
    return render_template('portfolio.html')
@portfolio.route('/Aboutme')
def Aboutme():
    return render_template('Aboutme.html')
@portfolio.route('/Skills')
def Skills():
    return render_template('Skills.html')
@portfolio.route('/Project')
def Project():
    return render_template('Project.html')
@portfolio.route('/Contactme')
def ContactMe():
    return render_template('Contactme.html')
@portfolio.route('/Education')
def Education():
    return render_template('Education.html')
@portfolio.route('/Experience')
def Experience():
    return render_template('Experience.html')
@portfolio.route('/social')
def social():
    return render_template('social.html')
if __name__=="__main__":
    portfolio.run(debug=True)