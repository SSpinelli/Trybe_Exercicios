from abc import ABC, abstractclassmethod
from datetime import datetime


class ManipuladorDeLog(ABC):
    @classmethod
    @abstractclassmethod
    def log(cls, msg):
        raise NotImplementedError


class LogEmTela(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        print(msg)


class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        with open("file.txt", "a") as file:
            print(msg, file=file)
        file.close()


class Log:
    def __init__(self, manipuladores):
        self.__manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipuladores):
        self.__manipuladores.add(manipuladores)

    def info(self, msg):
        mensagem_formatada = self.__formatar("INFO", msg)
        self.__log(mensagem_formatada)

    def alerta(self, msg):
        mensagem_formatada = self.__formatar("ALERTA", msg)
        self.__log(mensagem_formatada)

    def erro(self, msg):
        mensagem_formatada = self.__formatar("ERRO", msg)
        self.__log(mensagem_formatada)

    def debug(self, msg):
        mensagem_formatada = self.__formatar("DEBUG", msg)
        self.__log(mensagem_formatada)

    def __formatar(self, nivel, msg):
        d = datetime.now().strftime("%d/%m/%Y %H:%M")
        return f"[{nivel} - {d}]: {msg}"

    def __log(self, msg):
        for manipulador in self.__manipuladores:
            manipulador.log(msg)


a = LogEmTela()
b = LogEmArquivo()
c = Log([a, b])

c.alerta("Teste 02")
