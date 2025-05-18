# FUNÇÕES
# Imagine que você tenha diversos blocos de códigos repetidos ao longo do programa. Isso é muito ruim pois utiliza diversas linhas de código atoa, mas por outro lado é uma bela oportunidade para as funções entrarem no caminho. Funções basicamente são blocos de códigos que são gerenciáveis e tem uma alta facilidade de reúso, evitando a repetição de códigos. Vamos ver como isso funciona:
# Sintaxe básica
# def nome_da_funcao(argumentos/parâmetros opcionais):
#     <bloco de codigos>
# nome_da_funcao(argumentos/parâmetros opcionais)
# Lembrete: Argumentos e parâmetros são usados para se referirem a mesma coisa.


# As funções possuem 3 partes principais:
# - Nome da função: É o que identificará a função
# - Argumentos: São as variáveis da função que serão retornadas e são opcionais.
# - Chamada da função: É a saída da função. Quando é chamada uma função, executará o que estiver dentro da função, ou seja, o bloco de código dentro dela.

# Vamos esclarecer melhor isso:
# Primeiro utilizamos a palavra-chave def, seguido do nome que você quiser atribuir a função e por fim utiliza-se parênteses e os dois pontos (:). Em seguida, dentro do bloco de código indentado que pertence a função, é colocado o que você quiser para quando executar a função, exibir o que está lá dentro. Por fim, fora do bloco de comando da função, é chamada a função, com o nome da função e os parênteses.
def prazer(): # Utiliza-se a palavra-chave def, seguido do nome da função e parênteses.
    print('Olá, Mundo!') # É imprimido 'Olá, Mundo' na tela, mas só será executado quando a função é chamada.
prazer() # Para chamar a função, basta escrever o nome da função seguida por parênteses.
# saída: Olá, Mundo!

# Podemos executar essa função quantas vezes quisermos, basta chamá-las quantas vezes precisar. Cada chamada de função executará o bloco de comando dentro da função.
prazer() # saída: Olá, Mundo!
prazer() # saída: Olá, Mundo!
prazer() # saída: Olá, Mundo!



# Existem dois tipos de funções: as funções sem argumentos/parâmetros (as que não possuem nada dentro dos parênteses) e as funções com argumentos/parâmetros (que possuem uma variável dentro dos seus parênteses)
# Vamos ver novamente uma função sem argumentos:
def oi():
    print("Oi! prazer em te conhecer!")
oi() # saída: Oi! prazer em te conhecer!

def clima():
    print("O clima está chuvoso")
clima() # saída: O clima está chuvoso


# As funções podem imprimir quantos blocos de código forem necessários, não tem limites. Apenas coloque o que deseja que seja impresso dentro do bloco de código da função.
def restaurante():
    print("O garçom está a caminho")
    print("O garçom chegou")
    print("Comemos a pizza")
restaurante() # saída:
"""
"O garçom está a caminho"
"O garçom chegou"
"Comemos a pizza"

"""

# Agora vamos ver uma função com argumentos/parâmetros. A única diferença é que ela possui algo dentro dos seus parênteses.
def prazer(nome): # O argumento da função é nome
    print(f'Oi, {nome}!') # Imprimindo 'Oi, {e o nome da pessoa}'
prazer('Gustavo') # Na chamada da função é especificado o nome da pessoa
prazer('Guilherme')
prazer('Nicolas')
# saída: Oi, Gustavo
# saída: Oi, Guilherme
# saída: Oi, Nicolas


# Mais um exemplo utilizando funções com argumentos:
def exibe_lugar(lugar):
    print(f'Você está em {lugar}')
exibe_lugar('Casa do Tio Bento')
# Primeiramente criamos o nome da função, seu nome é 'exibe_lugar' e tem como parâmetro a variável 'lugar'. Em seguida o bloco de código imprime 'Você está em {e o nome do lugar}'. Chamamos a função e colocamos o parâmetro para 'Casa do Tio Bento'. Então após executar o programa, retornará: 'Você está em Casa Do Tio Bento'


# Mais um exemplo:
def imprime_dobro(lista):
    for elemento in lista:
        print(elemento * 2)
lista = [6, 7, 12, 4, 8]
imprime_dobro(lista)

# Esse código já é um pouco mais complexo, mas vamos entender: Criamos uma função e seu nome é imprime_dobro, ela possui um argumento (lista) e dentro de seu bloco de código, é utilizado uma iteração para cada elemento da lista. Esses elementos individuais são multiplicados por 2, e logo após isso criamos uma lista e atribuímos alguns valores a ela. Logo, chamamos a função com o nome da lista e o programa automaticamente duplicará cada elemento. saída:
"""
12
14
24
8
16
"""


