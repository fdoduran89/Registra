import mongoengine as me


class Mesa(me.Document):
    N_mesa = me.IntField(required=True)
    N_cedulas = me.IntField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)