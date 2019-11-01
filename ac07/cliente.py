from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.cliente_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    ClienteJaExiste, \
    remover as service_remover
    

cliente_app = Blueprint('cliente_app',  __name__)

campos = ["id", "nome", "email", "cpf", "rua", "bairro", "cidade", "numero_casa"]
tipos = [int, str, str, str, str, str, str, str]

@cliente_app.route('/cliente', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@cliente_app.route('/cliente/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@cliente_app.route('/cliente',methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['nome'], dados['email'], dados['cpf'],dados['rua'], dados['bairro'], dados['cidade'], dados['numero_casa'])
        return jsonify(to_dict(criado))
    except ClienteJaExiste:
        return '', 409


@cliente_app.route('/cliente/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404



    