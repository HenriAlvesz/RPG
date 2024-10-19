'''
class Battler_Base:
  def __init__(self, nome, params, xparams):
    self.nome = nome
    self.forca = params[0]
    self.agilidade = params[1]
    self.crit_chance = xparams[0]
    self.crit_mult = xparams[1]

class Game_Party:
  def __init__(self):
    self.members = []
    
  def add_member(self, member):
    self.members.append(member)
    
GAME_PARTY = Game_Party()

nome = "Gui"
params = [10, 10]
xparams = [0.1, 1.5]

new_character = Battler_Base(nome, params, xparams)

GAME_PARTY.add_member(new_character)

print(GAME_PARTY.members[0].forca)
'''
atributos_lista = []

def make_atribute(param, nome, descricao):
    atributos_lista.append({param: {'nome': nome, 'descricao': descricao}})

make_atribute("ATK", "Força", "Determina o poder de ataque do personagem")
make_atribute("AGI", "Agilidade", "Influencia a velocidade e esquiva do personagem")

print("Lista de Atributos:")
print("------------------")

for atributo in atributos_lista:
    for param, detalhes in atributo.items():
        print(f"Parâmetro: {param}")
        print(f"Nome: {detalhes['nome']}")
        print(f"Descrição: {detalhes['descricao']}")
        print("------------------")