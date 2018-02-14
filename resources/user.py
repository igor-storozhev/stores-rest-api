import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # static method?
    parser = reqparse.RequestParser()   # create parser
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exists"}, 409

        user = UserModel(**data) # because of dict structure key=value
        user.save_to_db()
        return {"message": "User created successfuly."}, 201
