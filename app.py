from flask import Flask
from flask_prometheus import monitor
import json

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():

    response = {"words": "testing"}
    r = json.dumps(response)
    return r



if __name__ == '__main__':
    monitor(app, port=8000)   # monitor using with prometheus 
    app.run(host='0.0.0.0', port=5000) 
  
