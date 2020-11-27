"""
### 2. Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço.
"""
class Produto:
    codigo = 0;
    nome = "";
    preco = 0.00;
    
    
def main():
    lista = []
    for x in range(5):
          p = Produto()
          p.codigo = int(input("Digite o codigo do produto: "))
          p.nome = input("Digite o nome do produto: ")
          p.preco = float(input("Digite o preço do produto: "));
          lista.append(p)
          
   
    for y in range(len(lista)):
         lista[y].preco = lista[y].preco + (lista[y].preco * 0.10)
    
         print("Codigo: ",lista[y].codigo, "Nome do Produto: ", lista[y].nome, "Preço do Produto aumento de 10%: ", lista[y].preco)
   
    
main()    
