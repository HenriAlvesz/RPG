import json
from rich import print
from rich.table import Table
from colorama import Fore, Style, init

#Colorama para uso no terminal
init(autoreset=True)

# Lista de atributos
atributos_lista = []

# Função para criar e adicionar atributos à lista
def make_atribute(param, nome, descricao):
    atributos_lista.append({param: {'nome': nome, 'descricao': descricao}})

# Criando atributos
make_atribute("ATK", "Força", "Determina o poder de ataque do personagem")
make_atribute("AGI", "Agilidade", "Influencia a velocidade e esquiva do personagem")
make_atribute("INT", "Inteligência", "Aumenta o poder mágico e a capacidade de resolver problemas")
make_atribute("VIG", "Vigor", "Determina a resistência física e energia do personagem")
make_atribute("CAR", "Vigor", "Determina a resistência física e energia do personagem")

# Função para exibir os atributos com Rich
def exibir_atributos():
    table = Table(title="Atributos Disponíveis")
    table.add_column("Código", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nome", style="magenta")
    table.add_column("Descrição", justify="left", style="green")

    for atributo in atributos_lista:
        for param, info in atributo.items():
            table.add_row(param, info['nome'], info['descricao'])

    print(table)

# Função de criação de personagem
def criar_personagem():
    nome = input(Fore.CYAN + "Digite o nome do seu personagem: ")
    print(f"{Fore.GREEN}\nBem-vindo, {nome}! Aqui estão os atributos disponíveis para você escolher:\n")
    exibir_atributos()
    personagem = {'nome': nome, 'atributos': {}, 'inventario': []}
    
    # Atribuição de pontos de atributos
    pontos_disponiveis = 10
    print(f"{Fore.YELLOW}\nVocê tem {pontos_disponiveis} pontos para distribuir entre os atributos.")

    for atributo in atributos_lista:
        for param, info in atributo.items():
            while True:
                try:
                    pontos = int(input(f"Quantos pontos você deseja colocar em {info['nome']}? "))
                    if pontos <= pontos_disponiveis:
                        personagem['atributos'][param] = pontos
                        pontos_disponiveis -= pontos
                        print(f"Pontos restantes: {pontos_disponiveis}")
                        break
                    else:
                        print(Fore.RED + "Pontos insuficientes. Tente novamente.")
                except ValueError:
                    print(Fore.RED + "Digite um número válido.")
    
    print(f"{Fore.GREEN}\nParabéns! Você criou o personagem {personagem['nome']} com os seguintes atributos:")
    for param, pontos in personagem['atributos'].items():
        print(f"{param}: {pontos} pontos")
    
    return personagem

#salvar os personagens em um arquivo JSON
def salvar_personagens(personagens, arquivo='personagens.json'):
    with open(arquivo, 'w') as f:
        json.dump(personagens, f, indent=4)
    print(Fore.GREEN + "\nPersonagens salvos com sucesso!")

#carregar os personagens de um arquivo JSON
def carregar_personagens(arquivo='personagens.json'):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#ficha do personagem com Rich
def exibir_ficha(personagem):
    table = Table(title=f"Ficha de {personagem['nome']}")
    table.add_column("Atributo", justify="left", style="cyan")
    table.add_column("Pontos", justify="right", style="magenta")
    
    for param, pontos in personagem['atributos'].items():
        table.add_row(param, str(pontos))

    print(table)
    print(Fore.YELLOW + "Inventário: " + (", ".join(personagem['inventario']) if personagem['inventario'] else "Vazio"))

# Função para adicionar itens ao inventário
def adicionar_item(personagem):
    item = input(f"Digite o nome do item para adicionar ao inventário de {personagem['nome']}: ")
    personagem['inventario'].append(item)
    print(Fore.GREEN + f"{item} foi adicionado ao inventário de {personagem['nome']}.")

# Função para selecionar um personagem para jogar
def selecionar_personagem(personagens):
    print(Fore.CYAN + "\nSelecione um personagem para jogar:")
    for idx, p in enumerate(personagens):
        print(f"{idx + 1}. {p['nome']}")
    
    while True:
        try:
            escolha = int(input("Digite o número do personagem: "))
            if 1 <= escolha <= len(personagens):
                return personagens[escolha - 1]
            else:
                print(Fore.RED + "Número inválido. Tente novamente.")
        except ValueError:
            print(Fore.RED + "Por favor, digite um número válido.")

# Função para gerenciar personagens 
def gerenciar_personagens():
    personagens = carregar_personagens()
    
    while len(personagens) < 5: #NUMERO MAXIMO DE PERSONAGENS
        opcao = input(Fore.CYAN + "\nVocê deseja criar um novo personagem? (s/n): ").lower()
        if opcao == 's':
            personagens.append(criar_personagem())
        elif opcao == 'n':
            break
        else:
            print(Fore.RED + "Opção inválida.")
    
    salvar_personagens(personagens)
    return personagens

def iniciar_jogo():
    print(Fore.YELLOW + "Bem-vindo ao RPG de chat no terminal!")
    
    personagens = gerenciar_personagens()
    
    if personagens:
        personagem_selecionado = selecionar_personagem(personagens)
        
        while True:
            print(f"\nVocê está jogando com {Fore.GREEN}{personagem_selecionado['nome']}. O que você gostaria de fazer?")
            print("1. Ver ficha")
            print("2. Adicionar item ao inventário")
            print("3. Selecionar outro personagem")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                exibir_ficha(personagem_selecionado)
            elif opcao == '2':
                adicionar_item(personagem_selecionado)
            elif opcao == '3':
                personagem_selecionado = selecionar_personagem(personagens)
            elif opcao == '4':
                print(Fore.YELLOW + "Saindo do jogo. Até logo!")
                salvar_personagens(personagens)
                break
            else:
                print(Fore.RED + "Opção inválida. Tente novamente.")


iniciar_jogo()
