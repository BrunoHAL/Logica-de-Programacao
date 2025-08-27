def menu():
    print("\n--- Sistema de Cadastro de Paciente ---")
    print("1 - Cadastrar paciente")
    print("2 - Mostrar paciente cadastrado")
    print("3 - Atender paciente")
    print("4 - Sair")
    return input("Escolha uma opção: ")
    
    
# Variáveis de controle
Lista_de_nomes = []
quantidade = 0

while True:
    opcao = menu()
    
    if opcao == "1":
        paciente = input("Digite o nome do paciente: ")
        quantidade = 0
        print(f"Paciente '{paciente}' cadastrado com sucesso!")
        Lista_de_nomes.insert(0,paciente)
        
    elif opcao == "2":
        if paciente is None:
            print("Nenhum paciente cadastrado ainda!")
        else:
            print(f"Existem {quantidade} de pacientes cadastrados!")
                        
    elif opcao == "3":
        if paciente is None:
            print("Nenhum paciente ainda foi atendido!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Produto {adicionar} unidade(s). Estoque atual: {quantidade}")
               
    elif opcao == "4":
            print("Saindo do sistema... até mais!")
            break
            
    else:
        print("Opção inválida! Tente novamente.")
        