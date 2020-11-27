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
    
    nome = input("digite o nome completo do titular que deseja encontrar: ")
    n_existe = True
    for y in range(len(contas)):
   
          if contas[y].nome_titular == nome:
            n_existe = False   
            print("-------------------------------")
            print("Titular da conta: ",contas[y].nome_titular)
            print("-------------------------------")
            print("Número da conta: ",contas[y].numero_conta)
            print("Saldo da conta: ",contas[y].saldo)
    if n_existe:
      print(nome,"não está cadastrado")
            
            
def deletar(contas):
    menor = 0.0;
    
    index_a_remover = 0;
    for k in range(len(contas)):
       
       if k == 0:
           menor = contas[k].saldo;
       else:
           if menor > contas[k].saldo:
               menor = contas[k].saldo
               index_a_remover = k
    contas.pop(index_a_remover)
    print("conta com saldo menor deletado com sucesso")
    return contas
        
        
        
def cadastrar(conta):
 contas = []

 for x in range(15):
    conta = Conta()
    conta.nome_titular = input("escreva o nome do titular: ")
    conta.saldo = float(input("digite o saldo da conta : "))
    conta.numero_conta = int(input("digite o número da conta "))
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
    print("1.Cadastrar uma conta digite 1")
    print("2.Consulta uma conta por nome digite 2")
    print("3.Visualizar todos os dados digite 3")
    print("4.excluir uma conta com saldo menor digite 4")
    print("5.Sair digite 5")
    escolha = int(input("Qual opção acima você deseja: "))
    return escolha
def sair():
    print("saiu do sistema")
def main():
     contas = []
     build(contas)
def build(contas):
    
    conta  = Conta()
    resposta = menu()
    
 
    if resposta == 1:
       contas = cadastrar(conta)
       algo = input("cadastro concluido digite algo para voltar pro menu ou 5 para sair .........")
       if algo == "5":
        return sair()
       else:
           build(contas)
    elif resposta == 3:
        
         if len(contas) == 0:
            print("nenhum aluno foi cadastrado, cadastre para pesquisar")
         else:
             listar(contas)
            
             algo = input("clique algo para continuar ou 5 para sair ....... ")
             if algo == "5":
              return  sair()
             
             build(contas)       
             
    elif  resposta == 4:
        
         if len(contas) == 0:
             print("nenhuma conta foi cadastrada, cadastre para deletar")
            
             algo = input("clique algo para continuar ou 5 para sair ....... ")
             if algo == "5":
              return  sair()
             
              build(contas)
            
            
         else:
            contas = deletar(contas)
             
            algo = input("clique algo para continuar ou 5 para sair ....... ")
            if algo == "5":
               return sair()
           
            build(contas)
        
    elif  resposta == 5:
         if len(contas) == 0:
             print("nenhuma conta foi cadastrada, cadastre para pesquisar")
            
             algo = input("clique algo para continuar ou 5 para sair ....... ")
             if algo == "5":
              return  sair()
             
              build(contas)
            
            
             else:
              consultar_nome(contas)
             
              algo = input("clique algo para continuar ou 5 para sair ....... ")
              if algo == "5":
                return sair()
           
                build(contas)
        
    elif resposta == 2:
            if len(contas) == 0:
             print("nenhum aluno foi cadastrado, cadastre para pesquisar")
            
             algo = input("clique algo para continuar ou 5 para sair ....... ")
             if algo == "5":
              return  sair()
             
             build(contas)
            
            
            else:
              consultar_nome(contas)
             
              algo = input("clique algo para continuar ou 5 para sair ....... ")
              if algo == "5":
                return sair()
           
              build(contas)
         
         
   
main()        
         
