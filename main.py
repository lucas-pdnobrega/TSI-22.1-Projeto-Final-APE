# Equipe : PlayerBarbie Socafofo, Rengato, Yagostoso, Bigsogga
# from IPython.display import clear_output
from library import *
from os import system
from time import sleep
import sys

# "Carregando"
loading(0.4, 3, 1)

# Exibindo o título do projeto
titulo(3.0)

# A ordem da matriz 'n' é igual a n + 1 pois precisamos de uma linha extra
n = 11

# Lendo os nomes dos jogadores
nomes = [input(f'Insira o nome do jogador {i+1}: ') for i in range(2)]

# Ler Frotas        
frotas = ler_frotas()


# Jogador 1 (p1)
tabuleiro_gabarito_p1 = gerar_matriz(n)
tabuleiro_resposta_p1 = gerar_matriz(n)

# Jogador 2 (p2)
tabuleiro_gabarito_p2 = gerar_matriz(n)
tabuleiro_resposta_p2 = gerar_matriz(n)

# Preencher os tabuleiros gabaritos
tabuleiro_gabarito_p1 = adicionar_navios(tabuleiro_gabarito_p1, frotas)
tabuleiro_gabarito_p2 = adicionar_navios(tabuleiro_gabarito_p2, frotas)

# Testando ciclo de entrada - A função começaria logo aqui né?
navios_afundados_p1 = 0
navios_afundados_p2 = 0
coordenada = []

# Carregando antes de rodar a função par_ou_impar
sleep(0.4)
vez = par_ou_impar(nomes)

# Definir a decisão
decisao = str()

