class Tv:
    @property
    def volume(self):
        if self.__ligada:
            return self.__volume
        return "A TV precisa estar ligada"

    @property
    def canal(self):
        if self.__ligada:
            return self.__canal
        return "A TV precisa estar ligada"

    @property
    def tamanho(self):
        return self.__tamanho

    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def ligar_desligar_tv(self):
        self.__ligada = not self.__ligada

    def aumentar_volume(self):
        if self.__volume < 99 and self.__ligada:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0 and self.__ligada:
            self.__volume -= 1

    def modificar_canal(self, novo_canal):
        if self.__ligada:
            if novo_canal < 1 or novo_canal > 99:
                raise ValueError(
                    "O canal da TV precisa ser um número entre 1 e 99"
                )
            self.__canal = novo_canal


minha_tv = Tv(55)

minha_tv.ligar_desligar_tv()
print(minha_tv.volume)
minha_tv.aumentar_volume()
print(minha_tv.volume)
minha_tv.ligar_desligar_tv()
minha_tv.diminuir_volume()
print(minha_tv.volume)
minha_tv.ligar_desligar_tv()
minha_tv.modificar_canal(99)
print(minha_tv.canal)
