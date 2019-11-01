from flask import Blueprint, jsonify, request
from infra.to_dict import to_dict_list, to_dict

relatorio_app = Blueprint('relatorio_app',__name__)

@relatorio_app.route('/relatorio', methods=['GET'])
def relatorio():
    from services.relatorio_service import relatorio as gera_relatorio
    return jsonify(to_dict_list(gera_relatorio()))