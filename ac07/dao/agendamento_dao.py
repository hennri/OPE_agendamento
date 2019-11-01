from infra.db import con
from wrap_connection import transact 
from model.agendamento import Agendamento
 
sql_criar = "INSERT INTO Agendamento(id, idcliente, idservico, data, preco) VALUES(?,?,?,?,?)"
sql_listar = "SELECT * FROM Agendamento"
sql_localizar = "SELECT * FROM Agendamento WHERE id = ?"
sql_delete  = "DELETE FROM Agendamento WHERE id = ?"
sql_atualizar = "UPDATE Agendamento SET id = ?, nome = ? WHERE id = ?"

cliente_db = []

class AgendamentoJaExiste(Exception):
    pass    

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for r in cursor.fetchall():
        resultado.append(Agendamento(r[0], r[1], r[2], r[3], r[4],))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    r = cursor.fetchone()
    if r == None:
        return None
    return Agendamento(r[0], r[1], r[2], r[3], r[4],)

@transact(con)
def criar(agendamento):
    cursor.execute(sql_criar,(agendamento.id, agendamento.idcliente, agendamento.idservico, agendamento.data, agendamento.preco))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_delete, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, idcliente, idservico, data, preco):
    cursor.execute(sql_atualizar, (id_novo, idcliente, idservico, data, preco, id_antigo))
    connection.commit()


