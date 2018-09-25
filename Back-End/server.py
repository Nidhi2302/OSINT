from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from twython import Twython

app = Flask(__name__)
api = Api(app)

CORS(app)


APP_KEY = 'zj1iOwJPtb2hpVmHE0kdjwcv0'
APP_SECRET = '7CnRAw4ar8SxROgYGxqbY6sYgNVSZdOCiPJRkzRupNirzh3FKN'

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()

@app.route("/dashboard")
def hello():
    b=twitter.search(q='python')
    return jsonify(b)

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port=5002)