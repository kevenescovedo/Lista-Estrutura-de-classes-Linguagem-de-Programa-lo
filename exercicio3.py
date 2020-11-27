"""
Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos.
Crie outra função para aplicar 10% de aumento no preço do produto e apresente todos os dados do preço.
"""




class Produto:
    codigo = 0
    nome = "";
    preco = 0.00
     

def cadastrar() :
     lista = []
     for x in range(5):
          p = Produto()
          p.codigo = int(input("Digite o codigo do produto: "))
          p.nome = input("Digite o nome do produto: ")
          p.preco = float(input("Digite o preço do produto: "));
          lista.append(p)
     return lista
def dez_porcento(value):
    return value + (value * 0.10)


          
    
    
def main():
 
    vetor = cadastrar()
    for y in range(len(vetor)):
        vetor[y].preco = dez_porcento(vetor[y].preco)
    
        print("Codigo: ",vetor[y].codigo, "Nome do Produto: ", vetor[y].nome, "Preço do Produto aumento de 10%: ", vetor[y].preco)
    
main()   
    
