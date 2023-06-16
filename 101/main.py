# py -m pip install flask
# py -m pip install flask-restful

from flask import Flask
from flask_restful import Resource, Api

app = Flask("minhaAPI")
api = Api(app)

class minhaapp(Resource):
    def get(self):
        return "Hello World - minhaapp!"
        

api.add_resource(minhaapp,'/')

if __name__ == '__main__':
    app.run()