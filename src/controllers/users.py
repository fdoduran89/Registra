from controllers.abstract import CRUDController
from models.users import User

class UserController(CRUDController):
    def __init__(self) -> None:
        super().__init__()
    
    def get_all(self):
        user = []
        for user in User.objects:
            user.append(user)
        return user
    
    def get_by_username(self, user_name):
        return User.objects(username=user_name).first()
    
    def create(self, content):
        user = User(
            username=content['username'],
            password=content['password'],
            email=content['email']
        )
        user.save()
        return user
    
    def update(self, user_name, content):
        user = self.get_by_username(user_name)
        if user:
            user.update(
                username=content.get('username', user.username), 
                email=content.get('email', user.email)
            )
            return user
        return None
    
    def delete(self, user_name):
        user = self.get_by_username(user_name)
        if user:
            user.delete()
            return user
        return None