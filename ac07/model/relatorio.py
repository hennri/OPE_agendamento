class ItemRelatorio():
    def __init__(self,nome_cliente):
        self.__nome_cliente = nome_cliente
        
    def atualizar(self,nome_cliente):
        self.__nome_cliente = nome_cliente
        return self
    
    @property
    def nome_cliente(self):
        return self.__nome_cliente
    
    
