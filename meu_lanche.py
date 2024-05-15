numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
if numero1>numero2:
    print(f"> {numero2} >> {numero1}")
elif numero2>numero1:
    print(f"> {numero1} >> {numero2}")
else:
    print("Os numeros digitados são iguais.")
