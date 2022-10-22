from flask import Flask
from config import config
import routes.mesa as rm
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_HOST'] = config['MONGO_URI']
db = MongoEngine()
db.init_app(app)

def index():
    return "<h1>Bienvenido al Portal Registraduria Nacional</h1>"

# Routes

#Mesas
app.add_url_rule('/', 'index', index)
app.add_url_rule('/regisNal', 'find_tables', rm.find_tables)
app.add_url_rule('/regisNal/<Nmesa>', 'find_table', rm.find_table)
app.add_url_rule('/regisNal', 'insert_table', rm.insert_table, methods= ['POST'])
app.add_url_rule('/regisNal/<Nmesa>', 'update_table', rm.update_table, methods= ['PUT'])
app.add_url_rule('/regisNal/<Nmesa>', 'delete_table', rm.delete_table, methods= ['DELETE'])

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()