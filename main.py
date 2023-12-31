from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'Hello': 'world'}, 200


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
