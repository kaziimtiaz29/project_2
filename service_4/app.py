from flask import Flask
from flask import redirect, url_for, request, Response, jsonify
import random, requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.route('/prize/<int:number>/<colour>',methods=["POST"])        
def prize_gen(number,colour):
    prize_obtained=""
    if number == 15:
        prize_obtained= "£50"
    else:
        prize_obtained="0"
    return prize_obtained

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)