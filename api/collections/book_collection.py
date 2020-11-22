from api.helpers.mongodb_helper import MongodbHelper


class BookCollection(MongodbHelper):

    def __init__(self, collection_name):
        super().__init__()
        self._name = collection_name
