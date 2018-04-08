from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return store.json()
        return { 'message': 'Store not found'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return { 'message': 'A store with name {} already exists'.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return { 'message': 'An error occured while creating he store.'}, 500
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            store.delete_from_db()
        return { 'message': 'Store has been deleted'}


class StoreList(Resource):
    def get(self):
        stores = StoreModel.query.all()
        # return { 'stores': [store.json() for store in stores]}
        return { 'stores': list(map(lambda store: store.json(), stores))}