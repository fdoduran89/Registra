from controllers.abstract import CRUDController
#from models.mesa import Mesa
from repositorios.mesa import MesaRepository

class MesaController(CRUDController):
    def __init__(self):
        self.mesaRepository = MesaRepository()

    
    def get_all(self):
        return self.mesaRepository.get_all()
    
    def get_by_id(self, id_item):
        return self.mesaRepository.get_by_id(id_item)
    
    def create(self, content):
        return self.mesaRepository.create(content)
    
    def update(self, id_item, content):
        return self.mesaRepository.update(id_item, content)
    
    def delete(self, id_item):
        return self.mesaRepository.delete(id_item)