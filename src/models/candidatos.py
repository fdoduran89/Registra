import mongoengine as me

class Candidato(me.Document):
    
    numberCedula = me.IntField(required=True)
    numberResolucion = me.IntField(required=True)
    nameCandidato = me.StringField(required=True)
    apellidoCandidato = me.StringField(required=True)
    
    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)
