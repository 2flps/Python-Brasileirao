from pegartimespontuacao import timespontuacao
from pegartimestabela import timestabela
from time import sleep

tabela_de_pontuacao = timespontuacao()
tabela_de_times = timestabela()

def tabela():
    '''
    -> Irá gerar a tabela do brasileirão (remover o inútil e concatenar a tabela de pontuação com a de times)
    :return: lista com os dicionários de cada time
    '''
    #Remover o inutil 2 da tabela de pontuação
    for c in range(0, len(tabela_de_pontuacao)):
        del tabela_de_pontuacao[c]['Inutil 2']

    #Remover o inutil da tabela de times
    for c in range(0, len(tabela_de_times)):
        del tabela_de_times[c]['Inutil']

    tabela = list()

    for c in range(0, len(tabela_de_times)):
        tabela_dados = {**tabela_de_times[c], **tabela_de_pontuacao[c]} # Juntará dois dicionários em um
        tabela.append(tabela_dados.copy())

    return tabela


def printarTabela(tabela):
    '''
    -> Irá printar de forma tabulada a tabela do brasileirão
    :param tabela: tabela não formatada (função tabela())
    :return: sem retorno
    '''
    print('''
{}
{:^158}
{}
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |'''.format('-' * 158, 'BRASILEIRÃO - ANO 2020', '-' * 158, 'Classificação', 'Time', 'Pontos', 'Jogos', 'Vitórias', 'Empates', 'Derrotas', 'Gols pró', 'Gols contra', 'Saldo de gols', '%'))
    for c in range(0, len(tabela)):
        print('''
| {:<15} | {:^17} | {:^8} | {:^8} | {:^11} | {:^9} | {:^11} | {:^11} | {:^13} | {:^17} | {:^4} |'''.format(tabela[c]['Classificação'], tabela[c]['Time'], tabela[c]['Pontos'], tabela[c]['Jogos'], tabela[c]['Vitórias'], tabela[c]['Empates'], tabela[c]['Derrotas'], tabela[c]['Gols pró'], tabela[c]['Gols contra'], tabela[c]['Saldo de gols'], tabela[c]['%']))