from abc import ABC, abstractmethod
from marshmallow import Schema


class SchemaComponent(ABC, Schema):

    @abstractmethod
    def serialize(self, payload):
        """Dumping"""

        result = self.dump(payload)
        return result

    @abstractmethod
    def deserialize(self, payload):
        """Loading"""

        result = self.load(payload)
        return result
