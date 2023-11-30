"""

testando o motor:

    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0


"""
class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

# class Carro:
#     velocidade = 0
#     direcao = (N,L,S,O)
#
#     def acelerar(self):
#         Carro.velocidade += 1
#
#     def frear(self):
#         Carro.velocidade -= 2
#
#     def virar_direita(self):