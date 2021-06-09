from flask import Flask
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.route('/colour',methods=["GET"])        
def colour_():
    return random.choice(["black","blue","violet"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)