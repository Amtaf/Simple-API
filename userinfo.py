import args as args
from flask import Flask
from flask_restful import Api, Resource, reqparse
from jinja2 import parser

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    return 'Hello World!'


users = [{
    "name": "Flora",
    "age": 21,
    "town": "Moshi"

},
    {
    "name": "Dully",
    "age": 13,
        "town": "Embu"

    },
    {
     "name": "Dada",
     "age": 34,
     "town": "thika"


    }
]
#Api endpoint by defining user resource class


class User(Resource):
    def get(self,name):
        for user in users:
            if name==user["name"]:
                return user, 200
                return "User not found",400

    def post(self, name):
        parser=reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("town")
        args = parser.parse_args()

        for user in users:
          if name == user["name"]:
           return "user with name{} already exists".format(name),400

        user={
          "name":name,
            "age":args["age"],
            "town":args["town"]

        }
        users.append(user)
        return user,201

    def put(self,name):
       parser=reqparse.RequestParser
       parser.add_argument("age")
       parser.add_argument("town")
       args=parser.parse_args()

       for user in users:
        if name == user["name"]:
         user["age"]=args["age"]
        user["town"]=args["town"]
        return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "town": args["town"]
         }

        users.append(user)
        return user, 201

    def delete(self, name,):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name),  200
api.add_resource(User, "/user/<string:name>")


if __name__ == '__main__':
    app.run()
