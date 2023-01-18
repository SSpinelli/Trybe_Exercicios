from cienciasDaComputacao.padroesDeProjetos.POO.liquidificador import (
    Liquidificador,
)
from cienciasDaComputacao.padroesDeProjetos.POO.fixacao01 import Ventilador

meu_liquidificador = Liquidificador("Rosa", 200, 100, 120)
meu_ventilador = Ventilador("Verde", "Vidro", 220, 180)

# print(meu_liquidificador.get_cor())


class Pessoa:
    def __init__(self, nome, saldo) -> None:
        self.nome = nome
        self.saldo = saldo
        self.liquidificador = None
        self.ventilador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo:
            self.saldo -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_ventilador(self, ventilador):
        if ventilador.price <= self.saldo:
            self.saldo -= ventilador.price
            self.ventilador = ventilador

    def __str__(self) -> str:
        return f"""
        {self.nome} - possui {self.saldo} na sua conta,
        um Liquidificador da cor {self.liquidificador.get_cor()}
        um Ventilador com copo de {self.ventilador.get_material()}
        """


pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(meu_liquidificador)
pessoa_cozinheira.comprar_ventilador(meu_ventilador)
pessoa_cozinheira.comprar_ventilador(meu_ventilador)

print(pessoa_cozinheira)
