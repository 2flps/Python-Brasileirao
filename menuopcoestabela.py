from tabelabrasileirao import tabela

def times(tabela):
    '''
    -> Irá pegar o nome de todos os times e colocá-los em uma tabela
    :param tabela: tabela na qual há as informações do campeonato brasileiro
    :return: lista com os nomes dos times
    '''
    times = list()

    for c in range(0, len(tabela)):
        times.append(tabela[c]['Time'][:])
    
    return times


def verTimes(listaTimes):
    '''
    -> Irá printar o nome de todos os times de forma formatada
    :param listaTimes: lista na qual há todos os times (função times())
    :return: sem retorno
    '''
    print('Lista de times:', end = ' ')
    ultimoElemento = len(listaTimes) #Irá pegar o tamanho da lista
    print(ultimoElemento)
    for c in range(0, ultimoElemento):
        if c == ultimoElemento - 1:
            print(listaTimes[c], end = '.')
        else:
            print(listaTimes[c], end = ', ')
    print()


def verTimeNome(times, nomeTime, tabela):
    '''
    -> Irá mostrar as informações de um time procurando-o pelo nome
    :param times: lista contendo o nome dos times
    :param nomeTime: time na qual o usuário deseja ver os dados
    :param tabela: lista contendo os dicionários com as informações dos times
    :return: informações do time/erro caso o time não exista
    '''
    timeslow = list()
    for time in times:
        timelow = time.lower()
        timeslow.append(timelow[:])
    nomedotime = nomeTime.strip().lower()
    contador = 0
    posicaodotime = 0
    encontrado = False
    for c in range(0, len(timeslow)):
        if timeslow[c] == nomedotime:
            posicaodotime = contador
            encontrado = True
        else:
            contador += 1
    if encontrado == False:
        return 'O seu time não foi encontrado. Talvez você digitou errado o nome do time, ou esqueceu de algum acento.'
    else:
        return ('''
{}
{:^158}
{}
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |'''.format('-' * 158, 'BRASILEIRÃO - ANO 2020', '-' * 158, 'Classificação', 'Time', 'Pontos', 'Jogos', 'Vitórias', 'Empates', 'Derrotas', 'Gols pró', 'Gols contra', 'Saldo de gols', '%', tabela[posicaodotime]['Classificação'], tabela[posicaodotime]['Time'], tabela[posicaodotime]['Pontos'], tabela[posicaodotime]['Jogos'], tabela[posicaodotime]['Vitórias'], tabela[posicaodotime]['Empates'], tabela[posicaodotime]['Derrotas'], tabela[posicaodotime]['Gols pró'], tabela[posicaodotime]['Gols contra'], tabela[posicaodotime]['Saldo de gols'], tabela[posicaodotime]['%']))


def verTimeClassificacao(timePos, tabela):
    '''
    -> Irá mostrar as informações de um time procunrando-o pelo nome
    :param timePos: posição do time na tabela (1-20)
    :param tabela: lista contendo os dicionários com as informações dos times
    :return: informações do time/erro caso a classificação esteja fora do alcance
    '''
    if timePos > 20 or timePos < 1:
        return 'O seu time não foi encontrado. Por favor, digite um valor entre 1 e 20.'
    elif type(timePos) != int:
        return 'O seu time não foi encontrado. Por favor, digite um valor numérico entre 1 e 20.'
    else:
        posicaodotime = timePos - 1
        return ('''
{}
{:^158}
{}
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |'''.format('-' * 158, 'BRASILEIRÃO - ANO 2020', '-' * 158, 'Classificação', 'Time', 'Pontos', 'Jogos', 'Vitórias', 'Empates', 'Derrotas', 'Gols pró', 'Gols contra', 'Saldo de gols', '%', tabela[posicaodotime]['Classificação'], tabela[posicaodotime]['Time'], tabela[posicaodotime]['Pontos'], tabela[posicaodotime]['Jogos'], tabela[posicaodotime]['Vitórias'], tabela[posicaodotime]['Empates'], tabela[posicaodotime]['Derrotas'], tabela[posicaodotime]['Gols pró'], tabela[posicaodotime]['Gols contra'], tabela[posicaodotime]['Saldo de gols'], tabela[posicaodotime]['%']))