"""Escreva um código que solicite o
nome completo do usuário e mostre
quantas letras tem esse nome"""

numero1 = int(input("Digite o 1 numero:"))
numero2 = int(input("Digite o 2 numero:"))
numero3 = int(input("Digite o 3 numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"O maior numero é {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O maior numero é {numero2}")
else:
    print(f"O maior numero é {numero3}")
