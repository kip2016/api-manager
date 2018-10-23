from flask import Blueprint
from flask_restful import Api, Resource
from .views import Products, SingleProduct,SaleOrder,SingleSale,UserRegister,UserLogin


v1 = Blueprint('blueprint', __name__, url_prefix='/api/v1')

api = Api(v1)

api.add_resource(Products, '/products')
api.add_resource(SingleProduct, '/products/<int:orderID>')
api.add_resource(SaleOrder,'/sales')
api.add_resource(SingleSale,'/sales/<int:orderID>')
api.add_resource(UserRegister,'/register')
api.add_resource(UserLogin,'/login')

