from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json(), 200
		return {"message" : "Store Not Found"}, 404

	def post(self, name):
		if StoreModel.find_by_name(name):
			return {"message" : "The store with the name '{}' already exists".format(name)}, 400
		
		store = StoreModel(name)

		try:
			store.save_to_db()
		except :
			return {"message" : "An problem occurred when trying to create the new store"}, 500
		return store.json(), 201

	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
		return {"message" : "Store deleted"}

class StoreList(Resource):
	def get(self):
		return {"stores" : [store.json() for store in StoreModel.query.all()]}, 200
		