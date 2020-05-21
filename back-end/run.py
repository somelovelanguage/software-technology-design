
# # run.py
from flask import Flask
from flask_restful import Api
#flask_doc
from flask_docs import ApiDoc
from flask import Blueprint
# 导入各资源类

from app.resources.hello import Hello
from app.resources.product import Product, Products
from app.resources.nodes import Nodes

app = Flask(__name__)

api = Api(app)
# 生成api文档
app.config['API_DOC_MEMBER']=['hello','products','nodes']
hello = Blueprint('hello','app/resources/hello')
products = Blueprint('products','app/resources/product')
nodes = Blueprint('nodes','app/resources/nodes')
ApiDoc(app)

api.add_resource(Hello,'/api/hello')
api.add_resource(Products, '/api/products/<string:option>')
api.add_resource(Product, '/api/product')
api.add_resource(Nodes, '/api/nodes')


if __name__ == '__main__':

    app.run(port=5000, debug=True)