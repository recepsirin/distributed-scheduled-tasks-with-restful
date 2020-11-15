from abc import ABC, abstractmethod


class SchemaComponent(ABC):

    @abstractmethod
    def serialize(self):
        """Dumping"""
        pass

    @abstractmethod
    def deserialize(self):
        """Loading"""
        pass
