class Personagem:
    def __init__(self, nome, forca, agilidade, inteligencia, vigor, carisma):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.inteligencia = inteligencia
        self.vigor = vigor
        self.carisma = carisma
        self.vida = vigor * 10  # A vida pode ser derivada do vigor
        self.mana = inteligencia * 5  # Mana derivada da inteligência

    def exibir_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Força: {self.forca}")
        print(f"Agilidade: {self.agilidade}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Vigor: {self.vigor}")
        print(f"Carisma: {self.carisma}")
        print(f"Vida: {self.vida}")
        print(f"Mana: {self.mana}")

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    
    pontos = 10
    print(f"Você tem {pontos} pontos para distribuir entre seus atributos.")
    
    forca = int(input("Quantos pontos em Força? "))
    pontos -= forca
    
    agilidade = int(input(f"Quantos pontos em Agilidade? (Restam {pontos}) "))
    pontos -= agilidade
    
    inteligencia = int(input(f"Quantos pontos em Inteligência? (Restam {pontos}) "))
    pontos -= inteligencia
    
    vigor = int(input(f"Quantos pontos em Vigor? (Restam {pontos}) "))
    pontos -= vigor
    
    carisma = pontos  # O que sobrar vai para Carisma
    print(f"Os {pontos} pontos restantes foram atribuídos ao Carisma.")
    
    # Retorna um novo personagem
    return Personagem(nome, forca, agilidade, inteligencia, vigor, carisma)

def criar_personagens():
    personagens = []
    for i in range(5):
        if input("Você quer criar um novo personagem? (s/n): ").lower() == 's':
            personagem = criar_personagem()
            personagens.append(personagem)
            personagem.exibir_ficha()
        else:
            break
    return personagens

#criar até 5 personagens
personagens = criar_personagens()

# Exibe a lista
for personagem in personagens:
    print(f"Personagem criado: {personagem.nome}")
