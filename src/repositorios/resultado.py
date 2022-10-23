from models.resultado import Resultado

class ResultadoRepository():
    # fields: id id_mesa id_partido id_candidato votos
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
        resultado = []
        for res in Resultado.objects:
            resultado.append(res)
        return resultado
    
    def get_by_id(self, id_item):
        return Resultado.objects(id= id_item).first()
        
    def create(self, content):
        resultado = Resultado(
            id_mesa=content['id_mesa'],
            id_partido=content['id_partido'],
            id_candidato=content['id_candidato'],
            votos=content['votos']
        )
        resultado.save()
        return resultado
    
    def update(self, id_item, content):
        resultado = self.get_by_id(id_item)
        if resultado:
            resultado.update(
                id_mesa=content.get('id_mesa', resultado.id_mesa),
                id_partido=content.get('id_partido', resultado.id_partido),
                id_candidato=content.get('id_candidato', resultado.id_candidato),
                votos=content.get('votos', resultado.votos)
            )
            return resultado
        return None
    
    def delete(self, id_item):
        resultado = self.get_by_id(id_item)
        if resultado:
            resultado.delete()
            return resultado
        return None
    
    def get_by_mesa(self, id_mesa):
        resultado = []
        for res in Resultado.objects(id_mesa= id_mesa):
            resultado.append(res)
        return resultado
    
    def get_by_partido(self, id_partido):
        resultado = []
        for res in Resultado.objects(id_partido= id_partido):
            resultado.append(res)
        return resultado
    
    def get_by_candidato(self, id_candidato):
        resultado = []
        for res in Resultado.objects(id_candidato= id_candidato):
            resultado.append(res)
        return resultado
