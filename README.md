# Python Brasileirão
A Python-made web scraping algorithm for the Campeonato Brasileiro. By now, the program is only available in Brazilian Portuguese.

## Usage
You just need to run "menu.py". Initially, the program will load the Selenium selected driver (Firefox Driver, by default) and analyse the [Campeonato Brasileiro's Scoreboard provided by Globo Esporte](https://globoesporte.globo.com/futebol/brasileirao-serie-a/). Right after, a prompt will be displayed, where you can choose to check the Scoreboard and some other things.\
If you want to change the Selenium driver, you will need to change both "pegartimestabela.py" and "pegartimespontuacao.py" import methods. By default, the imports look like this:
```python
import requests
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
```
Change `from selenium.webdriver.firefox.options import Options` to your driver of preference.

## Requirements
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Pandas](https://pypi.org/project/pandas/)
- [Selenium](https://pypi.org/project/selenium/)
- A browser driver. By default the program runs the [Firefox Driver](https://github.com/mozilla/geckodriver/releases). You will need to download the driver and put it on the Python's PATH.
- [lxml](https://pypi.org/project/lxml/)
