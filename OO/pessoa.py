class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 26
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    p = Mutante(nome='Augusto')
    p2 = Homem(p, nome='Aquiles')
    print(p2.cumprimentar())
    print(p2.nome)
    print(p2.idade)
    for filho in p2.filhos:
        print(filho.nome)

    p.sobrenome='César'
    print(f'Nome = {p.nome, p.sobrenome}')
    del p2.filhos
    print(p.__dict__)
    print(p2.__dict__)
    print(Pessoa.olhos)
    print(p.olhos)
    print(p2.olhos)
    print(id(Pessoa.olhos), id(p.olhos), id(p2.olhos))
    print(Pessoa.metodo_estatico(), p.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), p.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(p2, Pessoa))
    print(isinstance(p, Homem))
    print(p.olhos)
    print(p.cumprimentar())
    print(p2.cumprimentar())