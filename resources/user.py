from flask import Flask, request
import uuid
from blocklist import BLOCKLIST
from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SuccessSchema, UserQuerySchema, UserSchema
import hashlib
from flask_jwt_extended import create_access_token, get_jwt, jwt_required

blp = Blueprint("users",__name__, description="Operation on users")

@blp.route("/login")
class UserLogin(MethodView):
    def __init__(self):
        self.db = UserDatabase()

    @blp.arguments(UserSchema)
    def post(self, request_data):
        username = request_data["username"]
        password = hashlib.sha256(request_data["password"].encode('utf-8')).hexdigest()
        user_id = self.db.verify_user(username, password)
        if user_id:
            return {
                "access_token": create_access_token(identity=user_id)
                }
        abort(400, message="Incurrect Username and Password")


@blp.route("/logout")
class UserLogout(MethodView):
   
    @jwt_required()
    def post(self):
        jti =  get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {
            "message":"Successfuly logged out"
        }
       


@blp.route("/user")
class User(MethodView):

    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def get(self, args):
        id = args.get('id')  #args for arguments and .get()if you name the data that what is getting like in this case name?id    
        result =  self.db.get_user(id)
        if result is None:   
            abort(404, message="User does not exist")
        return result
    

    @blp.arguments(UserSchema)
    @blp.response(200, SuccessSchema)
    def post(self, request_data):
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode('utf-8')).hexdigest()
        if self.db.add_user(username, password):
            return {"message": "User Added Succesfully"}, 201
        abort(403, message="User Already exist")

    @blp.response(200, SuccessSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        result = self.db.delete_user(id)
        if result is True:
            return {"message": "User deleted Succesfully"}
        abort(404, message="User Not Found")
 