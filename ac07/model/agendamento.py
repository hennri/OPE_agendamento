class Agendamento():
    def __init__(self, id, idcliente, idservico, data, preco):
        self.__id = id
        self.__idcliente = idcliente
        self.__idservico = idservico
        self.__data = data
        self.__preco = preco
    
    def atualizar(self, id, idcliente, idservico, data, preco):
        self.__id = id
        self.__idcliente = idcliente
        self.__idservico = idservico
        self.__data = data
        self.__preco = preco
        return self
    
    @property
    def id(self):
        return self.__id
    
    @property
    def idcliente(self):
        return self.__idcliente
    
    @property
    def idservico(self):
        return self.__idservico

    @property
    def data(self):
        return self.__data

    @property
    def preco(self):
        return self.__preco