class Ventilador:
    def get_color(self):
        return self.__color

    def get_volts(self):
        return self.__volts

    def get_speed(self):
        return self.__speed

    def __init__(self, color, volts, price):
        self.__color = color
        self.__volts = volts
        self.price = price
        self.__speed = 0
        self.__max_speed = 5
        self.__its_on = False

    def ligar_ventilador(self, speed):
        if speed > 5 or speed < 0:
            raise ValueError(
                f"""Velocidade não pode ser menor que 0
                ou maior do que {self.__max_speed}"""
            )
        self.__speed = speed
        self.__its_on = True

    def desligar(self):
        self.__speed = 0
        self.__its_on = False

    def itsOn(self):
        return self.__its_on


class Person:
    def __init__(self, nome, idade, money):
        self.name = nome
        self.age = idade
        self.wallet = money
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.price > self.wallet:
            raise ValueError("Você não tem dinheiro o suficiente")
        self.wallet -= ventilador.price
        self.ventilador = ventilador

    def __str__(self) -> str:
        if self.ventilador is None:
            return f"{self.name} não tem um ventilador"
        else:
            return f"""{self.name} tem um
            ventilador da cor {self.ventilador.get_color()}"""


lu = Person("Luis Eduardo Klein de Carvalho", 29, 1000)
ventilador_de_lu = Ventilador("Preto", 220, 300)

print(lu)
print(lu.wallet)

lu.comprar_ventilador(ventilador_de_lu)

print(lu)
print(lu.wallet)
