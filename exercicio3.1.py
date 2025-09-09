# Criar class publicacao (conteudo, descricao, autor, data)
# Criar lista_de_publicacao[]
# Def menu[]
# Criar outras modalidades

from dataclasses import dataclass
from datetime import datetime

#cria��o de classe de publica��o
@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    
lista_publicacoes = []

#Aqui estamos criando uma publica��o
def criar_publicacao():
    print("\n === CRIAR PUBLICAC�O ===")
    conteudo = input("Digite o conte�do da publica��o: ")
    descricao = input("Digite a descri��o: ")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()
    
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Publica��o criada com sucesso!")

#Aqui estou criando a op��o de curtida na publica��o    
def curtir_publicacao():
    print("\n=== CURTIR PUBLICA��O ===")
    if not lista_publicacoes:
        print("Nenhuma publica��o dispon�vel.")
        return

    visualizar_feed()
    try:
        indice = int(input("Digite o n�mero da pulica��o para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("Publica��o curtida!")
        else:
            print("Publica��o n�o encontrada.")
    except ValueError:
        print("N�mero inv�lido.")
 
#Aqui estou desenvolvendo op��o de visualiza��o       
def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publica��o dispon�vel.")
        return
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
        print(f"    {pub.conteudo[:50]}...")
        print(f"    {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)

# Aqui estou criando o sistema de visualizar publica��o avulso       
def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICA��O ===")
    if not lista_publicacoes:
        print("Nenhuma publica��o dispon�vel.")
        return
    
    visualizar_feed()
    try:
        indice = int(input("Digite o n�mero da publica��o: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conte�do: {pub.conteudo}")
            print(f"Descri��o: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
        else:
            print("Publica��o n�o encontrada.")
    except ValueError:
        print("N�mero inv�lido.")

# Aqui ser� definido o tipo de visualiza��o por autor    
def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICA��ES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publica��o dispon�vel")
        return
    
    autor = input("Digite o nome do Autor: ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower]
    
    if not publicacoes_autor:
        print(f"Nenhuma publica��o encontrada para {autor}.")
        return
    
    print(f"\nPublica��es de {autor}:")
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo[:50]}... ({pub.curtidas} curtidas)")
        print(f" {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)
        
# Cria��o do menu para ser mostrado.    
def menu():
    while True:
        print("\n REDE SOCIAL ===")
        print("1. Criar Publica��o")
        print("2. Curtir Publica��o")
        print("3. Visualizar Feed")
        print("4. Visualizar Publica��o Individual")
        print("5. Visualizar Publica��es por Autor")
        print("0. Sair")
        
        opcao = input("Escolha uma op��o: ")
        
        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            visualizar_feed()
        elif opcao == "4":
            visualizar_publicacao_individual()
        elif opcao == "5":
            visualizar_publicacoes_por_autor()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Op��o inv�lida!")
if __name__ == "__main__": 
    menu()