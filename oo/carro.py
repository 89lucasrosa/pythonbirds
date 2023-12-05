


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
    >>> #Testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Norte'
    >>> # Testantando a classe carro
    carro.
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
class Direcao:
    rotacao_direita_dic = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_esquerda_dic = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE
    def girar_direita(self):
        self.valor = self.rotacao_direita_dic[self.valor]
    def girar_esquerda(self):
        self.valor = self.rotacao_esquerda_dic[self.valor]




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