from flask import Flask
from flask import redirect, url_for, request, Response, jsonify
import random, requests
from os import getenv


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@35.246.31.22:3306/project2'

@app.route('/prize',methods=["GET","POST"])        
def prize_gen():
    number= request.json['num']
    colour = request.json['col']
    
    app.logger.info(number) 
    prize_obtained=""

    if number['number'] == 15:
        prize_obtained= "£70"
    else:
        prize_obtained="0"
    return prize_obtained

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)