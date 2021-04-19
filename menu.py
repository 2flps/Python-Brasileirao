cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'pretoebranco': '\033[7;30m'} #Dicionário com cores

from tabelabrasileirao import printarTabela, tabela
from menuopcoestabela import *
from time import sleep
import datetime

# Tempo
agora = datetime.datetime.now()

tabelaBrasileirao = tabela() # Lista contendo os dicionários com as informações dos times
times = times(tabelaBrasileirao) # Lista contendo o nome de cada time

def menu(cores):
    '''
    -> Irá gerar o menu e printá-lo
    :param cores: dicionário contendo uma tabela de cores. Neste dicionário precisa ter as chaves 'vermelho' e 'limpa'
    :return: sem retorno
    '''
    while True:
        print('''
BRASILEIRÃO - ANO {}
ESCOLHA UMA OPÇÃO:\n'''.format(agora.year))
        sleep(1)
        print('{}1. Ver a tabela.{}'.format(cores['amarelo'], cores['limpa']))
        print('{}2. Ver os times.{}'.format(cores['amarelo'], cores['limpa']))
        print('{}3. Ver os dados de um time pelo nome.{}'.format(cores['amarelo'], cores['limpa']))
        print('{}4. Ver os dados de um time pela classificação.{}'.format(cores['amarelo'], cores['limpa']))
        print('{}5. Sair do programa.{}'.format(cores['vermelho'], cores['limpa']))
        userdesejo = str(input('Escolha sua opção: ')) # Aqui o usuário digitará a opção que ele deseja ver
        while userdesejo.isnumeric() == False: # Se o valor digitado não for númerico e inteiro, irá entrar nesse loop de erro
            userdesejo = str(input('Erro. Por favor, escolha o número da opção: '))
        userdesejoint = int(userdesejo) # Se o valor digitado for numérico e inteiro, irá converter para integer
        while userdesejoint < 1 or userdesejoint > 5: # Se o valor convertido para integer foi menor que um ou maior que cinco, irá entrar nesse loop de erro
            userdesejo = str(input('Erro. Por favor, escolha o número da opção: '))
            if userdesejo.isnumeric() == True: #Se o valor digitado for numérico e inteiro, irá converter para integer. Se não for, irá continuar no loop de erro
                userdesejoint = int(userdesejo)
            else:
                pass
        if userdesejoint == 1: # Escolha 1
            printarTabela(tabelaBrasileirao)
        elif userdesejoint == 2: # Escolha 2
            verTimes(times)
        elif userdesejoint == 3: # Escolha 3
            nomedotime = str(input('Digite o nome do time na qual você deseja ver as informações: ')).strip()
            print(verTimeNome(times, nomedotime, tabelaBrasileirao))
        elif userdesejoint == 4: # Escolha 4
            posicao = str(input('Digite a posição do time na tabela: '))
            while posicao.isnumeric() == False: # Se o valor digitado não for numérico e inteiro, irá entrar num looping de erro.
                posicao = str(input('Valor inválido. Por favor, digite novamente a posição do time na tabela: '))
            posicaoint = int(posicao) # Se o valor digitado for numérico e inteiro, irá ser convertido para integer
            while posicaoint < 1 and posicaoint > 20: # Se o valor convertido para integer for menor do que um ou maior do que vinte (quantidade de times que há no Brasileirão)
                posicao = str(input('Valor inválido. Por favor, digite novamente a posição do time na tabela: '))
                if posicao.isnumeric() == True: # Se o valor for numerico, será convertido para integer
                    posicaoint = int(posicao)
                else:
                    pass
            print(verTimeClassificacao(posicaoint, tabelaBrasileirao))
        elif userdesejoint == 5: # Irá finalizar o programa
            print('Programa encerrado')
            break


menu(cores) # Chama a função menu