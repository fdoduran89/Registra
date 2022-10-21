from flask import jsonify, request, make_response
from controllers.mesa import MesaController

mesa_controller = MesaController()

# create table
def insert_table():
    body = request.get_json()
    try:
        mesa = mesa_controller.get_by_id(body['N_mesa'])
        if mesa:
            return make_response({
                'message': 'La mesa N°' + body['N_mesa'] + ' Ya está registrada en el sistema'
            }, 400)
        mesa_controller.create(body)
        return make_response({
            'message': 'La mesa N°' + body['N_mesa'] + ' ha sido creada satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación de la mesa'
        }, 500)

# Find tables
def find_table():
    try:
        mesa = mesa_controller.get_all()
        return make_response(jsonify(mesa), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de las mesas'
        }, 500)

# Find table
def find_table(n_mesa):
    try:
        mesa = mesa_controller.get_by_id(n_mesa)
        if mesa:
            return make_response(jsonify(mesa), 200)
        else:
            return make_response({
                'message': 'La mesa N°' + n_mesa + ' no fue encontrada'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del estudiante'
        }, 500)

# delete table
def delete_table(n_mesa):
    try:
        delete = mesa_controller.delete(n_mesa)
        if delete:
            return make_response({
                'message': 'La mesa N°' + n_mesa + ' fue eliminada satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'La mesa N°' + n_mesa + ' no fue encontrada'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar la mesa'
        }, 500)

# update table
def update_table(n_mesa):
    body = request.get_json()
    try:
        update = mesa_controller.update(n_mesa, body)
        if update:
            return make_response({
                'message': 'La mesa N°' + n_mesa + ' fue actualizada satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay con el N° ' + n_mesa
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información de la mesa'
        }, 500)