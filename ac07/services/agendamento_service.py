from model.agendamento import Agendamento
from infra.log import Log
from dao.agendamento_dao import \
    listar as listar_dao, \
    localizar as localizar_dao, \
    criar as criar_dao, \
    remover as remover_dao, \
    atualizar as atualizar_dao

class JaExiste(Exception):
    pass

class NaoExiste(Exception):
    pass

class DataInvalida(Exception):
    pass

def validar_data(sdata):
    import datetime

    try:
        print("Validando " + sdata)
        data = datetime.datetime.strptime(sdata, "%Y/%m/%d")
    except:
        return False
    else:
        return True


def listar():
    return listar_dao()

def localizar(id):
    return localizar_dao(id)

def criar(id, idcliente, idservico, data, preco):
    from services.cliente_service import localizar as localizar_cliente
    from services.servico_service import localizar as localizar_servico

    if localizar(id) != None:
        raise JaExiste()
    
    if not validar_data(data):
        raise DataInvalida()

    if localizar_cliente(idcliente) == None:
        raise NaoExiste()
    
    if localizar_servico(idservico) == None:
        raise NaoExiste

    log = Log(None)
    criado = Agendamento(id, idcliente, idservico, data, preco)
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

def atualizar(id_antigo, id_novo, idcliente, idservico, data, preco):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise JaExiste()
    log = Log(existente)
    atualizar_dao(id_antigo,id_novo, idcliente, idservico, data, preco)
    log.finalizar(existente)
    return existente

