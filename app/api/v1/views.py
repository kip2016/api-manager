from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from .models import models
import re
import datetime

cart = []
users = []


class Products(Resource):
    # Get all cart entries
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My orders': cart
        }), 200)

    # Add to cart
    def post(self):

        id = len(cart) + 1
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        item = {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }

        cart.append(item)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'My Cart': cart
        }), 201)


class SingleProduct(Resource):
    # Get a single cart entry
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)


class SaleOrder(Resource):
    # Get all sales orders
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My sales': cart
        }), 200)

    # add a sale order
    def post(self):

        id = len(cart) + 1
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        item = {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }

        cart.append(item)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'My Cart': cart
        }), 201)


class SingleSale(Resource):
    # Get a single sale order
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)

my_users_list = models.Users()

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Email and password required"})

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "invalid Username or password"})

        authorize = my_users_list.verify_password(email, password)
        user=my_users_list.get_user_by_email(email)

        if authorize:
            access_token = create_access_token(identity=user)
            return jsonify(token = access_token, message = "Login successful!")
        

class UserRegister(Resource):

    def post(self):
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        role=data.get('role')
        roles=["attendant","admin"]

        if role not in roles:
            return jsonify({"message":"The role {} does not exist".format(role)})
        
        email_format = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if email_format is None:
            return jsonify({"message": "invalid email address"})

        for user in users:
            if(email == user['email']):
                return "user with {} already exist".format(email), 400

        cred = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }
        users.append(cred)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'users': users
        }), 201)


