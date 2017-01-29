#language: pt
#Cenário simples

Funcionalidade: Teste no browser Firefox e Chrome
    @firefox
    Cenário: Verificar se a pagina foi aberta corretamente pelo Firefox através da url e title
          Dado eu seto o driver do "Firefox" no selenium
          Então entro no site "python"
          E a url do browser deve ser "python"
          E o title do browser deve ter a palavra "python"

    @chrome
    Cenário: Verificar se a pagina foi aberta corretamente pelo Chrome através da url e title
          Dado eu seto o driver do "Chrome" no selenium
          Então entro no site "python"
          E a url do browser deve ser "python"
          E o title do browser deve ter a palavra "python"
