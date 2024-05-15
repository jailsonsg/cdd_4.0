#Programa que recebe um numero inteiro de um usuario e mostra a tabuada de multiplicação desse numero.
numero = int(input("Digite um numero inteiro: "))
for multiplicacao in range (1,11,1):
    resultado = multiplicacao * numero
    print(f"{numero} x {multiplicacao} = {resultado}")



