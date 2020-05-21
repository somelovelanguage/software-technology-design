from flask_restful import Resource, reqparse
from ../models/nodes import nodesModel
class Nodes(Resource):

	def get(self):
		return nodesModel.getNodes()
	def post():
		return "ok"
		