from flask import Flask,request, jsonify
import random   
from os import getenv

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@35.246.31.22:3306/project2'
@app.route('/get_number',methods=["GET"])
def lucky_number():
    result = {'number':random.randint(14, 17)}
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
