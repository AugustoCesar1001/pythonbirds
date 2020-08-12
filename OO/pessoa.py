class Pessoa:
    def cumprimentar(self, nome=None, idade=0):
        self.idade = idade
        self.nome = nome
        return f'Olá {nome, idade}'

if __name__ == '__main__':
    nome = 'Augusto'
    idade = 26
    p = Pessoa()
    print(id(p))
    print(p.cumprimentar(nome, idade))
