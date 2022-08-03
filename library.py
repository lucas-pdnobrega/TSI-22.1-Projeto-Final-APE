# Equipe : PlayerBarbie Socafofo, Rengato, Yagostoso, Bigsogga
from random import randint
from time import sleep
from os import system
import sys


# Função para exibir o título do projeto
def titulo(t):
    print("""

    ███████╗███████╗██╗████████╗░█████╗░  ██████╗░░█████╗░██████╗░
    ██╔════╝██╔════╝██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
    █████╗░░█████╗░░██║░░░██║░░░██║░░██║  ██████╔╝██║░░██║██████╔╝
    ██╔══╝░░██╔══╝░░██║░░░██║░░░██║░░██║  ██╔═══╝░██║░░██║██╔══██╗
    ██║░░░░░███████╗██║░░░██║░░░╚█████╔╝  ██║░░░░░╚█████╔╝██║░░██║
    ╚═╝░░░░░╚══════╝╚═╝░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

    """)
    sleep(t)
    # clear_output()
    system('cls')
    print("""

    ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░  ██████╗░░█████╗░██████╗░██████╗░██╗███████╗
    ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔════╝
    ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝  ██████╦╝███████║██████╔╝██████╦╝██║█████╗░░
    ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗  ██╔══██╗██╔══██║██╔══██╗██╔══██╗██║██╔══╝░░
    ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║  ██████╦╝██║░░██║██║░░██║██████╦╝██║███████╗
    ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝

    """)
    sleep(t)
    # clear_output()
    system('cls')
    print("""

    ██╗░░░██╗░█████╗░░██████╗░░█████╗░░██████╗████████╗░█████╗░░██████╗░█████╗░
    ╚██╗░██╔╝██╔══██╗██╔════╝░██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗
    ░╚████╔╝░███████║██║░░██╗░██║░░██║╚█████╗░░░░██║░░░██║░░██║╚█████╗░██║░░██║
    ░░╚██╔╝░░██╔══██║██║░░╚██╗██║░░██║░╚═══██╗░░░██║░░░██║░░██║░╚═══██╗██║░░██║
    ░░░██║░░░██║░░██║╚██████╔╝╚█████╔╝██████╔╝░░░██║░░░╚█████╔╝██████╔╝╚█████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░░╚════╝░

    """)
    sleep(t)
    # clear_output()
    system('cls')
    print("""

    ██████╗░███████╗███╗░░██╗░█████╗░████████╗██╗███╗░░██╗██╗░░██╗░█████╗░░██████╗███████╗███╗░░██╗░██████╗░█████╗░░█████╗░░█████╗░░█████╗░
    ██╔══██╗██╔════╝████╗░██║██╔══██╗╚══██╔══╝██║████╗░██║██║░░██║██╔══██╗██╔════╝██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ██████╔╝█████╗░░██╔██╗██║███████║░░░██║░░░██║██╔██╗██║███████║██║░░██║╚█████╗░█████╗░░██╔██╗██║╚█████╗░███████║██║░░╚═╝███████║██║░░██║
    ██╔══██╗██╔══╝░░██║╚████║██╔══██║░░░██║░░░██║██║╚████║██╔══██║██║░░██║░╚═══██╗██╔══╝░░██║╚████║░╚═══██╗██╔══██║██║░░██╗██╔══██║██║░░██║
    ██║░░██║███████╗██║░╚███║██║░░██║░░░██║░░░██║██║░╚███║██║░░██║╚█████╔╝██████╔╝███████╗██║░╚███║██████╔╝██║░░██║╚█████╔╝██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░

    """)
    sleep(t)
    # clear_output()
    system('cls')
    print("""

    ██████╗░██╗░██████╗░░██████╗░█████╗░░██████╗░░██████╗░░█████╗░
    ██╔══██╗██║██╔════╝░██╔════╝██╔══██╗██╔════╝░██╔════╝░██╔══██╗
    ██████╦╝██║██║░░██╗░╚█████╗░██║░░██║██║░░██╗░██║░░██╗░███████║
    ██╔══██╗██║██║░░╚██╗░╚═══██╗██║░░██║██║░░╚██╗██║░░╚██╗██╔══██║
    ██████╦╝██║╚██████╔╝██████╔╝╚█████╔╝╚██████╔╝╚██████╔╝██║░░██║
    ╚═════╝░╚═╝░╚═════╝░╚═════╝░░╚════╝░░╚═════╝░░╚═════╝░╚═╝░░╚═╝

    """)
    sleep(t)
    # clear_output()
    system('cls')

