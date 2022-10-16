from typing_extensions import Required
import mongoengine as me

class User(me.Document):
    username = me.StringField(required=True)
    password = me.PasswordField(Required=True)
    email = me.EmailField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)