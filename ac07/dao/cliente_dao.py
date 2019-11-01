from infra.db import con
from wrap_connection import transact 
from model.cliente import Cliente
 
sql_criar = "INSERT INTO Cliente(id, nome, email,cpf,rua,bairro,cidade,numero_casa) VALUES(?,?,?,?,?,?,?,?)"
sql_listar = "SELECT * FROM Cliente"
sql_localizar = "SELECT * FROM Cliente WHERE id = ?"
sql_delete  = "DELETE FROM Cliente WHERE id = ?"
sql_atualizar = "UPDATE Cliente SET id = ?, idcliente = ?, idservico = ? , data = ?, preco = ? WHERE id = ?"

cliente_db = []

class ClienteJaExiste(Exception):
    pass

    

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for r in cursor.fetchall():
        resultado.append(Cliente(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    r = cursor.fetchone()
    if r == None:
        return None
    return Cliente(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],)

@transact(con)
def criar(cliente):
    cursor.execute(sql_criar,(cliente.id, cliente.nome, cliente.email, cliente.cpf, cliente.rua, cliente.bairro, cliente.cidade, cliente.numero_casa))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_delete, (id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, idcliente, idservico, data, preco, id_novo,):
    cursor.execute(sql_atualizar, (id_novo, idcliente, idservico, data, preco, id_antigo))
    connection.commit()


