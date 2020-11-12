"""
5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações:
numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma
função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:

Cadastrar contas
Visualizar todas as contas
Consultar por nome
Alterar nome e/ou saldo de um número de conta
Excluir a conta com menor saldo
Sair
"""
class Conta:
  numero_conta = 0
  nome_titular = ""
  saldo = 0.0

def consultar_nome(contas):
  nome = input("digite o nome completo do titular que deseja encontrar -> ")
  n_existe = True
  for y in range(len(contas)):
    if contas[y].nome_titular == nome:
      n_existe = False   
      print("-------------------------------")
      print("Titular da conta: {} ".format(contas[y].nome_titular))
      print("-------------------------------")
      print("Número da conta: {} ".format(contas[y].numero_conta))
      print("Saldo da conta: {:.2f}".format(contas[y].saldo))
  if n_existe:
    print("{} titular não está cadastrado")

def deletar(contas):
  menor = 0.0
  index_a_remover = 0
  for k in range(len(contas)):
    if k == 0:
      menor = contas[k].saldo
    else:
      if menor > contas[k].saldo:
        menor = contas[k].saldo
        index_a_remover = k
  contas.pop(index_a_remover)
  print("conta com saldo menor deletado com sucesso")
  return contas
 
def cadastrar(conta):
 contas = []
 for x in range(2):
  conta = Conta()
  conta.nome_titular = input("escreva o nome do titular: ")
  conta.saldo = float(input("digite o saldo da conta : "))
  conta.numero_conta = int(input("digite o número da conta "))
  print()
  contas.append(conta)
 return contas

def listar(contas):
  for z in range(len(contas)):
    print("-------------------------------")
    print("Titular da conta: ",contas[z].nome_titular)
    print("-------------------------------")
    print("Numero da conta: ",contas[z].numero_conta)
    print("Saldo da conta: ",contas[z].saldo)

def menu():
  print("-------------------------------------------------")
  print("                      Banco                    ")
  print("-------------------------------------------------")
  print("Menu")
  print("1. Cadastrar uma conta digite 1")
  print("2. Consulta uma conta por nome digite 2")
  print("3. Visualizar todos os dados digite 3")
  print("4. Excluir uma conta com saldo menor digite 4")
  print("5. Alterar nome/saldo da conta digite 5")
  print("6. Sair digite 6")
  escolha = int(input("Qual opção acima você deseja? -> "))
  return escolha

def alterar(contas):
  numero_conta = int(input("Digite o número da conta que deseja fazer a alteração do nome/saldo -> "))
  n_existe = True
  for y in range(len(contas)):
    if contas[y].numero_conta == numero_conta:
      n_existe = False   
      print("*"*50)
      print("MENU")
      print("*"*50)
      print("1. Digite 1 para alterar o nome -> ")
      print("2. Digite 2 para alterar o saldo -> ")
      print("3. Digite 3 para alterar o nome e saldo -> ")
      resposta = int(input("Digite uma das opções acima para continuar ->"))
      if resposta == 1:
        contas[y].nome_titular = input("Digite a alteração do nome da conta {}".format(numero_conta))
      elif resposta == 2:
        contas[y].saldo = float(input("Digite a alteração do saldo da conta {:.2f}".format(numero_conta)))
      elif resposta == 3:
        contas[y].nome_titular = input("Digite a alteração do nome da conta {}".format(numero_conta))
        contas[y].saldo = float(input("Digite a alteração do saldo da conta {:.2f}".format(numero_conta)))
  if n_existe:
    print("Número de conta {} não existe em nosso banco de dados.".format(numero_conta))
  build(contas)

def sair():
  print("Obrigado por usar nosso sistema! :-)")

def main():
  contas = []
  build(contas)

def voltar_menu(contas):
  voltar = input("Cadastro concluido. Digite qualquer tecla para voltar pro menu ou 6 para sair .........")
  if voltar == "6":
    return sair()
  else:
    build(contas)

def build(contas):
  conta = Conta()
  resposta = menu()

  if resposta == 1:
    contas = cadastrar(conta)
    voltar_menu(contas)

  elif resposta == 3:
    if len(contas) == 0:
      print("Nenhuma conta foi cadastrada, cadastre para pesquisar.")
    else:
      listar(contas)
      voltar_menu(contas)

  elif resposta == 4:
    if len(contas) == 0:
        print("Nenhuma conta foi cadastrada, cadastre para deletar")
        voltar_menu(contas)
    else:
      contas = deletar(contas) 
      voltar_menu(contas)

  elif resposta == 6:
    sair()

  elif resposta == 2:
    if len(contas) == 0:
      print("Nenhuma conta foi cadastrado, cadastre para pesquisar")
      voltar_menu(contas)
    else:
      consultar_nome(contas)
      voltar_menu(contas)
  
  elif resposta == 5:
    if len(contas) == 0:
      print("Nenhuma conta foi cadastrado, cadastre para pesquisar")
      voltar_menu(contas)
    else:
      alterar(contas)
      voltar_menu(contas)
      

main()       
         
