from flask import Response, request
from flask_restful import Resource
from .function import validacao
import json


class Validador(Resource):

    def post(self):
        try:
            data = request.get_json()
            resultado = validacao(data['senha'])
            return Response(json.dumps(resultado), status=200)

        except TypeError:
            return 'Object of type TypeError is not JSON serializable'
