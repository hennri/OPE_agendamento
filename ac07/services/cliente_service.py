from model.cliente import Cliente
from infra.log import Log

from dao.cliente_dao import \
    listar as listar_dao, \
    localizar as localizar_dao, \
    criar as criar_dao, \
    remover as remover_dao, \
    atualizar as atualizar_dao

class ClienteJaExiste(Exception):
    pass

def listar():
    return listar_dao()

def localizar(id):
    return localizar_dao(id)

def criar(id, nome, email,cpf,rua,bairro,cidade,numero_casa):
    if localizar(id) != None:
        raise ClienteJaExiste()
    log = Log(None)
    criado = Cliente(id, nome, email,cpf,rua,bairro,cidade,numero_casa)
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

def atualizar(id_antigo, id_novo, id, nome, email, cpf, rua, bairro, cidade, numero_casa):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise ClienteJaExiste()
    log = Log(existente)
    atualizar_dao(id_antigo, id_novo, id, nome, email, cpf, rua, bairro, cidade, numero_casa )
    log.finalizar(existente)
    return existente

