from models.candidatos import Candidato

class CandidatoRepository():
    def __init__(self) -> None:
        super().__init__()
    
    def get_all(self):
        candidato = []
        for candi in Candidato.objects:
            candidato.append(candi)
        return candidato
    
    def create(self, content):
        candidato = Candidato(
            
            numberResolucion = content['numberResolucion'],
            nameCandidato = content['nameCandidato'],
            numberCedula = content['numberCedula']            
        )
        candidato.save()
        return candidato
    
    def update(self, id_item, content):
        candidatos = self.get_by_id(id_item)
        if candidatos:
            candidatos.update(
                numberResolucion = content.get('numberResolucion', candidatos.numberResolucion),
                nameCandidato = content.get('nameCandidato', candidatos.nameCandidato),
                numberCedula = content.get('numberCedula', candidatos.numberCedula)
            )
            return candidatos
        return None
    
    def delete(self, id_item):
        candidatos = self.get_by_id(id_item)
        if candidatos:
            candidatos.delete()
            return candidatos
        return None