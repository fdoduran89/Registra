from flask import Flask
from config import config
import routes.user as re
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_HOST'] = config['MONGO_URI']
db = MongoEngine()
db.init_app(app)

def index():
    return "<h1>Bienvenido al Portal Registraduria Nacional</h1>"

# Routes
app.add_url_rule('/', 'index', index)
app.add_url_rule('/regisNal', 'find_user', re.find_user)
app.add_url_rule('/regisNal/<user_username>', 'find_user', re.find_user)
app.add_url_rule('/regisNal', 'insert_user', re.insert_user, methods= ['POST'])
app.add_url_rule('/regisNal/<user_username>', 'update_user', re.update_user, methods= ['PUT'])
app.add_url_rule('/regisNal/<user_username>', 'delete_user', re.delete_user, methods= ['DELETE'])

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()