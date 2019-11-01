class Servico():
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

    def atualizar(self, id, descricao):
        self.__id = id 
        self.__descricao = descricao
    
    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao
