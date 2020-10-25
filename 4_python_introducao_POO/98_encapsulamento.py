"""
    encapsulamento serve para proteger methodos e atributos de sua classe
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]

    def listar_clientes(self):
        for id, cliente in self.__dados["clientes"].items():
            print(f"{id}: {cliente}")


bd1 = BaseDeDados()
bd1.inserir_cliente(1, "Fernando")
bd1.inserir_cliente(2, "Jose")
bd1.inserir_cliente(3, "Claudio")
bd1.inserir_cliente(4, "Flavia")
bd1.listar_clientes()
