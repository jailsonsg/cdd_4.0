"""ler as notas da 1a. e 2a. avaliações de um aluno,
calcule e imprima a média desse aluno. Só devem ser aceitos valores
válidos durante a leitura (0 a 10) para
cada nota"""
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("número invalido. Digite um numero entre 0 e 10."))
nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("número invalido. Digite um numero entre 0 e 10."))
    if nota2 >=0 and nota2 <= 10:
        print(nota1+nota2/2)


