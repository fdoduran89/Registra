from flask import jsonify, request, make_response
from controllers.mesa import MesaController

mesa_controller = MesaController()

def insert_table():
    body = request.get_json()
    try:
        mesa = mesa_controller.get_by_id(body['Nmesa'])
        if mesa:
            return make_response({
                'message': 'La mesa N°' + ' Ya está registrada en el sistema'
            }, 400)
        mesa_controller.create(body)
        return make_response({
            'message': 'La mesa N°' + ' ha sido creada satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación de la mesa'
        }, 500)

def find_tables():
    try:
        mesa = mesa_controller.get_all()
        return make_response(jsonify(mesa), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de las mesas'
        }, 500)

def find_table(Nmesa):
    try:
        mesa = mesa_controller.get_by_id(Nmesa)
        if mesa:
            return make_response(jsonify(mesa), 200)
        else:
            return make_response({
                'message': 'La mesa N°' + ' no fue encontrada'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de la mesa'
        }, 500)

def delete_table(Nmesa):
    try:
        delete = mesa_controller.delete(Nmesa)
        if delete:
            return make_response({
                'message': 'La mesa N°'  + ' fue eliminada satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'La mesa N°'  + ' no fue encontrada'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar la mesa'
        }, 500)

def update_table(Nmesa):
    body = request.get_json()
    try:
        update = mesa_controller.update(Nmesa, body)
        if update:
            return make_response({
                'message': 'La mesa N°'  + ' fue actualizada satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay con el N° '
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información de la mesa'
        }, 500)