# Função da jogada do jogador N
def jogada(tabuleiro_r, tabuleiro_g):

    # Variáveis a serem utilizadas durante a execução da função
    global n
    global frotas
    global nomes
    global navios_afundados_p1
    global navios_afundados_p2
    global tabuleiro_gabarito_p1
    global tabuleiro_gabarito_p2
    global tabuleiro_resposta_p1
    global tabuleiro_resposta_p2
    global vez
    global decisao

    # Loop de um jogador
    while True:

        # O que o jogador quer fazer?
        decisao = input(f'{nomes[vez]}, Selecione uma ação (Atirar, Resposta, Sair): ').lower()
        sleep(0.5)
        system('cls')

        if decisao == "atirar":
            
            # Exibir o tabuleiro-resposta no qual o player 1 vai jogar
            print(f'\nTabuleiro de {nomes[0]} (P1)\n')           
            exibir_matriz(tabuleiro_resposta_p1, n)
            
            # Exibir o tabuleiro-resposta no qual o player 2 vai jogar
            print(f'\nTabuleiro de {nomes[1]} (P2)\n')
            exibir_matriz(tabuleiro_resposta_p2, n)
            
            coordenada = extrair_coordenada()
            # Carregando para atirar
            loading(0.4, 1, 0)
            sleep(0.4)
            system('cls')
            
            # Se tem um navio não está afundado, afundar
            if tabuleiro_g[coordenada[0]][coordenada[1]] == 'N' and tabuleiro_r[coordenada[0]][coordenada[1]] != 'F':
                tabuleiro_r[coordenada[0]][coordenada[1]] = 'F'
                
                # Exibir o tabuleiro-resposta no qual o player 1 vai jogar
                print(f'\nDisparos de {nomes[0]} (P1)\n')
                exibir_matriz(tabuleiro_resposta_p1, n)
            
                # Exibir o tabuleiro-resposta no qual o player 2 vai jogar
                print(f'\nDisparos de {nomes[1]} (P2)\n')
                exibir_matriz(tabuleiro_resposta_p2, n)

                # Exibir fogo (colorido)
                print('\033[1;31m FOGO!')
                print('\033[1;0m  \n')
                
                # Qual jogador vai pontuar?
                if vez == 0:
                    navios_afundados_p1 += 1
                else:
                    navios_afundados_p2 += 1
    
                # Condição
                if vez == 0:
                    if afundados(frotas, navios_afundados_p1):
                        break
                else:
                    if afundados(frotas, navios_afundados_p2):
                        break
                
            # Se tem um um navio já afundado, tentar novamente
            elif tabuleiro_r[coordenada[0]][coordenada[1]] == 'F' and tabuleiro_g[coordenada[0]][coordenada[1]] == 'N':
                
                # Exibir o tabuleiro-resposta no qual o player 1 vai jogar
                print(f'\nDisparos de {nomes[0]} (P1)\n')       
                exibir_matriz(tabuleiro_resposta_p1, n)
            
                # Exibir o tabuleiro-resposta no qual o player 2 vai jogar
                print(f'\nDisparos de {nomes[1]} (P2)\n')
                exibir_matriz(tabuleiro_resposta_p2, n)
                
                print('\033[1;35m Tente novamente, já afundou o navio aqui...\n')
                print('\033[1;0m  \n')

            # Se já tentou atirar na coordenada, tentar novamente
            elif tabuleiro_r[coordenada[0]][coordenada[1]] == 'A':

                # Exibir o tabuleiro-resposta no qual o player 1 vai jogar
                print(f'\nDisparos de {nomes[0]} (P1)\n')        
                exibir_matriz(tabuleiro_resposta_p1, n)
            
                # Exibir o tabuleiro-resposta no qual o player 2 vai jogar
                print(f'\nDisparos de {nomes[1]} (P2)\n')
                exibir_matriz(tabuleiro_resposta_p2, n)
                
                print('\033[1;35m Tente novamente, já atiraste aqui...\n')
                print('\033[1;0m  \n')

            # Se não tem navio na coordenada fornecida, A de "água" é exibido
            else:
                tabuleiro_r[coordenada[0]][coordenada[1]] = 'A'
                
                # Exibir o tabuleiro-resposta no qual o player 1 vai jogar
                print(f'\nDisparos de {nomes[0]} (P1)\n')
                exibir_matriz(tabuleiro_resposta_p1, n)
            
                # Exibir o tabuleiro-resposta no qual o player 2 vai jogar
                print(f'\nDisparos de {nomes[1]} (P2)\n')
                exibir_matriz(tabuleiro_resposta_p2, n)
                
                # Exibir "ÁGUA" (colorido)
                print('\033[1;36m ÁGUA...')
                print('\033[1;0m  \n')

                # Trocar de jogador
                if vez == 0:
                    vez = 1
                else:
                    vez = 0
                break
            
        # Jogador pede resposta
        elif decisao == 'resposta':

            # Exibir as frotas do player 1 (alvos do player 2)
            print(f'\nAlvos de {nomes[0]} (P1)\n')
            exibir_matriz(tabuleiro_gabarito_p1, n)

            # Exibir as frotas do player 2 (alvos do player 1)
            print(f'\nAlvos de {nomes[1]} (P2)\n')
            exibir_matriz(tabuleiro_gabarito_p2, n)
            
        # Jogador optou por sair (loop de cada jogador)
        elif decisao == 'sair':
            break

# PARTIDA
while True:
    # Jogador optou por sair da partida? (loop da partida)
    if decisao == 'sair':
        break
    # Jogador 1 ganhou?
    if vez == 0:
        if afundados(frotas, navios_afundados_p1):
            print(f'\nO jogador {vez+1}, {nomes[vez]} ganhou!\n')
            break
    # Jogador 2 ganhou?
    else:
        if afundados(frotas, navios_afundados_p2):
            print(f'\nO jogador {vez+1}, {nomes[vez]} ganhou!\n')
            break
    # Jogador 1 joga   
    if vez == 0:
        jogada(tabuleiro_resposta_p1, tabuleiro_gabarito_p1)
    # Jogador 2 joga
    else:
        jogada(tabuleiro_resposta_p2, tabuleiro_gabarito_p2)

print('\n\033[1;33m Fim do jogo!\033[0m\n')