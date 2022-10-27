from models.resultado import Resultado
from models.mesa import Mesa
from models.candidatos import Candidato

class ResultadoRepository():
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
        self.check_content_fields(content)
        resultado = Resultado(
            id_mesa= content.get('id_mesa'),
            id_candidato= content.get('id_candidato'),
            votos= content.get('votos')
        )
        resultado.save()
        return resultado
    
    def update(self, id_item, content):
        resultado = self.get_by_id(id_item)
        if resultado:
            resultado.update(
                id_mesa=content.get('id_mesa', resultado.id_mesa),
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
    
    # def get_by_partido(self, id_partido):
    #     resultado = []
    #     for res in Resultado.objects(id_partido= id_partido):
    #         resultado.append(res)
    #     return resultado
    
    def get_by_candidato(self, id_candidato):
        resultado = []
        for res in Resultado.objects(id_candidato= id_candidato):
            resultado.append(res)
        return resultado
    
    def get_sum_mesa_candidato(self, id_mesa, id_candidato):
        resultado = {
            'id_mesa': id_mesa,
            'id_candidato': id_candidato,
            'votos': 0
        }
        self.check_content_fields(resultado)
        for res in Resultado.objects(id_mesa= id_mesa, id_candidato= id_candidato):
            resultado['votos'] += res.votos
        return resultado
    
    def check_content_fields(self, content):
        if not self.mesa_exists(content.get('id_mesa')):
            raise Exception('La mesa no existe')
        if not self.candidato_exists(content.get('id_candidato')):
            raise Exception('El candidato no existe')
        return True

    def mesa_exists(self, id_mesa):
        return Mesa.objects(Nmesa= id_mesa).first() != None
    
    def candidato_exists(self, id_candidato):
        return Candidato.objects(id= id_candidato).first() != None



