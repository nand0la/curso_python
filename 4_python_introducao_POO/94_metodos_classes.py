class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    """
        - Geralmente usamos o método de classe para criar métodos de fábrica.
        Os métodos de fábrica retornam o objeto de classe
        (semelhante a um construtor) para diferentes casos de uso.
    """

    @classmethod
    def retorna_idade_mais(cls):
        pass

    """
        - Geralmente usamos métodos estáticos para criar funções de utilidade.
    """

    @staticmethod
    def retorna_idade():
        pass
