senha = ('python')
tentativaDoUsuario = input("Digite sua senha: ")
tentativas = 0
if tentativaDoUsuario == senha:
    print("Bem vindo")
else:
  while tentativas < 2:
    tentativaDoUsuario = input("Senha errada. Tente novamente: ")
    tentativas += 1
  print("Voçê errou a senha mais de 3 vezes. Senha bloqueada! ")







