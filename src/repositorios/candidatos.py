from models.candidatos import Candidato

class CandidatoRepository():
    def __init__(self) -> None:
        super().__init__()
    
    def get_all(self):
        candidato = []
        for candi in Candidato.objects:
            candidato.append(candi)
        return candidato
    
    def get_by_id(self, id_item):
        return Candidato.objects(numberCedula= id_item).first()

    def create(self, content):
        candidato = Candidato(

            numberCedula=content['numberCedula'],
            numberResolucion=content['numberResolucion'],
            nameCandidato=content['nameCandidato'],
            apellidoCandidato=content['apellidoCandidato'] ,
            id_partido=content['id_partido']                    
        )
        candidato.save()
        return candidato
    
    def update(self, id_item, content):
        candidatos = self.get_by_id(id_item)
        if candidatos:
            candidatos.update(
                numberCedula=content.get('numberCedula', candidatos.numberCedula),
                numberResolucion=content.get('numberResolucion', candidatos.numberResolucion),
                nameCandidato=content.get('nameCandidato', candidatos.nameCandidato),
                apellidoCandidato=content.get('apellidoCandidato', candidatos.apellidoCandidato),
                id_partido=content.get('id_partido', candidatos.id_partido)
            )
            return candidatos
        return None
    
    def delete(self, id_item):
        candidatos = self.get_by_id(id_item)
        if candidatos:
            candidatos.delete()
            return candidatos
        return None