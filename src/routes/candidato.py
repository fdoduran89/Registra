from flask import jsonify, request, make_response
from controllers.candidato import CandidatoController

candidato_controller = CandidatoController()

# create candidato

def insert_candidato():
    body = request.get_json()
    try:
        candidatos = candidato_controller.get_by_id(body['nameCandidato'])
        if candidatos:
            return make_response({
                'message': 'El candidato' + body['nameCandidato'] + ' Ya está registrado en el sistema'
            }, 400)
        candidato_controller.create(body)
        return make_response({
            'message': 'El candidato' + body['nameCandidato'] + ' ha sido creado satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación del candidato'
        }, 500)

# Find candidatos
def find_candidatos():
    try:
        candidatos = candidato_controller.get_all()
        return make_response(jsonify(candidatos), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de los candidatos'
        }, 500)

# Find candidato
def find_candidato(nameCandidato):
    try:
        candidatos = candidato_controller.get_by_id(nameCandidato)
        if candidatos:
            return make_response(jsonify(candidatos), 200)
        else:
            return make_response({
                'message': 'El candidato' + nameCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del candidato'
        }, 500)

# delete partido
def delete_candidato(nameCandidato):
    try:
        delete = candidato_controller.delete(nameCandidato)
        if delete:
            return make_response({
                'message': 'El candidato' + nameCandidato + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El candidato' + nameCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar el candidato'
        }, 500)

# update candidato
def update_candidato(nameCandidato):
    body = request.get_json()
    try:
        update = candidato_controller.update(nameCandidato, body)
        if update:
            return make_response({
                'message': 'El candidato' + nameCandidato + ' fue actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay candidato con el nombre ' + nameCandidato
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información del candidato'
        }, 500)