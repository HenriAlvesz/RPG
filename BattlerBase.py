# Bibliotecas
import copy
import random
import os

import sys

def esperar_tecla():
    print("Pressione qualquer tecla para continuar...\n")
    # Se o sistema for Windows
    if sys.platform == 'win32':
        import msvcrt
        msvcrt.getch()
    # Se o sistema for Unix/Linux ou macOS
    else:
        import tty, termios
        # Captura o estado atual do terminal e espera uma tecla
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def limpar_terminal():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac e Linux
        os.system('clear')


# ---------- Dicionários ----------
# (crie um módulo para isso)
data_atrubutos = {
    'ATK': {
        'nome': 'Força',
        'descricao': '<Descrição da força>',
        'tipo': 'base',
    },
    'AGI': {
        'nome': 'Agilidade',
        'descricao': '<Descrição>',
        'tipo': 'base',
    },
    'VIG': {
        'nome': 'Vigor',
        'descricao': '<Descrição>',
        'tipo': 'base',
    },
    'INT': {
        'nome': 'Inteligência',
        'descricao': '<Descrição>',
        'tipo': 'base',
    },
    'CAR': {
        'nome': 'Carisma',
        'descricao': '<Descrição>',
        'tipo': 'base',
    },
    'RES': {
        'nome': 'Resistência',
        'descricao': '<Descrição>',
        'tipo': 'base',
    },
    'evasao': {
        'nome': 'Evasão',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'precisao': {
        'nome': 'Precisão',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'refleccao': {
        'nome': 'Reflexão',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'dano_mult': {
        'nome': 'Multiplicador de Dano',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'defesa_mult': {
        'nome': 'Multiplicador de Defesa',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'crit_mult': {
        'nome': 'Multiplicador de Crítico',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'crit_chance': {
        'nome': 'Chance de Crítico',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
    'xp_mult': {
        'nome': 'Multiplicador de XP obtido',
        'descricao': '<Descrição>',
        'tipo': 'especial',
    },
}
# data_equips contém os dados dos equipamentos
# Padrão: tipo, classificacao=geral, preco, tag, atributos especiais, atributos base
data_equips = {
    'Capacete de Mineiro': {  # (0)
        'tipo': 'cabeça',
        'classificacao': 'pesado',
        'descricao': 'Um capacete com lanterna, usado nas minas.',
        'preco': 10,
        'RES': 2,
    },
    'Balaclava': {
        'tipo': 'cabeça',
        'classificacao': 'leve',
        'descricao': 'Usado por foras da lei.',
        'preco': 6,
        'AGI': 1,
        'RES': 1,
        'VIG': 1,
    },
    'Botas de Couro': {
        'tipo': 'pés',
        'descricao': 'Protege os pés. Feito de couro de animal.',
        'preco': 8,
        'AGI': 2,
        'RES': 1,
    },
    'Couraça Simples': {
        'tipo': 'corpo',
        'descricao': 'Armadura realmente simples.',
        'preco': 16,
        'VIG': 1,
        'RES': 2,
    },
    'Adaga de Estanho': { # (4)
        'tipo': 'arma',
        'subtipo': 'adaga',
        'classificacao': 'leve',
        'descricao': 'Você inicia sua aventura com uma dessa.',
        'preco': 15,
        'crit_chance': -0.02,
        'ATK': 1,
        'AGI': 1,
    },
    'Adaga de Cobre': {
        'tipo': 'arma',
        'subtipo': 'adaga',
        'classificacao': 'leve',
        'descricao': 'Você inicia sua aventura com uma dessa.',
        'preco': 18,
        'crit_mult': -0.1,
        'ATK': 1,
        'VIG': 1,
    },
    'Adaga de Bronze': {
        'tipo': 'arma',
        'subtipo': 'adaga',
        'classificacao': 'leve',
        'descricao': 'Adaga feita de liga metálica de bronze.',
        'preco': 30,
        'crit_chance': 0.02,
        'crit_mult': 0.1,
        'ATK': 3,
        'AGI': 2,
    },
    'Espada Enferrujada': {
        'tipo': 'arma',
        'subtipo': 'espada',
        'classificacao': 'leve',
        'descricao': 'Uma espada velha, não é muito boa.',
        'preco': 25,
        'crit_mult': -0.1,
        'ATK': 3,
    },
    'Espada Antiga': {
        'tipo': 'arma',
        'subtipo': 'espada',
        'classificacao': 'leve',
        'descricao': 'Está em péssimas condições.',
        'preco': 35,
        'crit_mult': 0.1,
        'precisao': -0.05,
        'ATK': 5,
        'VIG': -1,
    },
    'Gorro de Lã': {
        'tipo': 'cabeça',
        'classificacao': 'leve',
        'descricao': 'Um gorro simples e leve que ajuda a manter o calor.',
        'preco': 5,
        'RES': 1,
    },
    'Sandálias de Linho': {
        'tipo': 'pés',
        'descricao': 'Sandálias leves e flexíveis feitas de linho.',
        'preco': 4,
        'AGI': 1,
    },
    'Túnica de Algodão': {
        'tipo': 'corpo',
        'descricao': 'Roupa leve que proporciona algum conforto.',
        'preco': 17,
        'RES': 1,
        'VIG': 1,
        'INT': 3,
    },
    'Faca de Cozinha': {
        'tipo': 'arma',
        'subtipo': 'adaga',
        'classificacao': 'leve',
        'descricao': 'Uma faca pequena, não muito adequada para combate.',
        'preco': 10,
        'ATK': 2,
    },
    'Máscara de Couro': {
        'tipo': 'cabeça',
        'classificacao': 'leve',
        'descricao': 'Uma máscara rudimentar que protege o rosto.',
        'preco': 12,
        'RES': 2,
        'AGI': 1,
    },
    'Botas de Aventureiro': {
        'tipo': 'pés',
        'descricao': 'Botas resistentes usadas por exploradores.',
        'preco': 10,
        'AGI': 2,
        'RES': 1,
    },
    'Colete de Couro Reforçado': {
        'tipo': 'corpo',
        'descricao': 'Colete de couro resistente, útil para iniciantes.',
        'preco': 20,
        'VIG': 1,
        'RES': 2,
    },
    'Clava de Madeira': {
        'tipo': 'arma',
        'subtipo': 'clava',
        'classificacao': 'pesado',
        'descricao': 'Uma clava rudimentar, mas que causa bons danos.',
        'preco': 15,
        'ATK': 2,
        'precisao': -0.02,
    },
    'Espada de Pedra': {
        'tipo': 'arma',
        'subtipo': 'espada',
        'classificacao': 'pesado',
        'descricao': 'Uma espada feita de pedra bruta.',
        'preco': 28,
        'ATK': 7,
        'AGI': -3,
        'crit_chance': 0.01,
    },
    'Porrete de Orc': {
        'tipo': 'arma',
        'subtipo': 'clava',
        'classificacao': 'pesado',
        'descricao': 'Um porrete feito de madeira dura, confiável para iniciantes.',
        'preco': 32,
        'ATK': 5,
        'RES': 3,
        'AGI': -2,
    },
    'Cinto de Escamas': {
        'tipo': 'acessório',
        'descricao': 'Protege parcialmente o tronco. Feita de escamas de cobra.',
        'preco': 46,
        'RES': 4,
        'CAR': 4,
    },
    'Anel de Madeira': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Um anel simples feito de madeira. ' +\
        'Aumenta a resistência levemente.',
        'preco': 5,
        'RES': 1,
    },
    'Colar de Conchas': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Um colar feito de conchas, conferindo um toque de estilo.',
        'preco': 8,
        'AGI': 1,
    },
    'Pulseira de Couro': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Uma pulseira de couro que dá um pouco de proteção.',
        'preco': 6,
        'VIG': 1,
    },
    'Broche de Ferro': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Um broche pequeno, mas resistente, que pode ser usado na roupa.',
        'preco': 7,
        'RES': 1,
        'precisao': 0.01,
    },
    'Amuleto de Pedra Preciosa': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Um amuleto brilhante que aumenta a sorte do portador.',
        'preco': 15,
        'CAR': 2,
        'crit_chance': 0.02,
    },
    'Cinto de Tecido Reforçado': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Um cinto que proporciona suporte adicional e resistência.',
        'preco': 12,
        'VIG': 2,
        'RES': 1,
    },
    'Bracelete de Ferro Forjado': {
        'tipo': 'acessório',
        'classificacao': 'pesado',
        'descricao': 'Um bracelete feito de ferro forjado, oferecendo boa proteção.',
        'preco': 20,
        'RES': 3,
        'defesa_mult': 0.08,
    },
    'Coroa de Louros': {
        'tipo': 'acessório',
        'classificacao': 'leve',
        'descricao': 'Uma coroa simbólica que aumenta o carisma do portador.',
        'preco': 18,
        'CAR': 3,
        'xp_mult': 0.1,
    },
}
data_runas = {}
data_habilidades = {
    'Atacar': {  # (0)
        'alvo': '1 inimigo',
        'script': 'hab_atacar(alvo)',
    },
    'Defender': {
        'alvo': 'self',
        'script': 'hab_defender()',
    },
}

# data_classe contém todas as classes do jogo
# Classes somam os valores de seus atributos aos do combatente
# (Futuramente adicionar "Tags" que definirão comportamentos especiais).
# Classes evoluem para classes mais altas, substitue o efeito.
# Subclasse é opcional, pode ser obtida explorando uma classe fora de sua especialidade.
# Exemplo: Classe Guerreiro com subclasse Clérigo pode evoluir para Paladino.
data_classe = {
    'Ladrão': {  # (0)
        'action_count': 1,
        'AGI': 3,
        'CAR': -2,
        'INT': -2,
        'RES': -2,
        'VIG': -2,
        'equips': [4, 4, 3, 1, 2, 'acessório'],
        'habilidades': [],
    },
    'Guerreiro': {
        'equips': [],
    },
}

data_estados = {
    # Padrão para estruturação dos efeitos:
    # Duração, tag, atributos especiais, atributos base.
    'Nocauteado': {  # (0)
        'tag': 'Incapacitado',
    },
    'Defendendo': {
        'duracao': 1,
        'defesa_mult': 1.5
    },
    'Furioso': {
        'duracao': 3,
        'dano_mult': 1.5,
        'defesa_mult': 0.65,
        'AGI': 2,
        'INT': -5,
    },
    'Atordoado': {
        'duracao': 2,
        'tag': 'Incapacitado',
        'defesa_mult': 0.9,
    }
}
data_itens = {
    'Tônico':
    {  # (0)
        'alvo': '1 aliado',
        'script': 'a.vida += 15',
        'preco': 5,
    },
    'Èter': {
        'alvo': '1 aliado',
        'script': 'a.mana += 10',
        'preco': 10,
    },
    'Fúria': {
        'alvo': '1 aliado',
        'script': 'a.add_estado(3)',
        'preco': 25,
    },
}
# Em breve eu faço mais exemplos para cada data_, e etc.
# ----- Fim dos Dicionários -----


def novo_equip(equip_id):
    data = data_equips
    equip = {  # Dados padrões
        'nome': 'N/d',
        'id': None,
        'tipo': '',
        'subtipo': '',
        'classificacao': 'geral',
        'descricao': 'N/d',
        'preco': 0,
        'tag': '',
        'runas': [],
    }
    if type(equip_id) is int:
        equipBase = copy.deepcopy(list(data.values())[equip_id])
        equip['nome'] = copy.deepcopy(list(data.keys())[equip_id])
        equip['id'] = equip_id
        for chave, valor in equipBase.items():
            equip[chave] = valor
    else:
        equip['tipo'] = equip_id

    return equip


def nova_classe(classe_key):
    if classe_key is None:
        return {}
    classe = copy.deepcopy(data_classe[classe_key])
    for i, equip in enumerate(classe['equips']):
        classe['equips'][i] = novo_equip(equip)

    return classe


class CombatenteBase:

    def __init__(self, nome, classe, ATK=5, AGI=5, INT=5, VIG=5, CAR=5):
        self.nome = nome
        # Atributos básicos
        self.ATK = ATK
        self.AGI = AGI
        self.INT = INT
        self.VIG = VIG
        self.CAR = CAR
        self.RES = 5  # Defesa base
        # Atributos especiais
        self.evasao = 0.1  # Chance de evitar ataques
        self.precisao = 0.75  # Chance de acertar ataques
        self.refleccao = 0.0  # Chance de refletir magia
        self.dano_mult = 1.0  # Multiplicador de dano
        self.defesa_mult = 1.0  # Denominador de dano recebido
        self.crit_chance = 0.1  # Chance de critico
        self.crit_mult = 1.75  # Multiplicador de dano em caso de critico
        self.xp_mult = 1.0  # Multiplicador de XP obtido
        # Lista de ações em espera (class Action) para execução imediata
        self.lista_actions = []
        self.action_count = 1  # Quantidade de ações por turno
        self.causar_estados = [
        ]  # Lista de dicionários {estado_id: x, chance: y}
        self.evitar_estados = []
        # Info: informações adicionais inúteis em batalha
        self.info = {'batalhas': 0, 'morreu': 0, 'matou': 0}
        # Modificadores de atributos
        self.estados = []  # Lista de dicionários
        self.classe = classe  # Dicionário da classe
        self.subclasse = {}  # Dicionário da subclasse
        self.xp = 0
        self.nivel = 1
        self.habilidades = []
        self.equips = self.init_equips()  # Lista de dicionários
        self.recuperar_total()

    def caracteristicas(self):
        return [self, self.classe, self.subclasse] + self.equips +\
        self.estados + self.habilidades

    def get_param(self, param):
        result = 0
        for item in self.caracteristicas():
            # Verifica se item é um objeto com atributo param
            if hasattr(item, param):
                result += getattr(item, param, 0)
            # Verifica se item é um dicionário com chave param
            elif isinstance(item, dict) and param in item:
                result += item.get(param, 0)
        return result

    def is_morto(self):
        return self.vida <= 0

    def is_vivo(self):
        return self.vida > 0

    # Novos métodos
    def recuperar_total(self):
        self.vida = self.max_vida()
        self.mana = self.max_mana()
        self.estamina = self.max_estamina()

    def max_vida(self):
        return self.get_param('VIG') * 10

    def max_mana(self):
        return self.get_param('INT') * 2

    def max_estamina(self):
        return (self.get_param('VIG') + self.get_param('AGI')) * 2

    def per_vida(self):
        return self.vida / self.max_vida()

    def per_mana(self):
        return self.mana / self.max_mana()

    def per_estamina(self):
        return self.estamina / self.max_estamina()

    # Identifica classe da instância
    def is_heroi(self):
        return isinstance(self, CombatenteHeroi)

    def is_monstro(self):
        return isinstance(self, CombatenteMonstro)

    def is_familiar(self):
        return isinstance(self, CombatenteFamiliar)

    # Retorna a classe do grupo que o representa
    def get_aliados(self):
        amigo = False  # Lógica para familiares
        if self in grupo_herois.familiares:
            amigo = True
        return grupo_herois if self.is_heroi() or amigo else grupo_monstros

    def get_inimigos(self):
        inimigo = False  # Lógica para familiares
        if self in grupo_monstros.familiares:
            inimigo = True
        return grupo_monstros if self.is_monstro() or inimigo else grupo_herois

    def add_xp(self, xp):
        self.xp += round(xp * self.get_param('xp_mult'))
        while self.xp >= self.xp_necessario:
            self.subir_nivel()

    # Calcula xp necessário para subir de nível
    def xp_necessario(self):
        return round(self.nivel * 15 * (1.1**(self.nivel - 1)))

    def subir_nivel(self):
        self.xp -= self.xp_necessario()
        if self.xp < 0:
            self.xp = 0
        self.nivel += 1
        self.recuperar_total()

    def init_equips(self):
        return self.classe.get('equips', [])
    # Equipar equipamento
    def set_equip(self, equip_obj, equip_id):
        if equip_id >= len(self.equips):
            return False
        old_equip = self.equips[equip_id]
        if old_equip['tipo'] != equip_obj['tipo']:
            return False
            self.equips[equip_id] = equip_obj
            self.get_aliados().add_equip(old_equip)
        return equip_obj

    def interpretar_input(self, input_):
        if input_ == '':
            return None

    # ----------- Batalha -----------
    def add_estado(self, estado_id):
        novo_estado = copy.deepcopy(list(data_estados.values())[estado_id])
        if any(estado == novo_estado for estado in self.estados):
            return
        self.estados.append(novo_estado)

    # Inicia objeto da ação
    def make_action(self):
        action = Action()
        action.errou = self.get_param('precisao') > random.random()
        return action

    def executar_dano(self, action, alvo):
        for tipo, dano in action.dano:
            alvo[tipo] -= dano

        for tipo, dreno in action.drenar:
            alvo[tipo] -= dreno
            # Aqui acessa o atributo correspondente em self
            setattr(self, tipo, getattr(self, tipo) + dreno)
        alvo.hab_reagir(alvo, action)

    def dano_modificador(self, alvo, action):
        action.dano['vida'] *= \
        self.get_param('dano_mult') / alvo.get_param('defesa_mult')
        action.drenar['vida'] *= \
        self.get_param('dano_mult') / alvo.get_param('defesa_mult')

    def hab_atacar(self, action, alvo):
        dano = max(0, self.get_param('ATK') * 2 - alvo.get_param('RES'))
        action.dano['vida'] = dano
        self.dano_modificador(alvo, action)
        self.executar_dano(alvo, action)

    def hab_defender(self):
        self.add_estado(2)

    # Lógica para Contra-atacar e Reflexão mágica
    def hab_reagir(self, action, alvo):
        pass

    # ----------- Ferramentas de depuração -----------
    def __repr__(self):  # Representação do objeto
        txt1 = ""
        if self.is_heroi():
            txt1 = 'Herói'
        elif self.is_monstro():
            txt1 = 'Monstro'
        elif self.is_familiar():
            txt1 = 'Familiar'
        return f'{txt1}: {self.nome}(Nv {self.nivel})'

    def exibir_atributos(self):
        keys = ('ATK', 'AGI', 'INT', 'VIG', 'CAR')
        print(f'Atributos de {self.nome}:\n')
        for key in keys:
            valor_total = self.get_param(key)
            valor_base = getattr(self, key)
            valor_delta = valor_total - valor_base
            if valor_delta >= 0:
                valor_delta = "+" + str(valor_delta)
            print(f' {key}:{"."*(12-len(key))} {valor_total} ({valor_delta})')

    def exibir_equips(self):
        print(f'Equipamentos de {self.nome}:\n')
        for equip in self.equips:
            name = equip["tipo"].capitalize() + ":"
            print(f' {name}{"."*(13-len(name))} {equip["nome"]}')
        print('')


# Classes que herdam de CombatenteBase, útil para comportamentos específicos
class CombatenteHeroi(CombatenteBase):
    pass


class CombatenteMonstro(CombatenteBase):

    def __init__(self, *args):
        super().__init__(*args)
        self.elite = False
        self.chefe = False


class CombatenteFamiliar(CombatenteBase):
    pass


class Action:

    def __init__(self):
        self.user = None
        self.target = None
        self.errou = False
        self.evitou = False
        self.critico = False
        self.refletido = False
        self.contra_atacado = False
        self.causar_estados = [
        ]  # Lista de dicionários {estado_id: x, chance: y}
        self.dano = {'vida': 0, 'mana': 0, 'estamina': 0}
        self.drenar = {'vida': 0, 'mana': 0, 'estamina': 0}


# Uma classe para armazenar os combatentes proporciona mais flexibilidade
class grupo_base:

    def __init__(self):
        self.membros = []
        self.familiares = []
        self.itens = {}
        self.equips = []
        self.ouro = 0
        self.cristais = 0

    def add_membro(self, member):
        self.membros.append(member)

    def remove_membro(self, member):
        self.membros.remove(member)

    def add_familiar(self, companion):
        self.familiares.append(companion)

    def remove_familiar(self, companion):
        self.familiares.remove(companion)

    def add_equip(self, equip_id):
        equip = equip_id
        if isinstance(equip_id, int):
            equip = novo_equip(equip_id)
        self.equips.append(equip)
        return equip

    def remove_equip(self, equip_obj):
        self.equips.remove(equip_obj)


batalha_log = []


def add_log(string):
    batalha_log.append(string)


def exibir_log():
    print('\n'.join(batalha_log))


grupo_herois = grupo_base()
grupo_monstros = grupo_base()

# ----- Depuração -----
minha_classe = 'Ladrão'  # Digamos que tenha sido o input VÁLIDO do jogador
novo_heroi = CombatenteHeroi("Guilherme", nova_classe(minha_classe), 6, 4, 5)
grupo_herois.add_membro(novo_heroi)

novo_monstro = CombatenteMonstro("Slime", {}, 5, 3, 6)
grupo_monstros.add_membro(novo_monstro)

#print("\n")
#grupo_herois.membros[0].exibir_atributos()

#print("\n")
grupo_herois.membros[0].exibir_equips()

#exibir_log()

equip = grupo_herois.add_equip(0)
grupo_herois.membros[0].set_equip(equip, 0)

grupo_herois.membros[0].exibir_equips()



#print(grupo_herois.equips)
