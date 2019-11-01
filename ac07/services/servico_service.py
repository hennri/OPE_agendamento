from model.servico import Servico
from infra.log import Log

from dao.servico_dao import \
    listar as listar_dao, \
    localizar as localizar_dao, \
    criar as criar_dao, \
    atualizar as atualizar_dao, \
    remover as remover_dao

class ServicoJaExiste(Exception):
    pass

def listar():
    return listar_dao()

def localizar(id):
    return localizar_dao(id)

def criar(id, descricao):
    if localizar(id) != None:
        raise ServicoJaExiste()
    log = Log(None)
    criado = Servico(id, descricao)
    criar_dao(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    remover_dao(existente.id)
    log.finalizar(None)
    return existente


