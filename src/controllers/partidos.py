from controllers.abstract import CRUDController
#from models.partidos import Partido
from repositorios.partidos import PartidoRepository


class PartidoController(CRUDController):
    def __init__(self) -> None:
        self.partidoRepository = PartidoRepository()
    
    def get_all(self):
        return self.partidoRepository.get_all()
    
    def get_by_id(self, id_item):
        return self.partidoRepository.get_by_id(id_item)
    
    def create(self, content):
        return self.partidoRepository.create(content)
    
    def update(self, id_item, content): 
        return self.partidoRepository.update(id_item, content)
    
    def delete(self, id_item):
        return self.partidoRepository.delete(id_item)