# Tópicos Avançados
# Valores padrão
# Imagine que você crie uma função que possui argumentos. Se você de alguma maneira esquecer de responder ao argumento na chamada de função, isso resultará em um erro. Veja um exemplo:
def informacoes(nome, idade):
    print(f"Seu nome é {nome} e você tem {idade} anos")
# informacoes() # Isso resultaria em um erro pois não foi preenchido aos argumentos da função.
informacoes('Lucas', 25) # Isso executaria o programa normalmente pois você preencheu o argumento que a função pedia.

# Sabendo disso, é possível criar argumentos pre-preenchidos para evitar erros. Vamos entender isso:
def informacoes(nome='usuario', idade=0):
    print(f"Seu nome é {nome} e você tem {idade} anos")
# Ok, vamos entender. Repare nos argumentos da função, dentro dos parênteses. Percebeu que já possui argumentos pre-definidos? nome está pre-definido como 'usuario' e idade está pre-definida como '0'. Então se você de repente esquecer de preencher aos argumentos na chamada da função, por padrão aqueles argumentos pre-definidos serão exibidos, veja só:
informacoes() # Seu nome é usuario e você tem 0 anos
# Mas também ainda é possível preencher seus próprios argumentos:
informacoes('Jorge', 19) # Seu nome é Jorge e você tem 19 anos

# vamos ver mais algum exemplo:
def info(continente='América do Norte', pais='Estados Unidos'):
    print(f'Você está na {continente} em {pais}')
info() # Você está na América do Norte em Estados Unidos^
info('América do Sul', 'Brasil')


# Return
# Como vimos, os blocos de código podem ter qualquer coisa dentro do seu bloco de código, porém utilizamos apenas os comandos print(). Mas existe um comando específico apenas para funções, o return. Pelo seu próprio nome, ele retorna algo. Quando usamos a função print, estamos apenas imprimindo na tela nossa mensagem. Porém a função return retorna um argumento ou qualquer outra coisa que desejar. Vamos ver com um exemplo simples:
def mensagem(nome):
    texto = f'Seu nome é {nome}'
    return texto
print(mensagem('João')) # Seu nome é João
# Para chamar uma função com o return, devemos utilizar o print agora.
# Vamos entender: Criamos a função mensagem com o argumento de nome, dentro do seu bloco de código criamos uma variável texto e atribuímos o seu valor para receber o nome que será digitado na chamada de função, e logo na próxima linha utilizamos o return para retornar aquele texto. Na chamada de função, primeiro utilizamos print() e dentro dos parênteses chamamos a função, definindo o nome para 'João'. A saída deste código é 'Seu nome é João'

# E é apenas isso. Apesar de ser simples, é recomendável que toda função retorne algo. Elas podem retornar textos também, não apenas argumentos. Veja o exemplo a seguir:
def retorna_texto():
    return 'Um exemplo de texto'
print(retorna_texto()) # Um exemplo de texto



# ARGS E KWARGS
# Bom, evoluindo mais em questões sobre as funções, vamos ver sobre args e kwargs. Elas servem especialmente quando você não sabe exatamente quantos argumentos a função terá. Como vimos, as funções tem seus próprios argumentos, ou seja, se definimos 2 argumentos a uma função, então ela terá 2 argumentos, nem mais nem menos. Mas isso muda ao falar sobre args e kwargs, pois isso te permite declarar na chamada da função quantos argumentos você quiser. Vamos ver como isso funciona
# *args
# Permite que uma função receba múltiplos argumentos, muito útil quando não se sabe a quantidade de argumentos que será necessário. Vamos voltar um pouco nas funções normais que recebem um argumento:
def imprime_nome(nome):
    print(f'Seu nome é {nome}')
imprime_nome('Lucas') # saída: Seu nome é Lucas
# Como vimos acima, a função recebeu um argumento, e quando chamamos a função, especificamos o valor do argumento, que era Lucas. Mas imagine só se houvesse uma função que recebe uma fila. Como você sabe, uma fila não tem um número exato de pessoas, pode ser uma fila de 3 pessoas até uma fila de 50 mil, simplesmente não existe um número exato. É nesse momento em que entram as args, quando você não sabe quantos argumentos será necessário. Vamos ver um exemplo:
def fila(*nomes):
    print(f'Está agora na fila: {nomes}')
