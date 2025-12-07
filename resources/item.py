from flask import Flask, request
import uuid
from db.items import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemGetSchema, ItemOptionalQuerySchema, ItemQuerySchema, ItemSchema, SuccessSchema
from flask_jwt_extended import jwt_required

blp = Blueprint("items",__name__, description="Operation on items")

@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()
    @jwt_required()
    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self, args):
        print(args)
        id = args.get('id')  #args for arguments and .get()if you name the data that what is getting like in this case name?id    
        if id is None:
            return self.db.get_items()
        else: 
            result =  self.db.get_item(id)
            if result is None:   
                abort(404, message="Record does not exist")
            return result
    
    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data, args):
        id = args.get('id')
        if self.db.update_item(id, request_data):
            return {"message": "Item Updated Succesfully"},200
        abort(404, message="Item Not Found")

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessSchema)
    def post(self, request_data):
        id=uuid.uuid4().hex
        self.db.add_item(id, request_data)
        return {"message": "Item Added Succesfully"}, 201

    @jwt_required()
    @blp.response(200, SuccessSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        result = self.db.delete_item(id)
        if result is True:
            return {"message": "Item deleted Succesfully"}
        abort(404, message="Item Not Found")
