# Tuplas são sequências imutáveis, ou seja, não é possível alterar seu valor após criá-las
# Sintaxe básica
# tupla = ('e1', 'e2', 'e3', 'e4','e5', 'e6')
# Tuplas possuem elementos e índices. Elementos são os valores dentro da tupla. Os índices são os identificadores dos elementos, cada elemento possui seu índice, que começa do 0 até a quantidade de elementos - 1. Logo, se uma tupla tem 50 elementos, o último índice será o 49, representando o último elemento
# Tuplas são úteis em Python quando você precisa de uma coleção ordenada de elementos que não devem ser modificados. 
# Tuplas podem ser escritas com ou sem parênteses, desde que os elementos sejam separados por vírgulas. No entanto, é recomendado e deve-se utilizar parênteses, melhorando a visibilidade.
tupla = ('elemento1', 'elemento2')
tupla = 'elemento1', 'elemento2'
print(tupla)

# Acessando os elementos pelo seu índice
# Como disse anteriormente, cada elemento tem o seu próprio índice. Então vamos ver como isso funciona na prática.
frutas = ('Laranja', 'Maçã', 'Abacate')
# ìndices:    0        1         2
# Para acessar um elemento pelo seu índice, basta seguir a seguinte sintaxe:
# nome_da_sequencia[índice]
frutas[0] # Frutas é o nome da tupla e estamos acessando o índice 0, resultando em Laranja
frutas[2] # Resulta em Abacate, pois está no índice 2
# Laranja tem o índice 0, Maçã 1, Abacate índice 2.

# Também é possível acessar os elementos por índices negativos
frutas = ('Laranja', 'Maçã', 'Abacate')
# índices:   -3        -2       -1
# agora laranja está no índice -3, maçã -2, abacate -1
frutas[-3] # Resultará em laranja


# Acessando a quantidade de elementos com a função len
coordenadas = ('N', 50, 100, -457, -121)
len(coordenadas)


# Tentando alterar o elemento de uma lista
tupla = 'Maria', 'João', 'Pedro'
# tupla[2] = 'Felipe' # Erro



# Tuplas são iteráveis: É possível iterar sobre uma tupla utilizando o loop de repetição for
tupla = ('Pedro')
for letra in tupla:
    print(letra) # P...e...d...r...o


# Empacotamento: Agrupar vários valores a uma tupla
# Empacotamento Explícito: Uma tupla com parênteses
tupla = (1, 2, 3)
print(tupla)  # (1, 2, 3)

# Empacotamento Implícito: Sem parênteses, apenas vírgulas
tupla = 1, 2, 3
print(tupla)  # (1, 2, 3)

# Os valores 1, 2, 3 foram empacotados na tupla.

# Desempacotamento: Extrair os valores de uma tupla e atribuí-los a variáveis únicas
tupla = (10, 20, 30)
a, b, c = tupla
# a = 10
# b = 20
# c = 30

tupla = ('e1', 'e2', 'e3', 'e4', 'e5')
a, *n = tupla
print(a, n)




# Verificando se algum elemento está numa tupla
# in: Verifica se o elemento ESTÁ na tupla e retorna um booleano(True ou False)
tupla = (1, 2, 3, 4, 5)
3 in tupla # 3 Está na tupla? True
'Felipe' not in tupla # Felipe não está na tupla? True





# Tuplas: As tuplas são imutáveis, ou seja, seus elementos não podem ser alterados nem modificados implicitamente (utilizando funções ou métodos para alterar os seus elementos). Um dos motivos para se usar as tuplas é que elas são muito boas quando você não quer alterar os seus elementos. As tuplas, diferentemente das listas, possuem parênteses, e é apenas isso que diferencia uma tupla de uma lista. Mas as tuplas também podem ser escritas sem os parênteses! O python reconhece que quando uma variável possui diversos valores separados por vírgulas, sabe que é uma tupla. Vamos ver um exemplo:
# Uma tupla com os parênteses
tupla = ('elemento1', 'elemento2', 'elemento3')
print(tupla)

# Uma tupla sem os parênteses
tupla = 'elemento1', 'elemento2', 'elemento3'
print(tupla)
# Vamos nos aprofundar mais nas tuplas e ver mais exemplos:
# Criando uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla) # Imprimindo a tupla

# tentando alterar o seu valor
# tupla[2] = 6 # Erro

# Vamos acessar os valores de uma tupla pelo seu índice, funcionam como listas
cores = ('Azul', 'Branco', 'Verde', 'Preto', 'Laranja')
print(cores[1])
print(cores[-2])
print(cores[1:4])

# Unindo tuplas: Agora vamos supor que você tenha duas tuplas e quer junta-lás, mas não sabe como. É possível fazer isso simplesmente utilizando o sinal de adição (+), como se fosse uma expressão matemática. Isso não fará a soma dos elementos da tupla:
tupla1 = (250, 120)
tupla2 = (-35, 90)
tupla = tupla1 + tupla2 # 250, 120, -35, 90
print(tupla) 

# Sobre as tuplas há bem pouco do que falar, elas são quase iguais as listas, mas seus elementos não podem ser alterados implicitamente, isto é, com funções e métodos.