from flask import jsonify, request, make_response
from controllers.resultado import ResultadoController

resultado_controller = ResultadoController()

def insert_resultado():
    body = request.get_json()
    try:
        resultado_controller.create(body)
        return make_response({
            'message': str(body['votos']) + ' voto(s) han sido agregados a la mesa ' +
            str(body['id_mesa']) + ' y al candidato ' + str(body['id_candidato'])
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación del resultado: ' + str(ex)
        }, 500)

def find_resultados():
    try:
        resultados = resultado_controller.get_all()
        return make_response(jsonify(resultados), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de los resultados'
        }, 500)

def find_resultado(id):
    try:
        resultados = resultado_controller.get_by_id(id)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado ' + str(id) + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado'
        }, 500)

def delete_resultado(id):
    try:
        delete = resultado_controller.delete(id)
        if delete:
            return make_response({
                'message': 'El resultado ' + str(id) + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El resultado ' + str(id) + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar el resultado'
        }, 500)

def update_resultado(id):
    body = request.get_json()
    try:
        update = resultado_controller.update(id, body)
        if update:
            return make_response({
                'message': 'El resultado ' + str(id) + ' fue actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El resultado ' + str(id) + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar el resultado'
        }, 500)

def find_resultado_by_mesa(id_mesa):
    try:
        resultados = resultado_controller.get_by_mesa(id_mesa)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + id_mesa + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + id_mesa
        }, 500)

def find_resultado_by_partido(id_partido):
    try:
        resultados = resultado_controller.get_by_partido(id_partido)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado del partido ' + id_partido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado del partido ' + id_partido
        }, 500)

def find_resultado_by_candidato(id_candidato):
    try:
        resultados = resultado_controller.get_by_candidato(id_candidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado del candidato ' + id_candidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado del candidato ' + id_candidato
        }, 500)

def find_resultado_by_mesa_and_partido(id_mesa, id_partido):
    try:
        resultados = resultado_controller.get_by_mesa_and_partido(id_mesa, id_partido)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + id_mesa + ' y del partido ' + id_partido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + id_mesa + ' y del partido ' + id_partido
        }, 500)

def find_resultado_by_mesa_and_candidato(id_mesa, id_candidato):
    try:
        resultados = resultado_controller.get_by_mesa_and_candidato(id_mesa, id_candidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + id_mesa + ' y del candidato ' + id_candidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def candidato_partido_votos_desc():
    try:
        resultados = resultado_controller.candidato_partido_votos_desc()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def candidato_mesa_partido_votos():
    try:
        resultados = resultado_controller.candidato_mesa_partido_votos()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def find_resultado_by_mesa_and_partido_and_candidato(id_mesa, id_partido, id_candidato):
    try:
        resultados = resultado_controller.get_by_mesa_and_partido_and_candidato(id_mesa, id_partido, id_candidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + id_mesa + ', del partido ' + id_partido + ' y del candidato ' + id_candidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + id_mesa + ', del partido ' + id_partido + ' y del candidato ' + id_candidato
        }, 500)

def mesa_votos():
    try:
        resultados = resultado_controller.mesa_votos()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def partido_votos():
    try:
        resultados = resultado_controller.partido_votos()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def partido_mesa_votos():
    try:
        resultados = resultado_controller.partido_mesa_votos()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def percentage_by_partido():
    try:
        resultados = resultado_controller.percentage_by_partido()
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'No se encontraron resultados'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información: ' + str(ex)
        }, 500)

def delete_database():
    try:
        resultado_controller.delete_database()
        return make_response({
            'message': 'La base de datos ha sido reseteada'
        }, 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al reseteada la base de datos'
        }, 500)