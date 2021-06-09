from flask import Flask,request, jsonify
import random   
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.route('/get_number',methods=["GET"])
def lucky_number():
    result = {'number':random.randint(14, 16)}
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
