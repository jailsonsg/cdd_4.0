resposta = "s"
while resposta == "s" or resposta == "S":
    media = 0
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("número invalido. Digite um numero entre 0 e 10."))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("número invalido. Digite um numero entre 0 e 10."))

    media = (nota1 + nota2)/2
    print(media)
    resposta = input("Deseja realizar novo cálculo(s/n ?")
