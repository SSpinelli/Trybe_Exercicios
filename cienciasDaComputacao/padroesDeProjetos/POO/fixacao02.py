from cienciasDaComputacao.padroesDeProjetos.POO.eletrodomestico import (
    Eletrodomestico,
)


class Secador(Eletrodomestico):
    pass


class Batedeira(Eletrodomestico):
    pass


class MaquinaDeLavar(Eletrodomestico):
    pass


meu_secador = Secador("Azul", 120, 200, 180)
minha_batedeira = Secador("Verde", 120, 200, 500)
minha_maquina_de_lavar = Secador("Preta", 120, 200, 880)

print(meu_secador.cor)
print(minha_batedeira.cor)
print(minha_maquina_de_lavar.cor)