# Função para exibir o loading
def loading(t, vezes, clear):
    done = 'false'
    print()
    while done == 'false':
        for repetir in range(vezes):
            sys.stdout.write('\rCarregando (     )')
            sleep(t)
            sys.stdout.write('\rCarregando (.    )')
            sleep(t)
            sys.stdout.write('\rCarregando (. .  )')
            sleep(t)
            sys.stdout.write('\rCarregando (. . .)')
            sleep(t)
        done = 'true'
    sleep(t)
    # Limpar o terminal (Windows)
    if clear == 1:
        system('cls')

# Quantidade de Navios no tabuleiro
def ler_frotas():
    while True:
        frotas = int(input('\nInsira o número de navios nas frotas dos jogadores (1-10): '))
        if frotas >= 1 and frotas <= 10:
            break
        print('Entrada inválida.')
    return frotas

# Gerando o tabuleiro
def gerar_matriz(n):
    tabuleiro = [['-'] * n for i in range(n)]
    for i in range(n - 1):
        string = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tabuleiro[i][0] = string[i]
        if i == n - 2:
            tabuleiro[i+1][0] = string[i+1]
    return tabuleiro

# Função para exibir matriz
def exibir_matriz(tabuleiro, n):

    for i in range(n):
        for j in range(n):
            if i < 1 and j > 0:
                print(f"{j}   ",end="")
            else:
                print(f"{tabuleiro[i][j]:4}",end="")
        print()
    print()

# Função que retorna quem será o primeiro a jogar (ímpar/par) NA HUMILDA
def par_ou_impar(jogadores):
    # Um dos jogadores escolhe entre ímpar ou par
    escolha_p1 = input(f'\n{jogadores[0]}, escolha Ímpar (I) ou Par (P): ').upper()
    escolha_p2 = str()  # Par ou ímpar funcional e enxuto por Yagostoso e Big_Sogga
    loading(0.4, 1, 1)
    # Decidindo
    if escolha_p1 == "P":
        escolha_p2 = "I"
        print(f"\n{jogadores[0]}, você será par!\n{jogadores[1]}, você será ímpar!")
    else:
        escolha_p2 = "P"  # já que, se escolha_p1 = "I", a escolha_p2 será "P"
        print(f"\n{jogadores[0]}, você será ímpar!\n{jogadores[1]}, você será par!")
    # Sorteio de números para o "ímpar/par"
    sleep(0.4)  # Carregando antes do sorteio
    sorteio = randint(1, 2)
    ganhador = int()
    # Verificando quem ganhou
    if sorteio % 2 == 0 and escolha_p1 == "P":
        print(f"\nO número sorteado é par, logo {jogadores[0]} irá começar a partida!\n")
        ganhador = jogadores.index(jogadores[0])
    elif sorteio % 2 == 0 and escolha_p2 == "P":
        print(f"\nO número sorteado é Par, logo {jogadores[1]} irá começar a partida\n")
        ganhador = jogadores.index(jogadores[1])
    elif sorteio % 2 != 0 and escolha_p1 == "I":
        print(f"\nO número sorteado é ímpar, logo {jogadores[0]} irá começar a partida!\n")
        ganhador = jogadores.index(jogadores[0])
    else:
        print(f"\nO número sorteado é ímpar, logo {jogadores[1]} irá começar a partida!\n")
        ganhador = jogadores.index(jogadores[1])

    # Limpar
    sleep(3.5)
    system('cls')
    return ganhador

