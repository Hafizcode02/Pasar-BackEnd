from app import app, response
from app.controller import UserController
from app.controller import AuthController
from flask import request, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route ('/')
def index():
    return 'Hello Flask App testing'

@app.route("/user/detail", methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Success')



@app.route('/user', methods= ['GET', 'POST'])
@jwt_required()
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()


@app.route('/user/<id>', methods= ['GET', 'PUT', 'DELETE'])
@jwt_required()
def userDetail(id):
    if request.method == 'GET':
        return UserController.detail(id)
    elif request.method == 'PUT':
        return UserController.edit(id)
    else:
        return UserController.delete(id)
        

@app.route('/login', methods=['POST'])
@jwt_required()
def logins():
   return AuthController.login()