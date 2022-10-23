from flask import jsonify, request, make_response
from controllers.resultado import ResultadoController

resultado_controller = ResultadoController()

def insert_resultado():
    body = request.get_json()
    try:
        resultado_controller.create(body)
        return make_response({
            'message': 'El resultado ha sido creado satisfactoriamente.'
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

def find_resultado(idResultado):
    try:
        resultados = resultado_controller.get_by_id(idResultado)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado' + idResultado + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado'
        }, 500)

def delete_resultado(idResultado):
    try:
        delete = resultado_controller.delete(idResultado)
        if delete:
            return make_response({
                'message': 'El resultado' + idResultado + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El resultado' + idResultado + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar el resultado'
        }, 500)

def update_resultado(idResultado):
    body = request.get_json()
    try:
        update = resultado_controller.update(idResultado, body)
        if update:
            return make_response({
                'message': 'El resultado' + idResultado + ' fue actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El resultado' + idResultado + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar el resultado'
        }, 500)

def find_resultado_by_mesa(idMesa):
    try:
        resultados = resultado_controller.get_by_mesa(idMesa)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + idMesa + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + idMesa
        }, 500)

def find_resultado_by_partido(idPartido):
    try:
        resultados = resultado_controller.get_by_partido(idPartido)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado del partido ' + idPartido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado del partido ' + idPartido
        }, 500)

def find_resultado_by_candidato(idCandidato):
    try:
        resultados = resultado_controller.get_by_candidato(idCandidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado del candidato ' + idCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado del candidato ' + idCandidato
        }, 500)

def find_resultado_by_mesa_and_partido(idMesa, idPartido):
    try:
        resultados = resultado_controller.get_by_mesa_and_partido(idMesa, idPartido)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + idMesa + ' y del partido ' + idPartido + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + idMesa + ' y del partido ' + idPartido
        }, 500)

def find_resultado_by_mesa_and_candidato(idMesa, idCandidato):
    try:
        resultados = resultado_controller.get_by_mesa_and_candidato(idMesa, idCandidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + idMesa + ' y del candidato ' + idCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + idMesa + ' y del candidato ' + idCandidato
        }, 500)

def find_resultado_by_partido_and_candidato(idPartido, idCandidato):
    try:
        resultados = resultado_controller.get_by_partido_and_candidato(idPartido, idCandidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado del partido ' + idPartido + ' y del candidato ' + idCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado del partido ' + idPartido + ' y del candidato ' + idCandidato
        }, 500)

def find_resultado_by_mesa_and_partido_and_candidato(idMesa, idPartido, idCandidato):
    try:
        resultados = resultado_controller.get_by_mesa_and_partido_and_candidato(idMesa, idPartido, idCandidato)
        if resultados:
            return make_response(jsonify(resultados), 200)
        else:
            return make_response({
                'message': 'El resultado de la mesa ' + idMesa + ', del partido ' + idPartido + ' y del candidato ' + idCandidato + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del resultado de la mesa ' + idMesa + ', del partido ' + idPartido + ' y del candidato ' + idCandidato
        }, 500)
