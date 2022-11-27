from flask import jsonify, request, make_response
from controllers.partidos import PartidoController

partido_controller = PartidoController()

def insert_partido():
    body = request.get_json()
    try:
        partidos = partido_controller.get_by_nombre(body['nombre_partido'])
        if partidos:
            return make_response({
                'message': 'El partido ' + body['nombre_partido'] + ' Ya está registrado en el sistema'
            }, 400)
        partido_controller.create(body)
        return make_response({
            'message': 'El partido ' + body['nombre_partido'] + ' ha sido creado satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación del partido'
        }, 500)

def find_partidos():
    try:
        partidos = partido_controller.get_all()
        print(partidos)
        return make_response(jsonify(partidos), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de los partidos'
        }, 500)

def find_partido(nombre_partido):
    try:
        partidos = partido_controller.get_by_nombre(nombre_partido)
        if partidos:
            return make_response(jsonify(partidos), 200)
        else:
            return make_response({
                'message': 'El partido' + nombre_partido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del partido'
        }, 500)

def find_partido_by_id(id):
    try:
        partidos = partido_controller.get_by_id(id)
        if partidos:
            return make_response(jsonify(partidos), 200)
        else:
            return make_response({
                'message': 'El partido' + id_partido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del partido'
        }, 500)

def delete_partido(nombre_partido):
    try:
        delete = partido_controller.delete(nombre_partido)
        if delete:
            return make_response({
                'message': 'El partido' + nombre_partido + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El partido' + nombre_partido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar el partido'
        }, 500)

def update_partido(nombre_partido):
    body = request.get_json()
    try:
        update = partido_controller.update(nombre_partido, body)
        if update:
            return make_response({
                'message': 'El partido' + nombre_partido + ' fue actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay partido con el nombre ' + nombre_partido
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información del partido'
        }, 500)
