from controllers.abstract import CRUDController
from models.partidos import Partido

class PartidoController(CRUDController):
    def __init__(self) -> None:
        super().__init__()
    
    def get_all(self):
        partidos = []
        for partidos in Partido.objects:
            partidos.append(partidos)
        return partidos
    
    def get_by_id(self, id_item):
        return Partido.objects(nombre_partido= id_item).first()
    
    def create(self, content):
        partidos = Partido(
            
            nombre_partido=content['nombre_partido'],
            lema_partido=content['lema_partido']

        )
        partidos.save()
        return partidos
    
    def update(self, id_item, content):
        partidos = self.get_by_id(id_item)
        if partidos:
            partidos.update(
                nombre_partido=content.get('nombre_partido', partidos.nombre_partido),
                lema_partido=content.get('lema_partido', partidos.lema_partido)
            )
            return partidos
        return None
    
    def delete(self, id_item):
        partidos = self.get_by_id(id_item)
        if partidos:
            partidos.delete()
            return partidos
        return None