fila('Maria', 'Pedro', 'Lucas', 'Ricardo', 'João', 'Paulo', 'Emanuel') # Está agora na fila: ('Maria', 'Pedro', 'Lucas', 'Ricardo', 'João', 'Paulo', 'Emanuel')
# !Lembre-se de que os args sempre retornam uma tupla
# Vamos entender o código. Criamos uma função nomeada de fila. Essa função tem o argumento de nomes, e note que há um asterisco neste argumento, indicando que é uma arg. No bloco de código da função é exibida a mensagem 'Está agora na fila {nome da pessoa}' e note que dentro das chaves não é colocado '*nomes' com asterisco, apenas nomes. Na chamada da função, usamos o nome da função e dentro dos parênteses declaramos 7 nomes de pessoas que estão na fila, ou seja, os agrs permitem que você especifique quantos argumentos desejar, diferentemente da função normal que segue um limite de argumentos, nada mais e nada menos que aqueles argumentos que precisam ser especificados.
# Vamos ver mais um exemplo:

def linguas(*idiomas):
    print(f'Você sabe falar {idiomas}')
linguas('Inglês', 'Espanhol', 'Coreano')
# A regra segue a mesma aqui, declaramos a função linguas que recebe como argumento args de idiomas, imprimindo 'Você sabe falar {e as linguas}', seguida da chamada da função, que declaramos 3 argumentos: Inglês, Espanhol e Coreano. Então a saída desta função será:
# Você sabe falar ('Inglês', 'Espanhol', 'Coreano')
# Entendeu bem as *args? Então vamos para as **kwargs!


# As kwargs são muito parecidas com as *args, porém a única diferença é que as kwargs possuem dois asteriscos e seus argumentos na chamada de função são diferentes. Vamos ver a um exemplo:
def loja(**produtos):
    print(f'A loja possui {produtos}')
loja(iphone = 3400, tablet = 2100, tv = 4500)
# Você conseguiu notar alguma coisa diferente, comparando com as args? Vamos lá, a primeira coisa foram os dois asteriscos no argumento produtos, indicando que isso é uma kwarg. Na chamada de função, as coisas são um pouco diferentes. Você deve especificar a chave e o valor daquele argumento que está criando. Nesse caso, a nossa chave é o nome do produto, e o valor dessa chave é o valor do produto. iphone = 3400 indica que a chave é 'iphone' e '3400' é o valor. Isso te lembra algo?... Chave... Valor...? As args retornam uma tupla, e as kwargs retornam um dicionário!
# Vamos ver mais um exemplo:


def informacoes(**dados):
    print(dados)
informacoes(Lucas = 12, Pedro = 56,  Maria = 35,  João = 16)
# Agora criamos um dicionário, onde o primeiro argumento é o nome da pessoa seguido da idade dela.


# ESCOPO
# Quando você declara uma variável em qualquer lugar que não seja dentro do bloco de código de uma função, então essa variável é global. Isso significa que essa variável pode ser utilizada aonde quer que seja, dentro de qualquer estrutura, como estruturas condicionais, loops, e até mesmo nas próprias funções! Porém, ao declarar uma variável DENTRO do bloco de código de uma função, então essa variável não passa mais ser uma variável global, mas sim uma variável local. Variáveis locais são todas as variáveis que são declaradas DENTRO de funções. Ok, mas por que isso importa? Há uma grande diferença entre variáveis de escopo global e local, e isso pode causar uma grande confusão no programa. Primeiramente, vamos ver um exemplo de uma variável global e uma variável local:
# Variável global
variavel = 'global'

# variavel local
def funcao():
    variavel = 'local'

# Ok, mas qual o problema disso? Vamos ver um exemplo muito confuso para você entender qual o perigo das variáveis locais:
variavel = 'global'

def funcao():
    variavel = 'local'
    return variavel
print(funcao()) # local
print(variavel) # global

# Vamos entender esse código. Primeiro declaramos uma variável com o nome de variavel e atribuímos seu valor a 'global', logo após isso criamos uma função, dentro dela CRIAMOS outra variável, com o mesmo nome, porém agora atribuímos o seu valor para 'local', e então utilizamos o return para retornar a variável dentro da função. Então utilizamos o print() e dentro de seus parênteses chamamos a função, que por sua vez retornou o valor da variável dentro da função, que era 'local', o que imprimiu 'local'. E depois disso utilizamos o print, e imprimimos o valor da variável global, que estava fora da função, e retornou 'global'. Isso é muito perigoso, pois pode causar muitos problemas no seu programa.