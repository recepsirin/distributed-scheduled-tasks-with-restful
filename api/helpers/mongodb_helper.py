from pymongo import MongoClient
from pymongo.errors import InvalidName


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

    def retrieve(self, collection=None) -> list:
        """
        :type collection: str -> collection name
        :returns a list of records
        """
        if collection is not None:
            r_list = list()
            for i in self.db[collection].find():
                r_list.append(i)
            return r_list

    def update(self, collection=None, query=None, updated_value=None, multiple_update=False):
        """
        :type collection: str -> collection name
        :type query: dict -> the value(s) you want to update, it's familiar like where clause
        :type updated_value: dict  -> insert the new value(s), it's familiar like set clause
        :type multiple_update: bool -> set true to active multiple update
        """

        if query is None:
            query = {}
        if updated_value is None:
            updated_value = {'$set': {'': ''}}

        try:

            if collection is not None:

                if multiple_update is False:
                    self.db[collection].update(query, updated_value)

                elif multiple_update is True:
                    self.db[collection].update_many(query, updated_value)

        except TypeError:
            print('Inserted valid type please visit the doc')
        except ValueError:
            print('Update cannot be empty')
        except InvalidName:
            print('Collection name cannot be empty')

    def delete(self, collection=None, query=None, multiple_deletion=False):
        """
        :type collection: str -> collection name
        :type query: dict -> the value(s) you want to delete, it's familiar like where clause
        :type multiple_deletion: bool -> set true to active multiple deletion
        :returns the count of deleted items
        """
        if query is None:
            query = {}

        if collection is not None:
            if multiple_deletion is False:
                d_res_count = self.db[collection].delete_one(query)
                return d_res_count.deleted_count

            elif multiple_deletion is True:
                d_res_count = self.db[collection].delete_many(query)
                return d_res_count.deleted_count
