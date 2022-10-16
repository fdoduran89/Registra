from abc import ABC, abstractmethod

class CRUDController(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_username(self, user_name):
        pass

    @abstractmethod
    def create(self, content):
        pass

    @abstractmethod
    def update(self, user_name, content):
        pass

    @abstractmethod
    def delete(self, user_name):
        pass