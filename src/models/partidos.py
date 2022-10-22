import mongoengine as me

class Partido(me.Document):
    
    nombre_partido = me.StringField(required=True)
    lema_partido = me.StringField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)