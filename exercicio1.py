#Exercicio 1
#Sistema de estoque com apenas 1 produto 
#1. Opção de cadastro do nome do produto. 
#2. Opção de retirar produto do estoque (precisa ver se tem o produto) 
#3. Opção de adicionar produto no estoque (precisa adicionar um numero maior que 0) 
#4. Opção de ver a quantidade no estoque 


def menu():
    print("\n--- Sistema de Estoque ---")
    print("1 - Cadastrar produtos")
    print("2 - Retirar do estoque")
    print("3 - Adicionar ao estoque")
    print("4 - Ver quantidade em estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    
    
# Variáveis de controle
produto = None
quantidade = 0

while True:
    opcao = menu()
    
    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = 0
        print(f"Produto '{produto}' cadastrado com sucesso!")
        
    elif opcao == "2":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade a retirar: "))
            if retirar <= 0:
                print("A quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidade(s). Estoque atual:{quantidad}")
                        
    elif opcao == "3":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Produto {adicionar} unidade(s). Estoque atual: {quantidade}")
                    
    elif opcao == "4":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            print(f"Produto: {produto} | Quantidade em estoque: {quantidade}")
                
    elif opcao == "0":
            print("Saindo do sistema... até mais!")
            break
            
    else:
        print("Opção inválida! Tente novamente.")


---
config:
  theme: redux
---
flowchart TD
    A(["Inicio"]) --> B["menu"]
    B --> C["Escolha uma opção:"]
    C --> n1["1 - Cadastrar produtos"] & n3["2 - Retirar do estoque"] & n5["3 - Adicionar ao estoque"] & n7["4 - Ver quantidade em estoque"]
    n1 --> n2["Digite o nome do produto"]
    n3 --> n4["Digite a quantidade a retirar"]
    n5 --> n6["Digite a quantidade a adicionar"]
    n7 --> n8["Quantidade em estoque"]
    n4 --> n9["Há quantidade no estoque ?"]
    n9 --> n10["Sim"] & n11["Não"]
    n11 --> n12["Quantidade insuficiente no estoque!"]
    n10 --> n13["Retirado {retirar} unidade(s). Estoque atual:{quantidad}"]
    n6 --> n14["Digite a quantidade a adicionar"]
    n14 --> n15["Menor que 0"] & n16["Maior que 0"]
    n15 --> n17["A quantidade deve ser maior que zero!"]
    n16 --> n18["Produto {adicionar} unidade(s). Estoque atual: {quantidade}"]
    n8 --> n19["Produto: {produto} | Quantidade em estoque: {quantidade}"]
    C@{ shape: diam}
    n9@{ shape: diam}
    n13@{ shape: rect}
    n14@{ shape: diam}
