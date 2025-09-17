#1º O sistema precisa ter agendamento
#2º O sistema precisa ter opção entre cadastro de cliente ou barbeiro
#3º O sistema precisa ter um cadastro da agenda do barbeiro
#4º O sistema precisa ter um cadastro de serviços. Ex: corte simples com preço
#5º O sistema precisa ter um lembrete do agendamento no dia anterior via Whatsapp ou email
#6º O sistema precisa ter modalidade de faturamento mensal individual de cada barbeiro
#7º O sistema precisa ter um histórico de clientes e serviços prestados
#8º O sistema precisa ter uma modalidade de reagendamento
#9º O sistema precisa ter um sistema de aviso para o barbeiro em caso de reagendamento
#10º O sistema precisa ter formas de pagamento(Via pix, via debito/credito ou pagamento no ato do corte)

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    Nome: str
    idade: str
    email: str
    contato: str
    senha: str
    
lista = []

class Barbeiro:
    Nome: str
    Horario: int
    
def criar_usuario():
    print("\n === Criação de Cadastro ===")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")
    contato = input("Digite seu contato: ")
    senha = input("Digite uma senha para cadastro: ")
    usuario_digitado = usuario(nome,idade,email,contato,senha)
    lista.append(usuario_digitado)
    print("Cadastro efetuado com sucesso!")
    
def fazer_login():
    login_email = input("Digite seu email: ")
    login_senha = input("Digite sua senha: ")
    
    for usuario in lista:
        if usuario.email == login_email:
            if usuario.senha == login_senha:
                print("Logado com sucesso!")
            else:
                print("email ou senha incorreto")
    
def agendamento():
    print("\n === Sistema de agendamento ===")
    dia = input("Digite o dia: ")
    hora = input("Digite o horario do agendamento: ")

