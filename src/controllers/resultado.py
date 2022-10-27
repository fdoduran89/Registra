from controllers.abstract import CRUDController
from repositorios.resultado import ResultadoRepository


class ResultadoController(CRUDController):

    def __init__(self) -> None:
        self.resultadoRepository = ResultadoRepository()

    def get_all(self):
        return self.resultadoRepository.get_all()

    def get_by_id(self, id_item):
        return self.resultadoRepository.get_by_id(id_item)

    def create(self, content):
        return self.resultadoRepository.create(content)

    def update(self, id_item, content):
        return self.resultadoRepository.update(id_item, content)

    def delete(self, id_item):
        return self.resultadoRepository.delete(id_item)

    def get_by_mesa(self, id_item):
        return self.resultadoRepository.get_by_mesa(id_item)
    
    # def get_by_partido(self, id_item):
    #     return self.resultadoRepository.get_by_partido(id_item)

    def get_by_candidato(self, id_item):
        return self.resultadoRepository.get_by_candidato(id_item)

    # def get_by_mesa_and_partido(self, id_mesa, id_partido):
    #     return self.resultadoRepository.get_by_mesa_and_partido(id_mesa, id_partido)

    def get_by_mesa_and_candidato(self, id_mesa, id_candidato):
        return self.resultadoRepository.get_sum_mesa_candidato(id_mesa, id_candidato)

    # def get_by_partido_and_candidato(self, id_partido, id_candidato):
    #     return self.resultadoRepository.get_by_partido_and_candidato(id_partido, id_candidato)

    # def get_by_mesa_and_partido_and_candidato(self, id_mesa, id_partido, id_candidato):
    #     return self.resultadoRepository.get_by_mesa_and_partido_and_candidato(id_mesa, id_partido, id_candidato)
