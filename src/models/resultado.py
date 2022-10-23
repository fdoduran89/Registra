import mongoengine as me

class Resultado(me.Document):
    id_mesa = me.IntField(required=True)
    id_partido = me.IntField(required=True)
    id_candidato = me.IntField(required=True)
    votos = me.IntField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)
