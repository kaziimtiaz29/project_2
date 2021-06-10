from flask import Flask, render_template
import requests 
from os import getenv 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI']= getenv('DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@35.246.31.22:3306/project2'
#app.config['SECRET_KEY']=''

db = SQLAlchemy(app) 

class lottery(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    #numbers=db.Column(db.Integer,nullable=False)
    #colours= db.Column(db.String(20),nullable=False)
    Prize=db.Column(db.String(30),nullable=False)

@app.route('/',methods =['GET','POST'])
@app.route('/home',methods =['GET','POST'])
def home():
    number = requests.get('http://number_api:5001/get_number').json()
    colour = requests.get('http://colour_api:5002/colour').text
    items={'num':number,'col':colour}
    prize= requests.post('http://prize_api:5003/prize',json=items).text

    prize_1 = lottery(Prize = prize)

    db.session.add(prize_1)
    db.session.commit()
    all_prizes= lottery.query.order_by(lottery.id.desc()).limit(5).all()
    return render_template("index.html",colours=colour,numbers=number,prize=prize,all_prizes=all_prizes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)