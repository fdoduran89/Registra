from models.mesa import Mesa

class MesaRepository():
    def get_all(self):
        mesa = []
        for mesa in Mesa.objects:
            mesa.append(mesa)
        return mesa

    def get_by_id(self, id_item):
        return Mesa.objects(Nmesa= id_item).first()
    
    def create(self, content):
        mesa = Mesa(
            Nmesa=content['Nmesa'],
            Ncedulas=content['Ncedulas']
        )
        mesa.save()
        return mesa
    
    def update(self, id_item, content):
        mesa = self.get_by_id(id_item)
        if mesa:
            mesa.update(
                Ncedulas=content.get('Ncedulas', mesa.Ncedulas)
            )
            return mesa
        return None
    
    def delete(self, id_item):
        mesa = self.get_by_id(id_item)
        if mesa:
            mesa.delete()
            return mesa
        return None