# Função para preencher a matriz
def adicionar_navios(tabuleiro, frotas):
    navios1 = 0

    while navios1 < frotas: # 10 torna-se entrada "frotas"

        i = randint(1, 10) # n-1 torna-se "nlin"
        j = randint(1, 10) # n-1 torna-se "ncol"
        
        # Checagem para o canto inferior direito
        if i == 10 and j == 10 and (tabuleiro[i-1][j] != "N") and (tabuleiro[i-1][j-1] != "N") and (tabuleiro[i][j-1] != "N") and (tabuleiro[i][j] != "N"):
            tabuleiro[i][j] = "N"
            navios1 += 1
        
        # Checagem para a última linha
        elif i == 10 and (tabuleiro[i-1][j] != "N") and (tabuleiro[i-1][j-1] != "N") and (tabuleiro[i-1][j+1] != "N") and (tabuleiro[i][j-1] != "N") and (tabuleiro[i][j] != "N") and (tabuleiro[i][j+1] != "N"):
            tabuleiro[i][j] = "N"
            navios1 += 1
        
        # Checagem para a última coluna
        elif j == 10 and (tabuleiro[i-1][j] != "N") and (tabuleiro[i-1][j-1] != "N") and (tabuleiro[i+1][j-1] != "N") and (tabuleiro[i+1][j] != "N") and (tabuleiro[i+1][j-1] != "N") and (tabuleiro[i][j-1] != "N") and (tabuleiro[i][j] != "N") and (tabuleiro[i+1][j] != "N"):
            tabuleiro[i][j] = "N"
            navios1 += 1
        
        # Em qualquer outra célula do tabuleiro
        elif i != 10 and j != 10 and (tabuleiro[i-1][j] != "N") and (tabuleiro[i-1][j-1] != "N") and (tabuleiro[i-1][j+1] != "N") and (tabuleiro[i+1][j-1] != "N") and (tabuleiro[i+1][j] != "N") and (tabuleiro[i+1][j-1] != "N") and (tabuleiro[i][j-1] != "N") and (tabuleiro[i][j] != "N") and (tabuleiro[i][j+1] != "N") and (tabuleiro[i+1][j] != "N") and (tabuleiro[i+1][j+1] != "N"):
            tabuleiro[i][j] = "N"
            navios1 += 1
    
    return tabuleiro

# Função para extrair a coordenada de uma string em formato "XN"
def extrair_coordenada():
    string = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        coord = input('Insira a coordenada desejada (A1, B2...) : ').upper()
        
        # Se digitou string vazia ou com um único elemento
        if len(coord) < 2:
            print('Coordenada inválida, tente novamente. ')
            
        # Se digitou uma coordenada em formato "XNN"
        elif len(coord) > 2:

            # Se o índice 0 é uma letra
            if coord[0] in string: 
                x = string.find(coord[0])  # A10 -> coord[0] = 'A'; coord[1] = '1'; coord[2] = '0'.
            
                # Se o índice 1 e 2 são números
                if (coord[1] and coord[2]) in '0123456789':
                    y = int(coord[1] + coord[2])

                    # Armazenar o valor da coordenada somente se x e y são valores válidos
                    if (y != 0 and y <= 10) and (x != 0 and x <= 10):
                        coord_convertida = [x, y] 
                        break
                     
            # Usuário não digitou um valor válido                       
            print('Coordenada inválida, tente novamente. ')


        # Se digitou uma coordenada em formato "XN"
        else:
            # Se o índice 0 é uma letra
            if coord[0] in string:
                x = string.find(coord[0])  # A1 -> coord[0] = 'A';  coord[1] = 1
                
                # Se o índice 1 é um número
                if (coord[1]) in '0123456789':
                    y = int(coord[1])

                    # Armazenar o valor da coordenada somente se X e Y são válidos
                    if (y != 0) and (x != 0 and x < 11):
                        coord_convertida = [x, y]
                        break
                    
            # Usuário não digitou uma coordenada válida          
            print('Coordenada inválida, tente novamente. ')


    return coord_convertida

# Função para checar condição-vitória
def afundados(frotas, afundados):
    if afundados >= frotas:
        return True
    else:
        return False