entradaHora1 = int(input("1: Digite a hora: "))
entradaMinuto1 = int(input("1: Digite os minutos: "))
entradaHora2 = int(input("2: Digite a hora: "))
entradaMinuto2 = int(input("2: Digite os minutos: "))
if entradaHora1 > 12:
    entradaHora1 -=12
if entradaHora2 > 12:
    entradaHora2 -=12
somaHora = (entradaHora1 + entradaHora2)
if somaHora > 12:
    somaHora -= 12
somaMinuto = (entradaMinuto1 + entradaMinuto2)
if somaMinuto > 60:
    somaMinuto -= 60
    somaHora += 1
print(f"{somaHora}:{somaMinuto}")






if somaMinuto > 60:
    somaHora += 1
    somaMinuto -= 60
else:
    somaMinuto = somaMinuto



