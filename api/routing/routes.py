from ..resources.players import PlayerResource


def initialize_routes(api):
    api.add_resource(PlayerResource, '/api/v1/players')
