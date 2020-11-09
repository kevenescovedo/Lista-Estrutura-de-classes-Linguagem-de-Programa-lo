""""
Uma empresa prestadora de serviços armazena informações sobre os
serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente.
É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços:

1) pintura;

2) jardinagem;

3) faxina e

4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente.

Cadastre os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições.
O programa deverá mostrar o seguinte menu de opções:

Cadastrar os tipos de serviços
Mostrar todos os tipos de serviço
Cadastrar os serviços prestados
Mostrar todos os serviços prestados
Mostrar os serviços prestados em determinado dia
Mostrar os serviços prestados dentro de um intervalo de valor
Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
Para a opção 1: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

Para a opção 2: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês.
Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente).
Cada linha representa um dia do mês. Dessa maneira, considere a matriz com dimensão 30 × 3.

Solicite o dia em que o serviço foi prestado e as demais informações. Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no
vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

Para a opção 3: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

Para a opção 4: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

Para a opção 5: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.
"""
class Tiposervico:
    codigo = 0
    descricao = ""
class Servico:
    numero = 0;
    codigo = 0;
    valor = 0;
    codigo_cliente = 0;
def menu():
    print("-----------------------------------------------------------------------------------------------------")
    print("                                              Menu                       ")
    print("-----------------------------------------------------------------------------------------------------")      
    print("1. Cadastrar os tipos de serviços digite 1")
    print("2. Mostrar todos os tipos de serviço digite 2")
    print("3. Cadastrar os serviços prestados digite 3")
    print("4. Mostrar todos os serviços prestados digite 4")
    print("5. Mostrar os serviços prestados em determinado dia digite 5")
    print("6. Mostrar os serviços prestados dentro de um intervalo de valor digite 6")
    print("7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço")
    resposta = int(input("Digite uma das opções acima -> "))
    return resposta
def build(a,b):
    
    resposta = menu()
    
 
    if resposta == 1:
        
        
       cadastrar_servico(a,b)
    elif  resposta == 2:
        mostrar_t_servico(a,b)
        
    elif resposta == 3:
        
       cadastrar_servico_prestado(a,b)
          
    elif  resposta == 4:
          mostrar_todos_servicos_prestados(a,b)
        
       
            
    elif  resposta == 5:
         mostrar_dia_servicos(a,b)
    elif  resposta == 6:
          mostrar_servico_intervalo(a,b)
    elif  resposta == 7:
         mostrar_relatorio(a,b)
      
    else:
        print("não tem essa opção por favor digite numeros entre 1 a 7 sem 0 zeros na frente somente números")
        build(a,b)
         
def main():
     tipos_de_servico = []
     servicos_prestados= []
     build( tipos_de_servico,servicos_prestados)
     
     
   

def cadastrar_servico(a,b):
   
  
    for x in range(4):
         tipo_servico =  Tiposervico()
         tipo_servico.codigo = int(input("Digite o codigo do serviço -> "))
         tipo_servico.descricao = input("Digite a descrição do serviço -> ")
         a.append(tipo_servico)
         
         
    return build(a,b)                               
                                   
        
     
    
def mostrar_t_servico(a,b):
    for y in range(4):


     print("Codigo: ", a[y].codigo,"Descrição: ", a[y].descricao)
     input("digite algo para voltar ao menu ................")
     return build(a,b)
def cadastrar_servico_prestado(a,b):
    b = []
    for dias in range(30):
        print(dias + 1,"Dia do mês")
        servicos = []
        x = 0;
        resposta = "s";
        while x <= 3 and resposta == "s" :
            servico = Servico()
            servico.numero = int(input("Digite o numero do serviço -> "))
            servico.codigo = int(input("Digite o Codigo do serviço -> "))
            
           
            n_existe = True
            for q in range(len(a)):
               
                if a[q] == serico.codigo:
                    n_existe = False
            if n_existe:
                print("o codigo não existe por favor cadastrar em tipo de serviço")
                input("Digite algo para continuar...........")
                b = []
                build(a,b)
                    
            servico.codigo_cliente = int(input("Digite o Codigo do Cliente serviço -> "))    
            servico.valor = float(input("Digite o Valor do serviço -> "))
            servicos.append(servico)
            x = x + 1
            resposta = input("Deseja continuar cadastrar o serviço nesse dia ? digite s para sim e n para não -> ")
           
        b.append(servicos)           
          
   
    return build(a,b)
    
def mostrar_todos_servicos_prestados(a,b):
    print(b)
    for lin in range(len(b)):
        print("Dia ", lin + 1)
        for col in range(len(b[lin])):
            
           
                print("")
                print("Numero do Seriviço -> ",b[lin][col].numero)
                print("Codigo do Serviço -> ",b[lin][col].codigo)
                print("Valor do Seriviço -> ",b[lin][col].valor)
                print("Codigo de Cliente do serviço -> ",b[lin][col].codigo_cliente)
    input("digite algo para voltar ao menu ................")
    return build(a,b)
def mostrar_dia_servicos(a,b):
    dia = int(input("digite o dia que você deseja ver os serviços -> "))
    for col in range(len(b[dia])):
         print("Dia",dia + 1)
         print("")
         print("Numero do Seriviço -> ",b[dia][col].numero)
         print("Codigo do Serviço -> ",b[dia][col].codigo)
         print("Valor do Serviço -> ",b[dia][col].valor)
         print("Codigo de Cliente do serviço -> ",b[dia][col].codigo_cliente)
    input("Digite algo para continuar...........")            
    return build(a,b)
def mostrar_servico_intervalo(a,b):
     valor_me = float(input("Digite o valor menor do intervalo -> "))
     valor_ma = float(input("Digite o valor maior do intervalo -> "))
     for lin in  range(len(b)):
         for col in range(len(b[lin])):
             if valor_me <= b[lin][col].valor <= valor_ma:
                 print("Valores entre ", valor_me, " e ", valor_ma)
                 print("")
                 print("Dia",lin + 1,)
                 print("")
                 print("Numero do Seriviço -> ",b[lin][col].numero)
                 print("Codigo do Serviço -> ",b[lin][col].codigo)
                 print("Valor do Serviço -> ",b[lin][col].valor)
                 print("Codigo de Cliente do serviço -> ",b[lin][col].codigo_cliente)
                 
     input("Digite algo para continuar...........")
     return build(a,b)
     
def mostrar_relatorio(a,b):
    print(b)
    for lin in range(len(b)):
        print("Dia ", lin + 1)
        for col in range(len(b[lin])):
            
           
                print("")
                print("Numero do Seriviço -> ",b[lin][col].numero)
                print("Codigo do Serviço -> ",b[lin][col].codigo)
                print("Valor do Serviço -> ",b[lin][col].valor)
                print("Descrição do Serviço",a[b[lin][col]].descricao)
                print("Codigo de Cliente do serviço -> ",b[lin][col].codigo_cliente)      
    input("digite algo para voltar ao menu ................")
    return build(a,b)    
        
    
main()            
    

        
    
    
    
    

