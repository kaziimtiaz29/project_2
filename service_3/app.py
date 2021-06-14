from flask import Flask
import random
from os import getenv
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@35.246.31.22:3306/project2'

@app.route('/colour',methods=["GET"])        
def colour_():
    return random.choice(["pink","blue","violet"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)