#language: pt
#Esquema do Cenário

Funcionalidade: Teste no browser Firefox e Chrome

    Esquema do Cenário: Verificar se a pagina foi aberta corretamente no Firefox e Chrome através da url e title
          Dado eu seto o driver do "<browser>" no selenium
          Então entro no site "<site>"
          E a url do browser deve ser "<site>"
          E o title do browser deve ter a palavra "<word>"

    Exemplos:Dados
        |browser|site  |word  |
        |Firefox|python|python|
        |Chrome |python|python|
