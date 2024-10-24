# Bibliotecas
import copy
import random

# ---------- Dicionários ----------
# (crie um módulo para isso)
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
        'AGI': 2,
        'RES': 1,
    },
    'Adaga de Bronze': { # (4)
        'tipo': 'arma',
        'subtipo': 'adaga',
        'classificacao': 'leve',
        'descricao': 'Uma adaga simples.',
        'preco': 15,
        'crit_chance': 0.02,
        'ATK': 2,
        'VIG': 1,
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
    'Guerreiro': {},
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
    data = copy.deepcopy(data_equips)  # Desfaz a referência
    equip = {  # Dados padrões
        'nome': 'N/d',
        'id': None,
        'tipo': '',
        'subtipo': '',
        'classificacao': 'geral',
        'descricao': 'N/d',
        'preco': 0,
        'tag': ''
    }
    if type(equip_id) is int:
        equipBase = list(data.values())[equip_id]
        equip['nome'] = list(data.keys())[equip_id]
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
        # Lista de ações em espera (class Action) para execução imediata
        self.lista_actions = []
        self.action_count = 1  # Quantidade de ações por turno
        self.causar_estados = [] # Lista de dicionários {estado_id: x, chance: y}
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
        self.xp += xp
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

    # ----------- Batalha -----------
    def add_estado(self, estado_id):
        novo_estado = copy.deepcopy(data_estados[estado_id])
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
            self[tipo] += dreno
        alvo.hab_reagir(alvo, action)

    def hab_atacar(self, action, alvo):
        dano = max(0, self.get_param('ATK') - alvo.get_param('RES'))
        action.dano['vida'] = dano
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
        self.causar_estados = [] # Lista de dicionários {estado_id: x, chance: y}
        self.dano = {'vida': 0, 'mana': 0, 'estamina': 0}
        self.drenar = {'vida': 0, 'mana': 0, 'estamina': 0}

# Uma classe para armazenar os combatentes proporciona mais flexibilidade
class grupo_base:

    def __init__(self):
        self.membros = []
        self.familiares = []
        self.itens = {}
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


grupo_herois = grupo_base()
grupo_monstros = grupo_base()

# ----- Depuração -----
minha_classe = 'Ladrão'  # Digamos que tenha sido o input VÁLIDO do jogador
novo_heroi = CombatenteHeroi("Guilherme", nova_classe(minha_classe), 6, 4, 5)
grupo_herois.add_membro(novo_heroi)

novo_monstro = CombatenteMonstro("Slime", {}, 99, 99, 1)
grupo_monstros.add_membro(novo_monstro)

print("\n")
grupo_herois.membros[0].exibir_atributos()

print("\n")
grupo_herois.membros[0].exibir_equips()

#print(grupo_herois.membros[0].ATK)
#print(grupo_herois.membros[0].get_param('crit_chance'))
