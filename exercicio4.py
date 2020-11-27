"""
 Uma escola precisa montar o cadastro geral de seus alunos.
 Este cadastro deverá conter as seguintes informações por aluno: nome completo,
 data de nascimento, telefone, endereço completo e série atual.
 Levando em conta que esta escola possui no máximo 500 alunos,
 como você faria para estruturar estas informações num sistema de cadastro e consulta de cadastro,
 por nome e visualização de todos os dados? Implemente utilizando estrutura. Também use a criação de
 funções para cada operação. Use o menu a seguir:
"""
class Aluno:
    nome_completo = "";
    data_nascimento = "";
    telefone = "";
    endereco_completo = "";
    serie_atual = "";
def cadastrar():
    alunos = []
    for x in range(2):
        
        aluno = Aluno()
        aluno.nome_completo = input("escreva o nome completo do aluno: ")
        aluno.data_nascimento = input("escreva a data de nascimento exemplo 10/03/2001: ")
        aluno.telefone = input("escreva o telefone do aluno exemplo (18)9996640661: ")
        aluno.endereco_completo = input("digite o endereco completo do aluno: ")
        aluno.serie_atual = input("digite a serie atual do aluno ex oitavo ano:")
        alunos.append(aluno)
    return alunos
def consultar_nome(alunos):
    
    nome = input("digite o nome completo do aluno que deseja encontrar: ")
    for y in range(len(alunos)):
          if alunos[y].nome_completo == nome:
            print("-------------------------------")
            print("Aluno: ",alunos[y].nome_completo)
            print("-------------------------------")
            print("Data de nascimento: ",alunos[y].data_nascimento)
            print("Telefone: ",alunos[y].telefone)
            print("Endereço: ",alunos[y].endereco_completo)
            print("Serie Atual: ",alunos[y].serie_atual)
            
def listar(alunos):
  
    for z in range(len(alunos)):
       
            print("-------------------------------")
            print("Aluno: ",alunos[z].nome_completo)
            print("-------------------------------")
            print("Data de nascimento: ",alunos[z].data_nascimento)
            print("Telefone: ",alunos[z].telefone)
            print("Endereço: ",alunos[z].endereco_completo)
            print("Serie Atual: ",alunos[z].serie_atual)
                               
                
                         
                        
                         
                               
                         
                   
                   
                 
                 
    
    
        
        
    
    
def menu():
    print("-------------------------------------------------")
    print("                      Escola                     ")
    print("-------------------------------------------------")
    print("Menu")
    print("1.Cadastrar alunos digite 1")
    print("2.Consulta por nome digite 2")
    print("3.Visualizar todos os dados digite 3")
    print("4.Sair digite 4")
    escolha = int(input("Qual opção acima você deseja: "))
    return escolha
def build(vetor) :
    
     resposta =  menu()
     if resposta == 1:
        
         vetor = cadastrar()
         algo = input("cadastro concluido digite algo para voltar pro menu ou 4 para sair .........")
         if algo == "4":
              return  sair()
         
         build(vetor)
         
     if resposta == 3:
        
         listar(vetor)
         algo = input("digite algo para voltar pro menu ou 4 para sair .........")
         if algo == "4":
                sair()
         build(vetor)
         return 0
     if resposta == 4:
         print("sair do sistema")
         
     if resposta == 2:
        
         if len(vetor) == 0:
            print("nenhum aluno foi cadastrado, cadastre para pesquisar")
            
            algo = input("clique algo para continuar ou 4 para sair ....... ")
            if algo == "4":
              return  sair()
             
            build(vetor)
            
            
         else:
             consultar_nome(vetor)
             
             algo = input("clique algo para continuar ou 4 para sair ....... ")
             if algo == "4":
                return sair()
           
             build(vetor)
   
         
            
          
             
            
         
     
         
         
def sair():
    print("sai do sistema")
    
def main():
    vetor = []
    build(vetor)
  
       
  
  
main()   
  
    
    
    
