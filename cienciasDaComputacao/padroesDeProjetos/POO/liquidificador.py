class Liquidificador:
    def get_cor(self):
        return self.__cor.upper()

    def set_cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # o primeiro parâmetro self representa o próprio objeto, é como se
        # fosse o This do JavaScript. O nome pode ser qualquer um,
        #  mas "self" é uma convenção.
        self.preco = preco
        self.__cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0
        self.corrente_maxima_no_motor = potencia / tensao

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )
        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return (self.__ligado, self.__velocidade)


# Em python, o construtor é dividido entre dois métodos "__new__" e "__init__".

meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador("Vermelho", 250, 220, 100)

# Nomes iniciados com "_" são considerados protegidos, lembrando que isso
# é apenas uma convenção dos desenvolvedores, pois ainda teremos acesso.
# Nos iniciados com "__" são considerados privados, não será
# possível acessar por fora da classe.

# Para acessar ou alterar usar esses valores precisamos usar os métodos.

# print(meu_liquidificador._potencia)
# ainda retorna o valor esperado
# print(seu_liquidificador.__velocidade)
# retorna um erro do tipo AttributeError

# meu_liquidificador.ligar(3)
# print(meu_liquidificador.esta_ligado())
# meu_liquidificador.desligar()
# print(meu_liquidificador.esta_ligado())

# print(f"A cor atual é: {meu_liquidificador.get_cor()}")
# meu_liquidificador.set_cor("Verde Limão")
# print(f"A cor atual é: {meu_liquidificador.get_cor()}")
