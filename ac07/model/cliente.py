class Cliente():
    def __init__(self, id, nome, email, cpf, rua, bairro, cidade, numero_casa):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__numero_casa = numero_casa
    
    def atualizar(self, id, nome, email, cpf, rua, bairro, cidade, numero_casa):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__numero_casa = numero_casa
        return self
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rua(self):
        return self.__rua

    @property
    def bairro(self):
        return self.__bairro

    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def numero_casa(self):
        return self.__numero_casa


    
        