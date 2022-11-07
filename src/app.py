from flask import Flask
from config import config
import routes.mesa as rm
import routes.partidos as rp
import routes.candidato as rc
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
app.add_url_rule('/regisNal', 'find_tables', rm.find_table, methods= ['GET'])
app.add_url_rule('/regisNal/<Nmesa>', 'find_table', rm.find_table)
app.add_url_rule('/regisNal', 'insert_table', rm.insert_table, methods= ['POST'])
app.add_url_rule('/regisNal/<Nmesa>', 'update_table', rm.update_table, methods= ['PUT'])
app.add_url_rule('/regisNal/<Nmesa>', 'delete_table', rm.delete_table, methods= ['DELETE'])


#partidos
app.add_url_rule('/regisNalP', 'find_partidos', rp.find_partidos)
app.add_url_rule('/regisNalP/<nombre_partido>', 'find_partido', rp.find_partido)
app.add_url_rule('/regisNalP', 'insert_partido', rp.insert_partido, methods= ['POST'])
app.add_url_rule('/regisNalP/<nombre_partido>', 'update_partido', rp.update_partido, methods= ['PUT'])
app.add_url_rule('/regisNalP/<nombre_partido>', 'delete_partido', rp.delete_partido, methods= ['DELETE'])



#candidatos

app.add_url_rule('/regisNalC', 'find_candidato', rc.find_candidato)
app.add_url_rule('/regisNalC/<nameCandidato>', 'find_candidato', rc.find_candidato)
app.add_url_rule('/regisNalC', 'insert_candidato', rc.insert_candidato, methods= ['POST'])
app.add_url_rule('/regisNalC/<numberCedula>', 'update_candidato', rc.update_candidato, methods= ['PUT'])
app.add_url_rule('/regisNalC/<numberCedula>', 'delete_candidato', rc.delete_candidato, methods= ['DELETE'])


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()