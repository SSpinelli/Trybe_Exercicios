class Pessoa:
    def __init__(self, nome, idade=None, saldo_na_conta=None):
        self.idade = idade
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.brinquedos = []

    def __str__(self) -> str:
        return f"{self.nome} - {self.idade} - {self.saldo_na_conta}"


pessoa_01 = Pessoa("Marcelo", 22, 700)
pessoa_02 = Pessoa("Matheus")
pessoa_03 = Pessoa("Maria", 33)
pessoa_04 = Pessoa("Márcia", saldo_na_conta=100)

print(pessoa_01)
print(pessoa_02)
print(pessoa_03)
print(pessoa_04)
