from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.servico_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    ServicoJaExiste
    

servico_app = Blueprint('servico_app',  __name__)

campos = ["id", "descricao"]
tipos = [int, str]

@servico_app.route('/servico', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@servico_app.route('/servico/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@servico_app.route('/servico',methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['descricao'])
        return jsonify(to_dict(criado))
    except ServicoJaExiste:
        return '', 409


@servico_app.route('/servico/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404


    