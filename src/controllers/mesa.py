from controllers.abstract import CRUDController
from models.mesa import Mesa

class MesaController(CRUDController):
    def __init__(self) -> None:
        super().__init__()
    
    def get_all(self):
        mesa = []
        for mesa in Mesa.objects:
            mesa.append(mesa)
        return mesa
    
    def get_by_id(self, id_item):
        return Mesa.objects(N_mesa= id_item).first()
    
    def create(self, content):
        mesa = Mesa(
            N_mesa=content['N_mesa'],
            N_cedulas=content['N_cedulas']
        )
        mesa.save()
        return mesa
    
    def update(self, id_item, content):
        mesa = self.get_by_id(id_item)
        if mesa:
            mesa.update(
                N_cedulas=content.get('N_cedulas', mesa.N_cedulas)
            )
            return mesa
        return None
    
    def delete(self, id_item):
        mesa = self.get_by_id(id_item)
        if mesa:
            mesa.delete()
            return mesa
        return None