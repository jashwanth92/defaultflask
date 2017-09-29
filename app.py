from flask import Flask
from flask_pymongo import PyMongo
import json, ast

app = Flask(__name__)

app.config['MONGO_DBNAME'] ='testingmongo'
app.config['MONGO_URI']='mongodb://****************/testingmongo'

mongo = PyMongo(app)


@app.route('/awss',methods =['GET'] )
def addone():
    # GET from mongo
    users = mongo.db.users
    response = users.find_one({},{'_id': False})
    response = ast.literal_eval(json.dumps(response))
    r = json.dumps(response)
    return r



if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port=5000)
