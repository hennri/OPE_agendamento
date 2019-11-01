from infra.db import con
from wrap_connection import transact 
from model.servico import Servico
 
sql_criar = "INSERT INTO Servico(id, descricao) VALUES(?,?)"
sql_listar = "SELECT * FROM Servico"
sql_localizar = "SELECT * FROM Servico WHERE id = ?"
sql_delete  = "DELETE FROM Servico WHERE id = ?"
sql_atualizar = "UPDATE Cliente SET id = ?, nome = ? WHERE id = ?"

servico_db = []
    

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for r in cursor.fetchall():
        resultado.append(Servico(r[0], r[1],))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    r = cursor.fetchone()
    if r == None:
        return None
    return Servico(r[0], r[1],)

@transact(con)
def criar(servico):
    cursor.execute(sql_criar,(servico.id, servico.descricao))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_delete, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, descricao):
    cursor.execute(sql_atualizar, (id_novo, descricao, id_antigo))
    connection.commit()


