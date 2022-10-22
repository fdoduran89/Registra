from controllers.abstract import CRUDController
from repositorios.candidatos import CandidatoRepository


class CandidatoRepository(CRUDController):
    def __init__(self) -> None:
        self.candidatoRepository = CandidatoRepository()
    

    def get_all(self):
        return self.candidatoRepository.get_all
    

    def get_by_id(self, id_item):
        return self.candidatoRepository.get_by_id(id_item)
    

    def create(self, content):
        return self.candidatoRepository.create(content)
    

    def update(self, id_item, content): 
        return self.candidatoRepository.update(id_item, content)
    

    def delete(self, id_item):
        return self.candidatoRepository.delete(id_item)