#Progama que recebe dois numeros e exibe eles sempre em ordem crescente.
numero1 = float(input("Digite o primeiro numero"))
numero2 = float(input("Digite o segundo numero"))
if numero1 < numero2:
    print(f"> {numero1} > {numero2}")
else:
    print(f"> {numero2} > {numero1}")
