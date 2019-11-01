from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.agendamento_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    JaExiste, \
    remover as service_remover
    

agendamento_app = Blueprint('agendamento_app',  __name__)

campos = ["id", "idcliente", "idservico", "data", "preco"]
tipos = [int, int, int, str, float]

@agendamento_app.route('/agendamento', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@agendamento_app.route('/agendamento/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@agendamento_app.route('/agendamento',methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['idcliente'], dados['idservico'], dados['data'], dados['preco'])
        return jsonify(to_dict(criado))
    except JaExiste:
        return '', 409


@agendamento_app.route('/agendamento/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404


    