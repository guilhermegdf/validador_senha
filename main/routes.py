from .validador import Validador


def initialize_routes(api):
    api.add_resource(Validador, '/')
