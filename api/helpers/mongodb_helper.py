from pymongo import MongoClient


class MongodbHelper:

    def __init__(self, uri=None, client=None):
        """
        :type uri: str --> your mongodb path
        :type client: str --> database name
        """

        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client[client]

    def create(self, collection=None, inserted_value=None, multiple_insert=False):
        """
        :type collection: str -> collection name
        :type inserted_value: dict -> the value(s) you want to insert
        :type multiple_insert: bool -> set true to active multiple insertion
        """
        if inserted_value is None:
            inserted_value = {}

        if collection is not None:

            if multiple_insert is False:
                self.db[collection].insert_one(inserted_value)
            elif multiple_insert is True:
                self.db[collection].insert_many(inserted_value)
