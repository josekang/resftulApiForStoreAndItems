import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("username",
		type = str,
		required = True,
		help = "Please ensure that you have entered the correct information"
		)

	parser.add_argument("password",
		type = str,
		required = True,
		help = "Please ensure that you have entered the correct information"
		)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data["username"]):
			return {"message" : "The username already exists"}, 400

		user = UserModel(**data)
		user.save_to_db()
		return {"message" : "The user has been created successfully"}, 201
		

























