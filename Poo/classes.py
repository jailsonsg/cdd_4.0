#classe é uma forma onde pode ser criado varios objetos a partir dela.
class Pessoa:
    #atributos são variaveis.
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    #métodos são ações. (funções)
    def dizer_ola(self):
        print(f"Olá meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}m.")

    def cozinhar(self, receita : str):
        print(f"Estou fazendo um(a) {receita}")

#instanciando um objeto.
pessoa1 = Pessoa(nome='Jailson', idade=22, altura=1.88)
pessoa1.dizer_ola()
pessoa1.cozinhar("pizza")


#(COMUNICAÇÃO) - É a comunicação entre objetos  (execução de um metodo)

# (API) - Se vc está desenvolvendo vc precisa conhecer tudo. Se vc está utilizando vc precisa usar da abstração.

#(ABSTRAÇÃO) - Focar apenas conceitos mais importantes para o cenário.

#(ENCAPSULAMENTO) - Apenas métodos do objeto podem alterar dados encapsulados.

#(HERANÇA) - Mecanismo que faz com que uma classe herde os atributos e metodos de outra (Classe pai/Super classe)

#(POLIMORFISMO) - Alteração de comportamentos nos (métodos)




