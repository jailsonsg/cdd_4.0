#Dado um numero digitado pelo o usuario o programa deve imprimir de 1 ate o numero digitado pelo usuario.
numero = int(input("Digite um numero: "))
for contador in range (1,numero+1,1):
    ## o print por padrão exibe elementos uma abaixo do outro (quebra de linha)

    ## para colocar os dados um ao lado do outro definimos o end como " ". 
    print(contador, end=" ")