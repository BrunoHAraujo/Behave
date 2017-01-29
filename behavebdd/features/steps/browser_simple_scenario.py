from selenium import webdriver
from behave import step
from time import sleep

dic_site = {"python":"https://www.python.org/"}
dic_titles ={"python":"Python"}


@step('eu seto o driver do "{driver:w}" no selenium')
def set_driver(context,driver):
    """
    Esta função seta o driver
    que será usado no
    selenium
    """
    if driver == "Firefox":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()


@step('entro no site "{site:w}"')
def set_site(context,site):
    """
    Esta função seta a url que será
    aberta pelo browser, acessando um dicionário
    pré definido que contém as urls
    """

    context.driver.get(dic_site[site])


@step('a url do browser deve ser "{site:w}"')
def verify_url(context,site):
    """0
    Esta função verifica se a url atual da página
    é a url que foi solicitada
    """
    sleep(2)
    print (context.driver.current_url)
    assert context.driver.current_url == dic_site[site]


@step('o title do browser deve ter a palavra "{frase:w}"')
def verify_title(context,frase):
    """
    Esta função verifica o title da pagina
    se ela contém a palavra python
    """
    sleep(2)
    assert dic_titles[frase] in context.driver.title
    sleep(1)
    context.driver.quit()
