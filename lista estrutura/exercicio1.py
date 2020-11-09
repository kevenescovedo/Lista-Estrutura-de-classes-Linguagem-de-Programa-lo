"""
Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.
"""
class Produto:
    codigo = 0;
    nome = "";
    preco = 0.00;
    
    
def main():
    p = Produto()
    p.codigo = int(input("Digite o codigo do produto: "))
    p.nome = input("Digite o nome do produto: ")
    p.preco = float(input("Digite o preço do produto: "));
    p.preco = p.preco + (p.preco * 0.10)
    print("Codigo: ",p.codigo, "Nome do Produto: ", p.nome, "Preço do Produto aumento de 10%: ", p.preco)
    
main()    
    
