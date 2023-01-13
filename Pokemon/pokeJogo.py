import random #Biblioteca de funções de aleatoriedade

#classe Pokemon
# A classe possui os seguintes atributos: nome, especie, tipo, ataque, defesa, hp e movimento

class Pokemon:  
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        self._nome = nome 
        self._especie = especie 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rápido"

#classes Pokemon
class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Aquatico'
        self._movimento = 'Jato de água'
        
class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Fogo"
        self._movimento = "Lança chamas"

class Planta(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Planta"
        self._movimento = "Chicote de cipó"

class Eletrico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Eletrico'
        self._movimento = 'Choque do Trovão'

class Psiquico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Psiquico'
        self._movimento = 'Hipnose'

class Fantasma(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Fantasma'
        self._movimento = 'Phantom Force'

class Inseto(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Inseto'
        self._movimento = 'Missil de espinhos'

class Pedra(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = 'Pedra'
        self._movimento = 'Deslizamento de Terra'

class Treinador: #classe Treinador
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

#subclasses Jogador e Inimigo
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    def escolherPokemon(self): #o jogador escolhe um Pokemon de sua lista para batalhar
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print('\033[31mVocê escreveu um número maior do que o disponível.\033[m')
            else: 
                print('\033[31mVocê escreveu um caractere inválido\033[m')

    def capturarPokemon(self, pokemonCapturado): #Essa função der: 0 pokemon escolhido escapou, se for: 1 adiciona a lista de pokemons do jogador
        opcao = ('ESCAPOU','CAPTURADO')
        jogarPokebola = random.randint(0,1)
        if jogarPokebola == 0:
            print('Pokebola vai!!!')
            print(f'\033[0;31;40m{pokemonCapturado._nome} {opcao[jogarPokebola]}!!!\033[m')
        else:
            jogarPokebola == 1
            print('Pokebola vai!!!')    
            self._pokemons.append(pokemonCapturado)
            print(f'\033[0;32;40m{pokemonCapturado._nome} foi {opcao[jogarPokebola]} COM SUCESSO!!!\033[m')

    
    def listarPokemons(self): #Essa função lista todos os pokemons presentes na lista de pokemons do jogador
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")
         

class Inimigo(Treinador):
    def _init_(self, nome, pokemons):
        super()._init_(nome, pokemons)

#A função recebe dois treinadores (Jogador e Inimigo)
#O Jogador pode escolher o próprio pokemon e o Inimigo
#escolhe um pokemon aleatório de sua lista. Os pokemons são salvos em duas variáveis e quem ficar com o menor hp perde o duelo.
    
def batalhaPokemon(treinador1, treinador2): 

    pokemonJogador = treinador1.escolherPokemon()
    pokemonInimigo = treinador2.escolherPokemon()
    hpatualjogador = pokemonJogador._hp - pokemonInimigo._ataque
    hpatualinimigo = pokemonInimigo._hp - pokemonJogador._ataque

    if hpatualinimigo < hpatualjogador:
        print(f'\033[0;34;40m{pokemonJogador._nome}\033[m atacou com {pokemonJogador._movimento} o \033[0;31;40m{pokemonInimigo._nome}\033[m')
        print(f'\033[0;32;40mPARABÉNS VOCÊ VENCEU!!!\no vencedor foi {pokemonJogador._nome} do treinador(a) {treinador1._nome}\033[m')
    elif hpatualjogador < hpatualinimigo:
        print(f'\033[0;31;40m{pokemonInimigo._nome}\033[m atacou com {pokemonInimigo._movimento} o \033[0;34;40m{pokemonJogador._nome}\033[m')
        print(f'\033[0;31;40mO vencedor foi {pokemonInimigo._nome} do treinador(a) {treinador2._nome}\033[m')
    else:
        print("\033[0;32;40mDeu EMPATE\033[m")

pokemonsDisponiveis = [
Fogo('Charmander', 'Charmander', 'Fogo', 52, 43, 39),
Planta('Bulbasauro', 'Bulbasauro', 'Planta', 49, 49, 45),
Aquatico('Squirtle', 'Squirtle', 'Aquatico', 48, 65, 44),
Fogo('Charmeleon', 'Charmeleon', 'Fogo', 64, 58, 58),
Fogo('Magmar', 'Magmar', 'Fogo', 95, 57, 93),
Planta('Ivysauro', 'Ivysauro', 'Planta', 62, 63, 60),
Planta('Victreebel', 'Victreebel', 'Planta', 105, 65, 70),
Aquatico('Wartortle', 'Wartortle', 'Aquatico', 63, 80, 59),
Aquatico('Poliwag', 'Poliwag', 'Aquatico', 50, 40, 40),
Eletrico('Pikachu', 'Pikachu', 'Eletrico', 55, 40, 35),
Eletrico('Raichu', 'Raichu', 'Eletrico', 90, 55, 60),
Psiquico('Alakazam', 'Alakazam', 'Psiquico', 50, 45, 55),
Pedra('Geodude','Geodude', 'Pedra', 80, 100, 40),
Pedra('Graveler','Graveler', 'Pedra', 105, 115, 55),
Pedra('Golem', 'Golem', 'Pedra', 130, 145, 80),
Fantasma('Gastly', 'Gastly', 'Fantasma', 30, 35, 30),
Fantasma('Haunter', 'Haunter', 'Fantasma', 45, 50, 45),
Fantasma('Gengar', 'Gengar', 'Fantasma', 60, 65, 60),
Pedra('Onix', 'Onix', 'Pedra', 45, 160, 70),
Psiquico('Drowzee', 'Drowzee', 'Psiquico', 48, 45, 60),
Psiquico('Hypno', 'Hypno', 'Psiquico', 73, 70, 85),
Inseto('Scyther', 'Scyther', 'Inseto', 110, 80, 70),
Inseto('Pinsir', 'Pinsir', 'Inseto', 125, 100, 85),
Inseto('Beedrill', 'Beedrill', 'Inseto', 90, 40, 65),
Eletrico('Electabuzz', 'Electabuzz', 'Eletrico', 83, 57, 105)
]

nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(3):
    print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

pokemonInicial = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
print('<==>' * 10)
print(f"O pokemon escolhido foi o \033[0;32;40m{pokemonInicial._nome}\033[m")
print('<==>' * 10)

jogador = Jogador(nomeJogador, [pokemonInicial])
inimigo = Inimigo("Adversário", pokemonsDisponiveis)

while True:
    print('<================ \033[0;34;40mMENU\033[m ================>')
    print("""\033[0;33;40m
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    0. Sair do jogo
    \033[m""")
    print('<======================================>')
    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Você saiu do jogo.")
        break
    elif menu=="1":
        jogador.listarPokemons()
    elif menu=="2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")
        
        capturado = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu=="3":
        print('<============== \033[0;31;40mBATALHAR\033[m ==============>')
        batalhaPokemon(jogador,inimigo)
    else:
        print('\033[31mVocê digitou algo inválido, tente novamente.\033[m')
