contador = 0
somaNotas = 0
divisao = 0
media = 0
while contador < 10:
    notas = float(input("Digite uma nota: "))
    if notas >= 0 and notas <= 10:
      somaNotas = somaNotas + notas
      divisao = divisao + 1
      contador = contador +1
    else:
        print("Numéro não é valido")
media = (somaNotas/divisao)
print(f"A média dos 10 numeros digitados é: {media}")
