import sqlite3

create_sql = [

"""
CREATE TABLE IF NOT EXISTS Cliente(
    id INTENGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT,
    cpf TEXT NOT NULL,
    rua TEXT NOT NULL,
    bairro TEXT NOT NULL, 
    cidade TEXT NOT NULL,
    numero_casa TEXT NOT NULL    
);
""",

"""
CREATE TABLE IF NOT EXISTS Agendamento(
    id INTEGER,
    idcliente INTENGER,
    idservico INTENGER,
    data DATETIME NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY(idcliente) REFERENCES Cliente(id),
    FOREIGN KEY(idservico) REFERENCES SERVICO(id)
)

""",

"""
CREATE TABLE IF NOT EXISTS Servico(
    id INTENGER PRIMARY KEY,
    descricao TEXT NOT NULL
)

"""

]

from wrap_connection import transact


def con():
    return sqlite3.connect('lms.db')

@transact(con)
def criar_db():
    for script in create_sql:
        cursor.execute(script)
    connection.commit()
    