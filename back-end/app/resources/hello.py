from flask_restful import Resource, reqparse
class Hello(Resource):

  def get(self):

    return 'Hello'