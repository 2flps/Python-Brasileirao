import requests
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Isso é apenas para pegar a primeira tabela do site, na qual contém informações sobre a classificação, o nome do time e o diferencial de posição a tabela em relação a última rodada
def timestabela():
    url = 'https://globoesporte.globo.com/futebol/brasileirao-serie-a/' # URL do site contendo a tabela do Brasileirão

    opcoes = Options()
    opcoes.headless = True # Essa opção fará com que o Mozilla rode em segundo plano
    driver = webdriver.Firefox(options=opcoes) # Isso fará com que o driver de web selecionado seja o Firefox (o driver de internet precisa estar dentro da Windows PATH)

    driver.get(url) # O driver irá registrar a URL

    #Pegar o elemento (tabela)
    elemento = driver.find_element_by_xpath('//*[@id="classificacao__wrapper"]/article/section[1]') # O driver irá pegar todo o conteúdo da XPath

    conteudo_html = elemento.get_attribute('outerHTML') # Irá extrair todo o conteúdo da HTML

    soup = BeautifulSoup(conteudo_html, 'html.parser') # Irá parsear o conteúdo da HTML
    encontrar_tabela = soup.find(name='table') # Irá encontrar o elemento desejado (nesse caso, 'table')

    dadosfull = pandas.read_html(str(encontrar_tabela))[0] # O panda irá fazer o trabalho de organizar a tabela e converte-lá para uma string dentro de uma lista
    dados = dadosfull[['Classificação', 'Classificação.1', 'Classificação.2']] # Aqui será definida as colunas da tabela
    dados.columns = ['Classificação', 'Time', 'Diferencial'] # Aqui as colunas serão renomeadas

    tabelaporca = dict() # O conteúdo bruto da tabela será colocado nesse dicionário
    tabelaporca['Tabela'] = dados.to_dict('records') # O conteúdo será organizado aqui usando o método .to_dict com o parâmetro 'records' (há mais parâmetros que podem ser usados)

    #Tabela legal
    tabela = list() # Essa lista irá armazenar dicionários
    tabeladados = dict() # Aqui ficará os dados do dicionário que será copiado para a lista 'tabela'

    # Organizar a tabela porca em uma tabela legal
    for classificacao in tabelaporca['Tabela']:
        tabeladados['Classificação'] = classificacao['Classificação']
        tabeladados['Time'] = classificacao['Time']
        tabeladados['Inutil'] = classificacao['Diferencial']
        tabela.append(tabeladados.copy())
        tabeladados.clear()

    # Remover a abreviação dos times que fica concatenada no final da frase
    for c in range(0, len(tabela)):
        timecorrigido = tabela[c]['Time'][:-3]
        tabela[c]['Time'] = timecorrigido

    driver.quit() # Fechará o driver do browser
    return tabela