from infra.to_dict import to_dict, to_dict_list
from flask import Flask, jsonify, request
from cliente import cliente_app
from servico import servico_app
from agendamento import agendamento_app
from infra.db import criar_db


app = Flask(__name__)
app.register_blueprint(cliente_app)
app.register_blueprint(servico_app)
app.register_blueprint(agendamento_app)

@app.route('/')
def all():
    from services.cliente_service import listar as listar_cliente
    from services.servico_service import listar as listar_servico
    from services.agendamento_service import listar as listar_agendamento

    database = {

    "CLIENTES" : to_dict_list(listar_cliente()),
    "SERVICOS" : to_dict_list(listar_servico()),
    "AGENDAMENTO": to_dict_list(listar_agendamento())
    }
    return jsonify(database)


criar_db()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug = True)
