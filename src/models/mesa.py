import mongoengine as me

class Mesa(me.Document):
    Nmesa = me.IntField(required=True)
    Ncedulas = me.IntField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)
