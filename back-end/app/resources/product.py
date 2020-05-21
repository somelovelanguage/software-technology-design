from flask_restful import Resource, reqparse

class Product(Resource):
	
	def delete(self):
	

		return "ok"
	def put(self):	
	

		return "ok"


class Products(Resource):
	
	def get(self,option):
		if option=="sortedproucts":
			return "sortedproucts"
		elif option=="dividedproducts":
			return "dividedproducts"
		elif option=="products":
			return "products"
		elif option=="arrivaltime":
			return "arrivaltime"

		
	def post(self):
		
		return "ok"