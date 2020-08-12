class Pessoa:
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self}'

if __name__ == '__main__':
    p = Pessoa(nome='Augusto')
    p2 = Pessoa(p, nome='Aquiles')
    print(p2.cumprimentar())
    print(p2.nome)
    print(p2.idade)
    for filho in p2.filhos:
        print(filho.nome)