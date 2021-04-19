import requests
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Aqui será pega a segunda tabela do site, que contém varias informações. Caso você queira saber o que está acontecendo nesse código, olhe o arquivo 'pegartimestabela.py', na qual é basicamente identico á este código.
def timespontuacao():
    url = 'https://globoesporte.globo.com/futebol/brasileirao-serie-a/'

    opcoes = Options()
    opcoes.headless = True
    driver = webdriver.Firefox(options=opcoes)

    driver.get(url)

    elemento = driver.find_element_by_xpath('//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]')

    conteudo_html = elemento.get_attribute('outerHTML')

    soup = BeautifulSoup(conteudo_html, 'html.parser')
    encontrar_tabela = soup.find(name='table')

    dadosfull = pandas.read_html(str(encontrar_tabela))[0]
    dados = dadosfull[['P', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG', '%', 'ÚLT. JOGOS']]
    dados.columns = ['Pontos', 'Jogos', 'Vitórias', 'Empates', 'Derrotas', 'Gols pró', 'Gols contra', 'Saldo de gols', '%', 'Ultimos jogos']

    tabelaporca = dict()
    tabelaporca['Tabela'] = dados.to_dict('records')

    tabela = list()
    tabeladados = dict()

    for items in tabelaporca['Tabela']:
        tabeladados['Pontos'] = items['Pontos']
        tabeladados['Jogos'] = items['Jogos']
        tabeladados['Vitórias'] = items['Vitórias']
        tabeladados['Empates'] = items['Empates']
        tabeladados['Derrotas'] = items['Derrotas']
        tabeladados['Gols pró'] = items['Gols pró']
        tabeladados['Gols contra'] = items['Gols contra']
        tabeladados['Saldo de gols'] = items['Saldo de gols']
        tabeladados['%'] = items['%']
        tabeladados['Inutil 2'] = items['Ultimos jogos']
        tabela.append(tabeladados.copy())
        tabeladados.clear()

    driver.quit()

    return tabela