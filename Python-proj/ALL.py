









# Listas são um tipo de dado (como os inteiros, booleanos, strings), mais especificamente, são sequências ordenadas e mutáveis (É possível alterar seus elementos) e possuem índices. Seus elementos são cercados por colchetes [] e cada elemento é separado por vírgulas. O índice é o identificador de um elemento, e começa do 0 até a quantidade de elementos - 1. Por exemplo, se uma lista tem 50 elementos, o primeiro índice será 0 e o último será a quantidade -1, que é 49.
# sintaxe básica
# lista = ['e1', 'e2', 'e3']

# Enquanto valores ficam espalhados por aí, listas 'juntam' tudo ->
# Exemplo muito ruim de usuários espalhados pelo programa
usuario1 = 'João Ferreira'
usuario2 = 'Felipe Almeida'
usuario3 = 'Julio Alberto'
usuario4 = 'Lucas Golmes'
# Exemplo muito bom e recomendável de uma lista de usuários que junta todos os usuários
usuarios = ['João Ferreira', 'Felipe Almeida', 'Julio Alberto', 'Lucas Golmes']


# Começando a entender as listas
# Vamos começar a declarar uma lista com 3 elementos:
lista = ['elemento1', 'elemento2', 'elemento3']
# índices:    0            1            2
# Repare que o índice começa sempre no primeiro elemento, e começa do índice 0. Como já disse anteriormente, os índices são como IDs para os elementos, você pode acessar um elemento pelo seu índice.
# Acessando os elementos pelo índice
# Para acessar um elemento pelo seu índice, basta seguir a seguinte sintaxe:
# nome_da_lista[índice]
# Sabendo que os índices iniciam em 0, vamos tentar acessar o elemento1 utilizando o seu índice:
print(lista[0]) # a saída desse comando será 'elemento1', pois ela está no índice 0.
# Acessando o elemento 2, que está no índice 1
print(lista[1])
# Acessando o elemento 3, que está no índice 2
print(lista[2])

# Um pouco chato acessar cada elemento pelo seu índice individualmente, que tal acessar todos os elementos de uma vez? Basta imprimir o nome da lista:
print(lista)

# Listas também aceitam diferentes tipos de dados: Sejam strings, booleans, inteiros e floats, listas armazenam todos esses valores:
lista = ['Pedro', 15, True, 'Maria', False]
# índices   0     1     2      3       4
# Acessando novamente um elemento pelo seu índice:
print(lista[3]) # Maria

# Algumas funções de listas
# Listas possuem funções, e isso é muito bom, pois com funções as listas ganham muitas funcionalidades. Vamos ver algumas delas:
# Imagine que você tem uma lista enorme de vendas, e por algum motivo quer saber qual é o MAIOR número da lista, o número mais grande do que todos os outros. Você pode fazer isso utilizando a função max():
vendas = [120, 456, 123, 986, 965, 329, 943, 542, 239, 236, 823, 967, 327, 432, 534, 976, 321, 743, 658, 735, 885, 364, 785, 984, 651, 798]
# Essa lista é relativamente grande, e ée difícil achar o maior númro logo de cara, então vamos utilizar a função max:
# sintaxe:
# max(nome-da-lista)
print(max(vendas))
# Bem fácil, não é? Agora como achar o menor número da lista? Podemos achar facilmente utilizando a função min():
# sintaxe: min(nome-da-lista)
print(min(vendas))
# Bem fácil também! que tal ver mais um exemplo?

# Queremos achar a maior idade e a menor idade nesta lista:
idades = [34, 12, 43, 65, 86, 87, 21, 33, 43, 90, 32, 43, 45, 15, 56, 23, 54, 43, 7, 8]
print(max(idades)) # Imprimindo o maior valor
print(min(idades)) # Imprimindo o menor valor


# Também é possível somar os elementos de uma lista, sim!!! Vamos ver como funciona:
# Vamos supor que você tem a tarefa de somar todas as notas de 15 alunos de uma escola, uma tarefa bem fácil! Vamos ver:
notas = [8, 9, 1, 4, 5, 6, 7, 4, 4, 5, 7, 10, 2, 4, 8]
# para somar todos os valores, utiliza-se a função sum(nome-da-lista):
print(sum(notas))
# Muito fácil também, concorda??



# Agora pense que você está fazendo uma festa de aniversário. Você anotou o nome de todos os seus amigos que vão à festa, porém a lista é gigantesca! Será uma super festa! Sua tarefa é saber a quantidade de pessoas que vão à festa, você já tem o nome das pessoas, e quer saber quantas pessoas são. Então para essa tarefa utilizaremos a função len(nome-da-lista):
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karine", "Lucas", "Maria" "Nicolas", "Olivia", "Patrick", "Heliezer", "Rafael", "Sofia", "Tiago", "Jorge", "Vitória", "William", "Maria", "Roberto", "Julia", "Amanda", "Bruna", "Caio", "Matheus"]
# Muitos itens, não é mesmo? Vamos descobrir quantos amigos terá na festa utilizando a função len(nome-da-lista):
print(len(nomes))




# Vamos supor que você quer acessar o último elemento de uma lista, mas a lista é gigante. É aí que entram os índices negativos.
# índices negativos são iguais aos índices positivos normais mas agora ocorre uma inversão. O último índice é o -1 e o primeiro depende de quantos elementos uma lista tem. Vamos criar a seguite lista:
cores = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'violeta', 'roxo', 'marrom', 'preto', 'branco', 'cinza', 'rosa', 'bege']
# negativos  -13       -12         -11      -10       -9        -8       -7       -6        -5       -4       -3       -2      -1
# a lista é enorme, e você quer acessar o último elemento, o bege.
# para isso, basta colocar o índice -1, pois -1 sempre será o último elemento de toda e qualquer lista, não importa o seu tamanho.
cores[-1] # bege



# Você já sabe acessar elementos pelos seus índices, mas e se você quisesse acessar múltiplos elementos de uma lista? É até possível acessar elemento por elemento, mas esse jeito é um pouco demorado e utiliza muitas linhas de código. Mas é por isso que surgiu a fatiação de listas.
# FATIAÇÃO DE LISTAS: Permite acessar múltiplos elementos de uma só vez!
# sintaxe básica:
# nome_da_lista[índice_de_inicio:índice_de_fim]
# Veja a seguinte lista:
materiais = ['Ferro', 'Madeira', 'Metal', 'Concreto', 'Pedra']
# índices:      0         1         2         3          4
# Vamos supor que eu quero acessar a Madeira, o Metal e o Concreto.
# Sem a fatiação de listas:
materiais[1]
materiais[2]
materiais[3]

# Com a fatiação de listas:
materiais[1:4]
# Repare que sem a fatiação acessamos individualmente os elementos de índice 1, 2 e 3. Mas já na fatiação acessamos do índice 1 até o índice 4. É aqui que surgem muitas dúvidas. Ao fatiar uma lista, você deve especificar o ínicio e o fim, ou seja, aonde que começa a acessar a lista até aonde para de acessar a lista, porém no índice de fim, sempre é escrito o índice final somando + 1.
# Vamos ver mais exemplos

minerios = ['Diamante', 'Ferro', 'Ouro', 'Cobre']
# índices:      0          1       2        3
# Vamos supor que queremos acessar o Diamante, o Ferro e o ouro
# Sem a fatiação:
minerios[0]
minerios[1]
minerios[2]

# Com a Fatiação:
minerios[0:3]
# Ou você pode fazer isso (não é recomendável, mas pode ser útil para aprendizado)
minerios[0:2+1]
# O resultado é o mesmo

# Também existe a fatiação de listas com o índice inverso
animais = ['Gato', 'Coruja', 'Aranha', 'Escorpião']
# índices:   -4       -3        -2         -1
# vamos supor que queremos acessar a coruja e a aranha
# segue a mesma regra do que a fatiação com índices positivos
animais[-3:-1] # Começa a fatiar do índice -3, e para até o -2.
# A mesma fatiação pode ser feita assim:
animais[-3:-2+1] # Vamos pensar: Começa do índice -3, acessa a coruja. Depois vai para o índice -2 e acessa a Aranha, e para por aí.
# Fatiação com índices negativos é mais complexo do que fatiação a fatiação tradicional com índices positivos. Então sempre que puder utilize fatiação com índices positivos, é menos confuso e é mais fácil de compreender.



# Alterando os elementos da lista
# Você pode alterar os elementos de uma lista tanto explicitamente (alterar direto a lista) quanto alterar implicitamente (utilizar funções do python que modifiquem os elementos de uma lista). Vamos apresentar como alterar listas implicitamente, ou seja, utilizando funções.
# Visualize a lista a seguir:
automoveis = ['Carro', 'Caminhão', 'Moto', 'Bicicleta']
# Analisando, há um item errado na lista. Bicicleta não é um automóvel, então podemos utilizar as funções de lista. Você deve estar se perguntando: Mas por que não apago o elemento simplesmente apagando pela lista?
# Ao usar as funções de lista, você evita confusões. É muito usado em loops e em condições (Assuntos mais avançados), quando você executar um programa, você não consegue simplesmente apagar ou adicionar manualmente elementos. O programa pode fazer essa tarefa para você, permitindo que você alcance a sua tarefa.
# Voltando a explicação... Vamos supor que queremos remover o elemento 'Bicicleta' da lista, pois ele não é um automóvel.
# utilizamos a função .remove('elemento')
# vamos ver como funciona:
automoveis.remove('Bicicleta')

# É só isso! Já podemos remover elementos de uma lista!
# Vejamos outros exemplos:
materias = ['Geografia', 'Tijolo', 'Artes', 'Matemática', 'Parede']
# Que estranho, concorda? Tijolo e Parede são matérias escolares? Então vamos remové-los!
materias.remove('Tijolo')
materias.remove('Parede')

# Simples, né?
# Podemos remover qualquer elemento de uma lista utilizando o índice!
frutas = ['Maçã', 'Banana', 'Laranja', 'Kiwi', 'Massinha', 'Abacaxi', 'Slime']
# índices:  0        1          2        3         4           5         6
# nome_da_lista.pop(índice)
frutas.pop(4)
# Removemos o elemento do índice 4, que era Massinha
# podemos remover também o último elemento, sem colocar o índice entre os parênteses:
frutas.pop() # Remove o último elemento
frutas.pop(-1) # Também é possível fazer isso, resultando na mesma coisa

# ADICIONANDO ELEMENTOS
# Vamos supor que você queria adicionar algum elemento em uma lista. Veja por exemplo, a seguinte lista:
estados_sul = ['Paraná', 'Rio Grande do Sul']
# Está faltando Santa Catarina, e para isso podemos utilizar a função append, vamos ver:
# sintaxe:
# lista.append('elemento')
estados_sul.append('Santa Catarina')
# Siples demais! Mas uma coisa importante a lembrar é que a função append sempre adiciona os elementos no último índice ou seja, após adicionar um elemento, esse elemento passa a ser o último elemento
# Vamos ver outros exemplos
IAs = ['ChatGPT', 'DeepSeek', 'Grok']
# Queremos adicionar Sider, já sabe como?
IAs.append('Sider')
print(IAs)
# Moleza!

# E também podemos adicionar elementos no índice que quisermos!
# A função insert te permite adicionar um elemento no índice que desejar, mas sem substituir o elemento que estava naquele índice.
# Veja alguns exemplos:
mamiferos = ['Baleia', 'Morcego']
# índices       0          1
# queremos adicionar 'Humano' no índice 1, logo após o índice 0 que está sendo ocupado pelo elemento 'Baleia'. Se adicionarmos o elemento 'Humano' no índice 1, o Morcego não será substituído, mas sim ocupará o próximo índice, que é o índice 2. Vamos ver na prática:
# sintaxe básica:
# lista.insert(indice, elemento)
mamiferos.insert(1, 'Humano') # Estamos inserindo 'Humano' no índice 1.
# A lista agora está assim:
mamiferos = ['Baleia', 'Humano', 'Morcego']
# Bem fácil, não acha? Mas não esqueça que insert NÃO subtitui um elemento, mas sim 'joga' os elementos para frente, É como se o insert fosse uma pessoa e estivesse pulando a fila do supermercado, mas sem empurrar a pessoa que estava atrás dele.

# Vamos ver mais um último exemplo para fixar!
fila = ['Pessoa1', 'Pessoa2', 'Pessoa3', 'Pessoa4', 'Pessoa5']
fila.insert(1, 'Furão de Fila') # O Furão de Fila furou e entrou no lugar 2!
print(fila)

# Também existe outra forma de alterar um elemento pelo seu índice
# Esta forma agora sim SUBSTITUI um novo elemento pelo antigo elemento. Vamos ver como funciona
compras = ['Tomate', 'Sabonete', 'Detergente', 'Abacaxi', 'Laranja']
# índices     0          1            2            3           4
compras[3] = 'Abacate'
# Estamos alterando o elemento do índice 3, que era 'Abacaxi', e que agora passa a ser 'Abacate'
# Então quando você quer SUBSTITUIR um elemento que já existia na lista por outro novo elemento, utilize esse método.

# Vamos fazer o exemplo da fila denovo!
fila = ['Pessoa1', 'Pessoa2', 'Pessoa3', 'Pessoa4', 'Pessoa5']
# índices   0          1           2         3           4
fila[1] = 'Intrusor' # Agora sim, o Intrusor empurra a pessoa2 e ela sai da fila


# Juntando listas
# Já pensou juntar listas para criar uma nova lista? Com o python isso é possível, utilizando a função extend! Vamos ver como funciona!
# Vamos supor que temos duas listas, e queremos unir todas em apenas uma, veja o exemplo:
# sintaxe básica:
# lista1.extend(lista2)
planetas = ['Terra', 'Marte', 'Vênus']
estrelas = ['Sol', 'Sagittarius A']
planetas.extend(estrelas) # planetas agora possui os elementos: ['Terra', 'Marte', 'Vênus', 'Sol', 'Sagittarius A']

# Também é possível juntar listas utilizando o operador de adição +
sucos = ['Laranja', 'Limão', 'Abacaxi']
refrigerantes = ['Coca-Cola', 'Pepsi']
print(sucos + refrigerantes)
# Escolher entre a função extend e juntar utilizando o operador de adição é que o extend já é próprio para fazer isso, então é mais recomendado.


# Organizando listas
# Imagine que você tenha uma lista toda embaralhada, e precisava colocar em ordem alfabética ou númerica essa lista? Seria trabalhoso, não é? Mas graças a função sort, você consegue organizar sua lista em ordem crescente! Vamos ver isso na prática:
# sintaxe: lista.sort()
letras = ['c', 'd', 'y', 'w', 'b', 'a', 'z', 'j', 'o', 'r', 'f', 't']
letras.sort() # Prontinho, a sua lista já está toda organizada em ordem alfabética!
print(letras)

# Um exemplo em ordem númerica crescente
numeros = [4, 8, 12, 5, 9, -4, 0, 5, 6, -6, 120, 450, 32, 21, 7]
numeros.sort() # Lista organizada
print(numeros) 

# OK, mas e se precisar ordenar em ordem decrescente?
# Simples, apenas utilize a função reverse! Veja como fica:
nomes = ['Pedro', 'João', 'Maria', 'Zazu', 'Antônio']
nomes.sort() # Primeiro ordenamos a lista normalmente
nomes.reverse() # Depois invertemos a ordem, ficando em ordem decrescente!
print(nomes)


# Imagine que você tem a tarefa de verificar quantas vezes um produto especifico foi vendido num mercadinho no mês de fevereiro. O gerente do mercadinho te envia a seguinte lista para analisar:
produtos = ['Salgadinhos', 'Arroz', 'Tomate', 'Refrigerante', 'Feijão', 'Açúcar', 'Salgadinhos', 'Arroz', 'Arroz', 'Arroz', 'Sal', 'Banana', 'Arroz', 'Salgadinhos', 'Chocolate', 'Cerveja', 'Óleo', 'Cerveja', 'Cerveja', 'Macarrão', 'Arroz', 'Banana', 'Leite', 'Arroz', 'Açúcar', 'Óleo', 'Refrigerante', 'Arroz', 'Óleo', 'Balas', 'Açúcar', 'Chocolate', 'Refrigerante', 'Leite', 'Óleo', 'Manteiga', 'Arroz', 'Refrigerante', 'Arroz', 'Manteiga', 'Arroz', 'Sal', 'Manteiga', 'Cerveja', 'Leite', 'Iogurte', 'Balas', 'Sal', 'Cerveja', 'Sal', 'Leite', 'Arroz', 'Arroz', 'Arroz', 'Salgadinhos', 'Macarrão', 'Sal', 'Arroz', 'Leite', 'Arroz', 'Arroz', 'Açúcar', 'Tomate', 'Arroz', 'Arroz', 'Sal', 'Arroz', 'Banana', 'Banana', 'Tomate', 'Manteiga', 'Cerveja', 'Óleo', 'Refrigerante', 'Feijão', 'Feijão', 'Arroz', 'Iogurte', 'Feijão', 'Chocolate', 'Feijão', 'Arroz', 'Arroz', 'Açúcar', 'Cerveja', 'Salgadinhos', 'Arroz', 'Arroz', 'Cerveja', 'Arroz', 'Macarrão', 'Macarrão', 'Feijão', 'Chocolate', 'Tomate', 'Tomate', 'Iogurte', 'Óleo', 'Chocolate', 'Arroz', 'Manteiga', 'Iogurte', 'Iogurte']# Como já dito, sua tarefa é verificar quantas vezes um produto foi vendido. O gerente do mercadinho disse para verificar quantas vezes 'Arroz' foi vendido. E aí? Vai contar um por um ou vamos utilizar uma função que faz isso em segundos??
# Como já dito, sua tarefa é verificar quantas vezes um produto foi vendido. O gerente do mercadinho disse para verificar quantas vezes 'Arroz' foi vendido. E aí? Vai contar um por um ou vamos utilizar uma função que faz isso em segundos??
# Quando você quer contar algum elemento, ou seja, verificar quantas vezes ele aparece numa lista, utilizamos a função .count():
# sintaxe: lista.count('elemento')
print(produtos.count('Arroz')) # saída: 27



# Operadores de pertencimento
# Os operadore de pertencimento verificam se um valor está contido ou não está contido em uma sequência ou coleção (como listas, strings, dicionários, etc). Vamos ver um exemplo:
# Verificamos se um elemento ou valor está presente na lista utilizando as palavras-chave in e not in. Vamos ver como funciona:
# Primeiro criamos uma lista
passaros = ['Tucano', 'Bem-te-vi', 'Quero-Quero']
# Logo em seguida vamos verificar se algum valor está presente na lista utilizando a palavra-chave 'in':
'Tucano' in lista # Tucano está na lista? O programa verifica e retorna o booleano True
# Agora vamos verificar se algum valor NÃO está na lista:
'Pombo' not in lista # Pombo não está na lista? O programa analisa e retorna um booleano, nesse caso, True.



"""
# count('elemento'): Retorna o número de vezes que um elemento aparece numa lista
nomes.count('Felipe')

# index('elemento'): Retorna qual o índice em que um elemento está
nomes.index('João')

# copy: Permite que outra lista tenha o mesmo valor que a original
nomes2 = nomes.copy()

# del: Deleta um elemento ou a própria lista
"del nomes[1]" # deleta o elemento do índice 1
"del nomes" # deleta toda a lista

# clear: Limpa todos os elementos de uma lista, deixando-a vazia.
nomes.clear()

# in e not in: Verifica se algum elemento está presente na lista
'Felipe' in nomes
'Marcia' not in nomes

# extend: Junta duas listas
alunos = ['João', 'Letícia', 'Pedro']
notas = [6, 4, 9]
alunos.extend(notas)
"""




# Desempacotamento de listas
# O desempacotamento de listas é utilizado quando você quer atribuir diversas variáveis para cada elemento da lista. Vamos supor que eu tenho uma lista chamada nomes e apresenta os seguintes nomes: 'João', 'Felipe', 'Fábio'; E eu quero atribuir uma variável para cada um desses nomes. Vamos ver como isso é feito:
lista = ['João', 'Felipe', 'Fábio']
user001, user002, user003 = lista # Agora cada variável dessa possui o seu respectivo elemento da lista, ou seja, user001 armazena o valor 'João', user002 armazena 'Felipe' e user003 armazena 'Fábio'
print(user001) # user001 = 'João'
print(user002) # user002 = 'Felipe'
print(user003) # user003 = 'Fábio'

# Mas esse tipo de desempacotamento pode gerar erros, um dos motivos é que há chances de ter 5 elementos na lista e você ter declarado apenas 4 variáveis e na hora de desempacotar os elementos isso retornará um erro, pois o número de elementos é diferente do número de desampacotamento de variáveis. Mas podemos corrigir isso utilizando o asterisco. Vamos ver:
# Uma lista com 5 elementos, mas possui apenas duas variáveis:
lista = ['Pedro', 'Maria', 'João', 'Felipe', 'Jorge']
user1, *users = lista
print(user1) # Pedro
print(users) # ['Maria', 'João', 'Felipe', 'Jorge']
# vamos enteder, declaramos uma lista onde ela possui 5 elementos, e em seguida, criamos a variável user1, que se refere ao elemento 'Pedro' da lista, e a variável users com um asterisco. Por incrível que pareça, isso não resulta em um erro, mas todo o segredoe está no asterisco. Quando você desempacota utilizando uma variável com um asterisco, isso significa que agora a variável com asterisco está armazenando todos os elementos após o 'Pedro', pois já está sendo ocupado pelo user1. Ou seja, users está armazenando 'Maria', 'João', 'Felipe' e 'Jorge'! Vamos ver mais um exemplo:

frutas = ['Melancia', 'Abacaxi', 'Maçã', 'Laranja']
fruta1, *frutas_restantes = frutas
print(fruta1) # Melancia
print(frutas_restantes) # ['Abacaxi', 'Maçã', 'Laranja']
# Agora fruta1 está armazenando Melancia e frutas_restantes está armazenando os elementos restantes da lista, que são: ['Abacaxi', 'Maçã', 'Laranja']

# Também é possível utilizar o asterisco como a primeira variável, então ela armazenará os primeiros elementos da lista:
animais = ['Tubarão', 'Crocodilo', 'Gato', 'Morcego']
*inicio, fim = animais
print(inicio) # ['Tubarão', 'Crocodilo', 'Gato']
print(fim) # Morcego
# Agora como a ordem foi alterada, a variável inicio possui os primeiros elementos da lista, e o fim possui o último elemento da lista, que é o Morcego.


# Tuplas em Python

# Tuplas são coleções de dados que, ao contrário das listas, não podem ser modificadas depois de criadas.
# São úteis quando você quer garantir que os dados permaneçam os mesmos.

# Criando tuplas
tupla1 = ('elemento1', 'elemento2')  # Forma mais comum, usando parênteses
tupla2 = 'elemento1', 'elemento2'    # Também funciona sem parênteses
print(tupla1)
print(tupla2)

# Índices em tuplas
# Cada elemento da tupla tem uma posição (índice), começando do zero
frutas = ('Laranja', 'Maçã', 'Abacate')
# Índices:     0        1        2

# Acessando elementos pelos índices
print(frutas[0])  # Acessa o primeiro elemento: Laranja
print(frutas[2])  # Acessa o terceiro elemento: Abacate

# Índices negativos acessam do fim para o começo
print(frutas[-1])  # Último elemento: Abacate
print(frutas[-2])  # Penúltimo elemento: Maçã

# Descobrindo o tamanho da tupla com len()
coordenadas = ('N', 50, 100, -457, -121)
print(len(coordenadas))  # Retorna 5, pois há 5 elementos

# Tuplas são imutáveis
# Após a criação, não é possível mudar os valores
tupla = ('Maria', 'João', 'Pedro')
# tupla[2] = 'Felipe'  # Isso causaria um erro, pois não se pode alterar tuplas

# Tuplas são iteráveis
# Podemos percorrer seus elementos usando um loop
nome = ('Pedro')  # Isso é uma string, não uma tupla com um elemento
for letra in nome:
    print(letra)  # Vai imprimir letra por letra: P, e, d, r, o

# Empacotamento de tupla
# Podemos armazenar múltiplos valores em uma variável
tupla = (1, 2, 3)
print(tupla)

# Também é possível empacotar sem parênteses
tupla = 4, 5, 6
print(tupla)

# Desempacotamento de tupla
# Podemos extrair os valores da tupla para variáveis separadas
tupla = (10, 20, 30)
a, b, c = tupla
print(a)  # 10
print(b)  # 20
print(c)  # 30

# Podemos usar o operador * para capturar múltiplos valores em uma variável
tupla = ('e1', 'e2', 'e3', 'e4', 'e5')
a, *resto = tupla
print(a)      # 'e1'
print(resto)  # ['e2', 'e3', 'e4', 'e5'] → repara que o "resto" vira uma lista

# Verificando a existência de um valor na tupla
tupla = (1, 2, 3, 4, 5)
print(3 in tupla)         # Retorna True, pois 3 está na tupla
print('Felipe' not in tupla)  # Retorna True, pois 'Felipe' não está na tupla

# Unindo tuplas com o operador +
# Isso cria uma nova tupla com os elementos das duas
tupla1 = (250, 120)
tupla2 = (-35, 90)
tupla3 = tupla1 + tupla2
print(tupla3)  # Resultado: (250, 120, -35, 90)

# Fatiamento de tuplas (igual listas)
# Podemos acessar fatias da tupla, definindo início e fim
cores = ('Azul', 'Branco', 'Verde', 'Preto', 'Laranja')
print(cores[1])     # Acessa o segundo elemento: Branco
print(cores[-2])    # Acessa o penúltimo elemento: Preto
print(cores[1:4])   # Acessa os elementos do índice 1 ao 3: ('Branco', 'Verde', 'Preto')

# Conclusão
# Tuplas são úteis quando queremos armazenar dados que não devem mudar.
# Elas se parecem com listas, mas não possuem métodos de modificação como append ou remove.
# Por serem imutáveis, são mais seguras e podem ser usadas como chave de dicionários, por exemplo.


#   -   -   -   -   -   -   Sets  -   -   -   -   -   -   -   -   -   -   
# Sets são sequências desordenadas(Não possuem uma ordem especifica, a ordem de seus elementos é aleatória) e são muito úteis em situações específicas. Os sets, diferentemente das listas, possuem chaves, e cada elemento também é separado por vírgulas. Os sets não aceitam valores repetidos, isso é muito bom para eliminar todos os valores de uma lista comum, por exemplo. Vamos ver um exemplo:
lista = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'b', 'b', 'c']
lista = set(lista)
lista = list(lista)
print(lista) # ['a', 'b', 'c']

# Vamos mergulhar no mundo dos sets!
# Vamos supor que queremos fazer um bolo. Alguém muito inexperiente em culinária separou os igredientes, veja:
igredientes = {'Farinha', 'Trigo', 'Madeira', 'Alface'}
# índices          0         1         2          3
print(igredientes)

# Você vê os igrediente e se pergunta: "Por que Madeira e Alface estão entre os igredientes?" Você precisa achar algum jeito de remove-los! Por sorte existe a função remove, vamos ver!

# a função remove é responsável por remover algum elemento dentro de um set. Basta dizer o nome do elemento e ele será removido. Vamos remover os igredientes que não fazem sentido:
# sintaxe: set.remove('elemento')
igredientes.remove('Madeira')
print(igredientes) # {'Farinha', 'Alface', 'Trigo'}
# Isso! Removemos a Madeira! Agora vamos remover o Alface! 
igredientes.remove('Alface')
print(igredientes) # {'Farinha', 'Trigo'}

# Ok, o bolo está com apenas dois igredientes, precisamos de mais! Vamos adicionar o fermento!
# Podemos adicionar um elemento com a função add. Ficaria assim:
igredientes.add('Fermento')
print(igredientes) # {'Trigo', 'Farinha', 'Fermento'}
# Ainda faltam igredientes, vamos adiconar mais!
igredientes.add('Açucar')
igredientes.add('Ovos')
igredientes.add('Leite')
igredientes.add('Manteiga')
print(igredientes) # {'Açucar', 'Farinha', 'Fermento', 'Ovos', 'Trigo', 'Leite', 'Manteiga'}
# Ah, agora sim! Já temos todos os igredientes!


# Imagine agora temos um set que possui algumas frutas dentro dele:
frutas = {'Maçã', 'João', 'Banana', 'Pedro', 'Vinicius', 'Abacaxi', 'Limão', 'Felipe', 'Macarrão', 'Peixes'}
# Mas espera. Essa lista está cheia de coisas que não são frutas! Podemos remover cada elemento um por um, mas isso seria trabalhoso. Uma maneira mais fácil é limpar a lista toda de uma vez e utilizar a função add para adicionar novas frutas posteriormente.
# Limpando a lista
# Com os sets é possível limpar a lista utilizando a função clear:
# sintaxe: set.clear()
frutas.clear()
print(frutas) # set() Isso mostra que o set está vazio e não possui nenhum elemento. Ótimo, agora vamos adicionar os elementos na lista

frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Limão')
frutas.add('Abacaxi')
print(frutas) # {'Banana', 'Maçã', 'Limão'}

# Para ter certeza, vamos verificar se os elementos estão no set:
print('Maçã' in frutas) # True
print('Banana' in frutas) # True
# E também vamos verificar se os elementos antigos não estão mais no set:
print('Vinicius' not in frutas) # True
print('Pedro' not in frutas) # True

# Perfeito, só faltou verificar quantas frutas nosso set possui. Vamos fazer isso utilizando a função len
quantidade = len(frutas)
print(quantidade) # 4

# Ótimo, isso mostra que os sets são muito poderosos e apresentam muitas funcionalidades!


# DICIONÁRIOS EM PYTHON 🧠🍉

# Dicionários são mutáveis como listas, mas usam CHAVES em vez de índices.
# Cada chave aponta para um VALOR, formando pares únicos de chave-valor.

# Exemplo: estamos no mercado! 🛒
frutas = {
    'Maçã': 0.99,
    'Laranja': 1.39,
    'Abacaxi': 1.99
}
print(frutas)

# Podemos escrever o dicionário numa linha só também:
frutas = {'Maçã': 0.99, 'Laranja': 1.39, 'Abacaxi': 1.99}

# Dicionários funcionam muito bem para dados únicos! 👤
dados_pessoais = {
    'João Lucas': 14,
    'Maria Fernanda': 23,
    'Alexandre Ferreira': 37
}
# Mas cuidado: nomes podem se repetir! Melhor usar CPF, ID ou telefone.

# Vamos ver como acessar dados no dicionário:
dados = {
    1: 'Henrique da Costa',
    2: 'Felipe dos Santos',
    3: 'Arthur Feitosa',
    4: 'Marcos Teixeira',
    5: 'Fábio Alberto'
}

print(dados[2])  # Felipe dos Santos
print(dados[5])  # Fábio Alberto

# Alterando valores:
dados[3] = 'Marco Antônio'  # Substitui valor da chave existente
dados[6] = 'Luiza Moura'    # Adiciona novo par chave-valor
print(dados)

# Deletando pares chave-valor:
del dados[2]
del dados[4]
print(dados)

# Acessando chaves, valores e itens:
chaves = dados.keys()
valores = dados.values()
itens = dados.items()

print(chaves)
print(valores)
print(itens)

# Verificando se existe uma chave ou valor:
print(1 in dados)  # True
print('Fábio' in dados.values())  # False (valor completo é 'Fábio Alberto')
print('Henrique' not in dados.values())  # True

# Dicionário dentro de outro dicionário 😮
pessoas = {
    'João Miguel': {
        'idade': 14,
        'cidade': 'Cidade dos Astronautas',
        'rua': 'Rua dos Capixabas'
    },
    'Lucas Ferreira': {
        'idade': 23,
        'cidade': 'Cidade do Folclore',
        'rua': 'Rua dos Caçadores'
    }
}
print(pessoas['João Miguel']['idade'])  # 14

# Outro exemplo simples:
compras = {
    'Arroz': 3.45,
    'Feijão': 2.90,
    'Macarrão': 4.50
}
print(compras)
print(compras['Arroz'])  # 3.45

# Modificando valores:
compras['Sushi'] = 1.35      # Adiciona novo item
compras['Macarrão'] = 0.35   # Atualiza valor existente

# Funções úteis com dicionários:
frutas = {
    'Maçã': 3.99,
    'Laranja': 4.99,
    'Limão': 2.99,
    'Abacaxi': 1.99,
    'Manga': 1.59
}

# del: remove um par chave-valor
del frutas['Abacaxi']
print(frutas)

# popitem(): remove o último par adicionado
frutas.popitem()
print(frutas)

# pop(): remove pela chave
frutas.pop('Maçã')
print(frutas)

# get(): acessa valor de forma segura
print(frutas.get('Limão', 'Fruta não encontrada'))     # 2.99
print(frutas.get('Pêra', 'Fruta não encontrada'))      # Fruta não encontrada

# in / not in: operadores de verificação
print('Laranja' in frutas)     # True
print('Tomate' not in frutas)  # True

# clear(): limpa todo o dicionário
frutas.clear()
print(frutas)  # {}

# Acessando chaves, valores e itens de novo:
compras = {
    'Arroz': 3.45,
    'Feijão': 2.90,
    'Macarrão': 4.50,
    'Sushi': 1.35
}
print(compras.keys())    # dict_keys(['Arroz', 'Feijão', 'Macarrão', 'Sushi'])
print(compras.values())  # dict_values([3.45, 2.9, 4.5, 1.35])
print(compras.items())   # dict_items([('Arroz', 3.45), ...])

# Vamos fazer uma análise com notas de alunos 📚
alunos = {
    'João': 7.90,
    'Mariane': 5.60,
    'Cristopher': 8.55,
    'Lucas': 4.50
}
# Total de notas:
total = sum(alunos.values())
print(total)

# Número de alunos:
quantidade = len(alunos)
print(quantidade)

# Média das notas:
media = total / quantidade
print(media)

# Iterando com for:
produtos = {
    'smartphone': 3500,
    'tablet': 2675,
    'smartwatch': 375
}
for chave, valor in produtos.items():
    print(chave, valor)

# Saída:
# smartphone 3500
# tablet 2675
# smartwatch 375



# ESTRUTURAS DE REPETIÇÃO: # while
# As vezes você quer executar repetidas vezes um bloco de código, e geralmente faz algo como isso:
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
# Mas o while simplifica tudo isso. O que ele faz é repetir algum bloco de código ENQUANTO (while) sua condição for verdadeira. Lembram muito as estruturas condicionais, não é? Mas a grande diferença é que as estrututas condicionais executam apenas uma vez o bloco de código se sua condição for verdadeira, e as estruturas de repetição executam repetidas vezes um bloco de códigos. Vamos ver o exemplo mais simples possível:
# Queremos imprimir na tela 5 vezes 'Hello, World!'
# O primeiro passo para a criação de um loop while é seu contador. Pode ser de qualquer nome (defina nomes claros), então vamos utilizar neste exemplo uma variável contador, e atribuir o seu valor para 1, apenas isso:
contador = 1
# Em seguida, adicionamos a palavra-chave while, seguida de sua condição. Como queremos executar 5 vezes, colocamos essa condição:
while contador <= 5: # Enquanto a variável contador for menor ou igual a 5, então vamos executar repetidas vezes o bloco de código:
    print('Hello, World!') # Vamos imprimir o bloco de código 'Hello, World'
    contador = contador + 1 # E por fim, vamos incremetar +1 a variavel contador, pra ela não entrar em um loop infinito (jajá falamos disso)
# Perceba mais uma vez que o código está indentado com 4 espaços, sinalizando que aquele bloco de código faz parte da estrutura while.
# Recapitulando: O código acima executa 5 vezes o bloco de código 'Helllo, World!'. Lembrando que a cada repetição, a variável contador aumenta em 1.


# Vamos criar um programa que repete 5 vezes o código 'Contagem: 1, 2, 3, 4, 5...'
# Primeiramente, criamos a variavel contadora
contador = 1
# Colocamos a condição e verificamos se contador é menor ou igual a 5. Enquanto isso for True, executamos o bloco de código
while contador <= 5: # Lembrete: Se você tem uma variável 1 que vá até 5 ou 10/15/20, utilizw o operador "<="
    print(f'Contagem: {contador}') # Irá exibir sempre a contagem e o número que o contador está, já que a cada repetição o contador muda de valor
    contador = contador + 1 # Incrementando +1 para evitar o loop inifinito
# E prontinho, o código executará direitinho!

# Vamos ver mais exemplos
# Agora um exemplo de programa que começa o contador em 5 e o contador termina em 1:
# Declaramos a variável contadora
contador = 5 # Agora começa em 5
while contador >= 1: # Enquanto contador for maior que 1:
    print(f'Contagem: {contador}') # Imprime na tela o atual valor da contagem
    contador = contador - 1 # Agora estamos decrementando, subtraindo -1, por que a variável deve ser em algum momento menor que 1.


# Quebrando e continuando com o break e o continue
# Há algumas situações que você precisará parar de executar um bloco de repetiçaõ while mesmo que  condição ainda não seja satisfeita. É possível fazer isso utilizando a palavra-chave break. Vamos supor que quer repetir os números de 1 a 10, mas quando o número ser 7, o loop while simplesmente parasse? É totalmente possível fazer isso utilizando o break! Vamos ver como isso funciona
# Exemplo de programa que executa os números de 1 a 10, mas quando chega no 7, para a execução do loop
contador = 1
while contador <= 10:
    print(contador)
    if contador == 7:
        break
    contador = contador + 1
# Vamos entender este código. Criamos a variável contadora como sempre, declaramos o loop while e sua condição, logo em seguida, imprimimos o valor da variável contador e surge uma estrutura condicional: avalia se a variável contadora é igual a 7. Se for, a função break quebrará o loop e não será mais executado. E por último incrementa +1 para evitar o loop infinito.

# Quando o programa executar o comando continue, a execução do programa retornará novamente ao início do loop e a condição e será verificada novamente. Vamos supor que você queira imprimir os números de 1 a 5, porém deseja pular o número 4. Vamos ao exemplo: 
contador = 1
while contador <= 5:
    if contador == 4:
        contador = contador + 1
        continue
    print(contador)
    contador = contador + 1
# Vamos entender o código: Declaramos a variável contador, e enquanto o contador for menor ou igual a 5, verifica se contador é igual a 4, se for, adiciona +1 no contador e ignora o resto do código abaixo do continue. Se a condição for falsa, imprimimos o conntador e adicionamos +1 na variável.


# Agora um programa que pergunta ao usuário seu nome. O loop quebrará apenas quando o usuário digitar 'exit':
while True:
    nome = input("Digite o seu nome: ")
    if nome == 'quit':
        break


# Tópicos Avançados
# Substiuição de 'contador' por 'i'
# Os desenvolvedores utilizam a variável i em vez de contador. Parece um pouco contraintuitivo, pois as variáveis devem ser claras e significativas. Porém a comunidade adotou a forma de substituir contador por i. Vamos ver como ficaria num exemplo:
i = 5
while i >= 1:
    print(i)
    i = i - 1

# Utilizando operadores de atribuição
# O while possui bastante código, ou seja, é relativamente grande o espaço de linhas necessário para fazer repetições. Há uma forma de diminuir essa 'verbosidade' toda. Vamos utilizar o operador de atribuição para diminuir um pouco isso:
i = 1
while i < 5:
    print(i)
    i += 1 # Operador de atribuição
# A diferença aqui é que utilizamos o sinal 'i += 1'. Isso é a mesma coisa do que dizer 'i = i + 1'. Veja mais um exemplo:
i = 1
while i < 5:
    print(i)
    i += 1 # é a mesma coisa do que 'i = i + 1'

# Loops infinitos: Executam o programa até o infinito.. e além
# Loops infinitos são loops que nunca param de executar, executam o bloco de código que está dentro deles para sempre. Issso acontece quando você acidentalmente esquece de incrementar ou decrementar a variável contadora responsável pela quantidade de execuções de um bloco. Exemplo:
# contador = 1
# while contador < 10:
#     print('Contando!')
# O código a seguir é um exemplo de loop infinito. Vamos descobrir o porque. Primeiramente declaramos a variável contador e atribuí-mos a ela o valor 1 normalmente, tudo certo. Criamos um loop while que verifica se o contador é menor que 10, se for menor que 10, continua executando, até chegar a um momento em que a condição se torna falsa (até o contador ser 10). Nós imprimos 'Contando!', mas o único detalhe é que esquecemos de incrementar + 1 dentro de seu bloco de código, por isso o loop ficará executando eternamente. Isso consome muita memória RAM e Bateria, então quando acidentalmente entrar em um loop infinito, feche o programa o mais rápido possível. Então a correção deste loop infinito seria esse:
contador = 1
while contador < 10:
    print('Contando!')
    contador = contador + 1 # Evitando que o loop seja infinito
# Agora sim, adicionamos o incrementador! Não se esqueça disso!


# While...else:
# Semelhante as condições, os laços de repetição while também aceitam else. O else só é executado quando a condição do while for falsa, como as estruturas de condição. Vamos ver na pratica:
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('As repetições acabaram')

# Isso imprime os números de 1 a 10, e quando a condição do while for falsa, isso é, quando a variável i atingir o valor 11, o programa verifica se 11 é menor que 10, e como isso retorna um booleano False, então o else será executado seguido de seu bloco de código, imprimindo 'As repetições acabaram'


# ESTRUTURA DE REPETIÇÃO: for
# Além do loop while, também existe um outra alternativa para repetições no python, o for. O for possui uma sintaxe bem menos verbosa (isso significa que o for pode fazer a mesma coisa que o loop while, porém com menos linhas de código) e ainda te permite iterar sobre listas ou coleções (Assunto mais adiante). 


# Exemplo ruim de uma contagem até 5:
print('Contagem: 1')
print('Contagem: 2')
print('Contagem: 3')
print('Contagem: 4')
print('Contagem: 5')
# Exemplo recomendável e certo de contar até 5:
for contagem in range(1, 6):
    print(f'Contagem: {contagem}')


# Entendendo o loop for range
# for range: Conta do início até o fim, como uma contagem regressiva (ou progressiva).
# Sintaxe:
# for contador in range(inicio, fim, passos):
    # bloco de códigos
# primeiramente utiliza-se a palavra-chave for, em seguida uma variável desejada, como contador, e por fim utiliza-se 'in' e o range(), contendo dentro dos seus parênteses os números especificados. Vamos ver um exemplo
for contador in range(0, 5, 1):
    print(contador)
# Utilizamos o for, a variável contador, logo em seguida o in range(0, 5, 1). Vamos explicar o range. O primeiro número do range significa em qual número ele deve começar, nesse caso, 0. O segundo número diz até quando o contador deve parar, nesse caso 4, pois o fim sempre é subtraído em -1, ou seja, se o número final é 10, então na verdade seu fim é 9. E o último número diz quantos em quantos passos o contador irá pular, nesse caso é 1, então contará normalmente de 0 a 4. Por fim é colocado dentro da estrutura do for o comando de blocos, nesse caso, imprimirá o contador, ou seja, imprimirá: 0, 1, 2, 3, 4.
# Vamos ver mais um exemplo:

for i in range(1, 6, 1):
    print(i)
# Declaramos a variável i, e o range começa do 1, termina até o 6, e pula de 1 em 1 número (isso é, normalmente). A saída será: 1, 2, 3, 4, 5
# Lembre-se que o for é uma estrutura de repetição, então sempre que executar uma vez o bloco de código dentro dele, a variável contador será subtraída ou adicionada em 1, como um loop while. Veremos mais a frente a diferença entre loop while e loop for.

# Mas não é necessário colocar em quantos em quantos passos a variável vai pular. podemos utilizar essa sintaxe:
# for i in range(inicio, fim):
    # <bloco de comandos>

# Vamos ver um exemplo:

for i in range(1, 4):
    print(i)
# Declaramos a variável contadora 'i', e o seu range de início é de 1, ou seja, comecará em 1, e seu range de fim é 4, ou seja, terminará em 3, pois o fim é sempre subtraído. A saída desse for é: 1, 2, 3


# Porém ainda é possível omitir o range de início, restando apenas o range de fim! Vamos ver como isso ficaria:
# for i in range(fim):
    # <bloco de comandos>

for i in range(5):
    print(i)
# Aqui omitimos o range de início, então ele começará em 0, e terminará em 4, bela reduzida, não é mesmo?

# Vamos ver um exemplo mais avançado:
for foguete in range(4):
    print(f'Lançando em {foguete}')
# Vamos entender o código. Declaramos a variável foguete, que conta de 0 até 3. O seu bloco de código imprimirá 'Lançando em {e o número do contador}'. Cada execução que o loop realizar, será incrementado em +1 a variável foguete. Vamos entender melhor isso:

for i in range(1, 4):
    print(i)
# Esse bloco de código começa em 1, e termina em 3. A cada execução, é incrementada +1 a variável i, e o programa verifica se i é maior que 3. Se a variável i for maior que 3, então o loop para de executar, pois sua condição já esteve satisfeita. Não parece, mas o loop for também há uma condição, conseguiu perceber?
# for i in condição:
    # <bloco de código>
# Mas nesse caso a condição é o range, e não uma comparação tradicional com operadores de comparação como num loop while. É claro que o programa faz comparação no loop for, mas isso não é visível. Vamos ver apenas um último exemplo:
for repeticao in range(1, 6):
    print('Estou repetindo!')
# Ok, declaramos uma variável repeticao e agora ela repete de 1 até 5, e a cada repetição, será incrementada +1 na variável, executando o bloco de código 'Estou repetindo!'. Acompanhe comigo: A variável repeticao tem o valor de 1, então o programa verifica se a repeticao é menor que 5, e como 1 é menor que 5, então executa o bloco de código, imprimindo o que estiver lá dentro. Na segunda, terceira, quarta, quinta repetição, o programa verifica se ainda a variável não é 5, então executa novamente. Mas quando a variável repeticao é 6, o programa compara, e vê que a variável já chegou ao fim, já terminou. Então simplesmente para de executar o loop e executa o resto do programa.

# Então, que tal ver um loop for com um else, lembrando muito as condições?
for foguete in range(4):    
    print(f'Lançando em {foguete}')
else:
    print('Lançar!')
# Vamos lá, foi declarada a variável foguete, que começa em 0 e termina em 3. Na primeira repetição é executado o loop, executando o seu bloco de código, e imprime 'lançando em {e a variável}'. Como nesse caso não especificamos o início e apenas o fim, então a repetição começará do 0. Ou seja, na primeira repetição imprimirá 'Lançando em 0', pois a variável foguete tem o valor 0. Então é feita mais uma repetição, e desta vez o valor da variável é 1, pois a cada execução a variável é incrementada em 1, e então, imprime 'Lançando em 1'. E repete isso até chegar na repetição 4. O programa veifica se a variável é 4, e então, ignora o bloco de código do loop for e executa o else. Lembra do else, aquele utilizado em condições, que quando uma condição é falsa, ele é executado? Então, o programa viu que a condição do loop for é falsa e executou o else, imprimindo na tela 'Lançar!'.


# Vamos lá, hora de responder algumas perguntas

# Qual a diferença entre loop while e loop for?
# Um loop while pode ser usado quando não se sabe ao certo quantas repetições você quer que algo repita. o while True é um exemplo muito bom disso, pois executa a repetição infinitamente, e só para quando é feito o uso de um break. Vamos ver um loop while True:
while True:
    nome = input("Digite o seu nome ou 'exit' para sair: ")
    if nome == 'exit':
        break
# Vamos explicar: Criamos um loop while True, isso significa que o loop executará infinitamente. Pedimos ao usuário o seu nome, e isso ficará executando. O loop while só terminará de executar quando o usuário digitar 'exit', pois foi feito o uso do break, quebrando o laço while. Então enquanto o usuário digitar qualquer outra coisa que não seja 'exit', o loop ficará executado seu bloco de código para sempre, perguntado ao usuário seu nome infinitamente. A única forma de parar essa repetição é utilizando um break.
# Já um loop for pode ser usado quando já se sabe o número de repetições que você quer. Um exemplo:
for i in range(6):
    print('Já sei quantas vezes serei executado! 5 vezes!')



# Agora vamos ver alguns exemplos de iteração em listas
# A iteração em listas segue o mesmo conceito da iteração com strings, mas a grande diferença é que a iteração em listas imprime cada elemento da lista, e não cada letra. Vamos ver alguns exemplos
# Iterando com o loop for
# Uma iteração significa acessar cada elemento ou caractere de uma sequência, como uma lista ou uma string. Vamos ver alguns exemplos:
# Vamos supor que temos uma string, e queremos imprimir cada letra da string individualmente. É possível fazer isso com uma iteração:
string = 'texto'
for letra in string:
    print(letra)
# Aqui já é notável que as coisas mudaram, vamos entender. Declaramos a variável string e atribuímos seu valor a 'texto'. Em seguida, criamos um loop for e uma variável letra, ela será responsável por iterar sobre cada caractere da string, ou seja, imprimir cada letrinha. Lembrando que o nome da variável após o loop for pode ser qualquer um que você desejar. O código acima se lê assim:
# para cada letra na string, então imprima a letra.
# Vamos ver mais exemplos:

pais = 'Brasil' # Lembrando que variáveis não devem ter acentuações!
for letra in pais:
    print(letra)
# Vamos entender: Declaramos a variável pais, e em seguida o loop for, seguido da variável letra, que itera sobre cada letra da variável pais (Brasil). Então isso imprimirá cada letra do Brasil em uma linha diferente, ou seja:
"""
B
r
a
s
i
l
"""

# Hora de iterar sobre listas
# Agora vamos falar de iterações com listas. As iterações com listas diferentemente das iterações com strings, imprimem cada elemento da lista, e não cada letra da lista. É feito quase a mesma coisa com a iteração de strings, vamos ver um exemplo:
# Vamos supor que queremos imprimir individualmente cada elemento de uma lista de frutas:
frutas = ['Maçã', 'Banana', 'Laranja']
# então utilizamos o for, seguido da variável que desejamos e em seguida a palavra-chave in, e por fim, o nome da lista, com o seu bloco de código. Vamos ver:
for fruta in frutas:
    print(fruta)
# Vamos entender: Declaramos a lista frutas, declaramos o laço for seguido pelo nome da variável e a palavra-chave in com a lista frutas, e no seu bloco de código imprime cada fruta, resultado em:

"""
Maçã
Banana
Laranja
"""
# Uma coisa muito importante a dizer é que, ao executar o bloco de códigos dentro do loop for, a repetição é feita novamente até não possuir mais elementos dentro da lista.
# Repare que o nome da lista está escrito no plural ('frutas') e o nome da variável após o for está escrito em singular ('fruta') indicando que isso acessará cada elemento da lista individualmente.

# Vamos ver mais um exemplo:
animais = ['Coruja', 'Lobo', 'Cachorro', 'Cavalo']
for animal in animais:
    print(animal)
# O loop for acima se lê assim: Para cada animal na lista de animais, então: imprima animal. Vamos entender melhor, declaramos a lista animais seguido pelo loop for, que itera a cada elemento, e imprime cada elemento individualmente, conseguiu compreender?

# Vamos a alguns exemplos mais avançados:
# Vamos supor que estavamos minerando numa caverna, mas não queremos que tenha Ferros, apenas queremos outros minérios, e ignorar o minério Ferro. Podemos utilizar um loop for e dentro desse loop utilizar uma estrutura de condição verificando se Ferro está na lista. Se estiver, então queremos que o programa ignore esse minério. Vamos como isso funciona:
minerios = ['Diamante', 'Ouro', 'Ferro', 'Cobre']
for minerio in minerios:
    if minerio == 'Ferro':
        continue
    print(minerio)
# Vamos entender esse código. Criamos uma lista e dentro dela possui minérios. Em seguida utilizamos o loop for, para iterar sobre cada elemento. Dentro deste loop for, utilizamos uma estrutura de condição para verificar se o elemento que estamos iterando é Ferro. Se o elemento for ferro, então simplesmente ignoramos esse elemento e a repetição retorna ao início, verificando se o elemento é ferro novamente, se não for, apenas imprime o minério. A saída desse código é a seguinte:
"""
Diamante
Ouro
Cobre
"""

# Tópicos avançados
# Vamos supor que você está iterando uma lista, e quer verificar se algum elemento está na lista. Você utiliza uma condição para verificar e quando verifica, o elemento dentro da lista era maiúsculo, e você utilizou letras minúsculas. Veja o exemplo a seguir:
produtos = ['Fone', 'Celular', 'Tablet', 'Computador']
for produto in produtos:
    if produto == 'celular':
        print('Achei um celular!')
# Aqui há um grande problema. Repare que na lista, celular está com sua primeira letra em maiúsculas ('Celular') e você está verificando se 'celular' (em minúsculas) está na lista produtos. Não vai ter nenhuma saída, pois 'Celular' é diferente de 'celular'. Por sorte podemos utilizar uma função de strings para converter todos os produtos em minúsculas, o lower(). O código ficaria assim:
produtos = ['Fone', 'Celular', 'Tablet', 'Computador']
for produto in produtos:
    produto = produto.lower()
    if produto == 'celular':
        print('Achei um celular!')
# Agora sim. O que foi alterado nesse código é que antes de tudo, convertemos todos os produtos da lista para minúsculas, e em seguida, verificamos se celular está na lista. Veja como a função lower() é muito importante.


# Operador ternário
# Se você analisar uma estrutura condicional com o if, elif e o else, notará que eles utilizam muitas linhas de código. Foi pensando nisso que foi criado o operador ternário, prometendo diminuir mais linhas, e fazer a mesma coisa mas em apenas UMA LINHA! Sua sintaxe é um pouco diferente de uma estrutura condicional utilizando o if. Vamos ver como funciona:
# Sintaxe:
# 'valor verdadeiro' if True else 'valor falso'
print('Verdadeiro' if True else 'Falso')
# Ok, vamos entender esse código. Primeiro dizemos o que é para imprimir se a condição for True, nesse caso, utilizamos 'Verdadeiro' Ou seja, será imprimido 'Verdadeiro' se True == True. Mas se for falso, então executará o que vem logo após o else, ou seja, imprimirá 'Falso'. Vamos ver mais um exemplo e comparar com uma condição if:
pet = True
# Estrutura condicional
if pet:
    print('Possui um pet')
else:
    print('Não possui um pet')





# -   -   -   -   -   -   - Funções -   -   -   -   -   -   -   -   -
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






# Operador ternário
print('Possui um pet' if pet else 'Não possui um pet')
# O código se lê assim:
# Imprima 'possui um pet' se pet for True, se não, imprima 'Não possui um pet'. Neste caso, pet é True, então executará 'Possui um pet'. Vamos ver mais um exemplo


idade = 151
if idade < 18:
    print('Jovem')
else:
    print('Adulto')

print('Jovem' if idade < 18 else 'Adulto')
# Vamos entender: O programa imprimirá 'Jovem' se idade for menor que 18, mas se idade não for menor que 18, isso é, se idade for maior que 18, então imprimirá 'Adulto'. Os operadores ternário possuem uma sintaxe bem menor se comparado a uma estrutura condicial tradicional, não é mesmo? Vamos a mais alguns exemplos
luz = True
ternario = 'luz acessa' if luz else 'luz apagada'
print(ternario) # 'luz acessa'





# - -   -   -   -   -   -   Arquivos    -   -   -   -   -   -   
# Arquivos: O Python permite que você leia e modifique o conteúdo de arquivos! Lembrando que nesse curso, vamos focar nos arquivos de texto, aqueles com a extensão '.txt'. Vamos lá. Imagine que você precise ler o conteúdo de um arquivo ou até alterar ele.
# Que tal fazer isso com Python? É simples e poderoso!

# Primeira coisa: pra mexer em um arquivo, a gente precisa abrir ele, certo? Então vamos aprender a abrir arquivos com Python.

# A sintaxe básica pra isso é:
# open(nome_do_arquivo, modo, encoding)

# Agora vamos entender o que cada parte dessa função faz:
# - nome_do_arquivo: o nome do arquivo que você quer acessar. Simples assim.
# - modo: o que você vai fazer com o arquivo? Ler? Escrever? Adicionar mais conteúdo?
# - encoding: define como o texto será codificado. Usamos 'utf-8' pra aceitar acentos, emojis e caracteres especiais.

# Vamos ver os modos mais comuns:
"""
w  - write: escreve no arquivo, apagando tudo o que tinha antes (cuidado!)
r  - read: só lê o conteúdo do arquivo
a  - append: adiciona conteúdo no final, sem apagar o que já tinha
a+ - append and read: adiciona conteúdo e também permite leitura
"""

# Vamos ver isso funcionando na prática!

# Primeiro, criamos uma variável chamada 'arquivo', e abrimos um arquivo pra escrita ('w'):
arquivo = open('arquivo.txt', 'w', encoding='utf-8')

# Aqui a gente criou (ou sobrescreveu) um arquivo chamado 'arquivo.txt'.
# Estamos usando o modo 'w', que vai apagar qualquer conteúdo antigo e escrever do zero.
# Também usamos encoding='utf-8' pra garantir que acentuação e caracteres especiais funcionem.

# Agora vamos escrever alguma coisa nesse arquivo:
arquivo.write('Escrevendo coisas aqui')

# Pronto! Quando esse código é executado, ele cria o arquivo (se não existir) e escreve exatamente o que colocamos no .write(). Fácil, né?

# Agora vamos ver como a gente lê o conteúdo de um arquivo.
# Pra isso, usamos o modo 'r':
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())  # saída esperada: Escrevendo coisas aqui

# Legal! Agora vamos conhecer o modo 'a', que é usado pra adicionar conteúdo sem apagar o que já tinha:
arquivo = open('arquivo.txt', 'a', encoding='utf-8')
arquivo.write('Escrevendo coisas aqui novamente!')

# Vamos ler o conteúdo de novo e ver como ficou:
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())

# saída:
"""
Escrevendo coisas aqui
Escrevendo coisas aquiEscrevendo coisas aqui novamente!
"""

# Repara que o texto ficou tudo grudado. Isso acontece porque o write() escreve exatamente como a gente manda, e não coloca uma quebra de linha automática. Porém a solução é simples: apenas usar '\n' pra pular pra próxima linha.

# Vamos corrigir isso:
arquivo = open('arquivo.txt', 'a', encoding='utf-8')
arquivo.write('\nEscrevendo coisas aqui novamente!')

# Agora sim, tudo organizadinho!
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())

# saída:
"""
Escrevendo coisas aqui
Escrevendo coisas aqui novamente!
"""

# Legal demais, né? Agora deixa eu te mostrar um truque profissional: Ao invés de abrir e fechar arquivos manualmente, dá pra usar o 'with'. É um método mais seguro para abrir arquivos e modificá-los. Vamos ver:

# Veja só como usar:
with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nMais uma linha adicionada com segurança!')

# Aqui usamos o 'with open(...) as arquivo', o que significa que ele automaticamente fecha o arquivo, evitando desastres posteriores.









# Exceções e Tratamento de Erros
# Exceções são essenciais num programa para mostrar uma mensagem menos assustadora, mas não só por causa disso, os erros também são um péssimo vilão, uma vez que não foram identificados, o programa todo se quebra e o usuário fica perdido. As exceções tratam erros gerais, mas você pode especificar qual erro deseja tratar.
# # sintaxe básica:
# try:
#     <bloco de código>
# except:
#     <mensagem de erro>
# Primeiramente utilizamos o try, e dentro de seu bloco de códigos inserimos o código que é suspeito de falhas. Logo em seguida, fora do bloco de códigos do try, utilizamos o except, e no bloco de código do except colocamos os códigos que serão exibidos caso ocorra algum erro.

# Vamos ver o seguinte exemplo em que tentamos dividir uma STRING por um INT:
try:
    divisao = 3 / "string"
    print(divisao) # Isso sempre dará um erro porque não é possível dividir um inteiro por uma string.
except:
    print("Ocorreu um erro!")

# saída: Ocorreu um erro!


# É muito recomendado que se utilize tratamento de erros em todo programa que você for criar, especialmente quando é utilizado a interação com o usuário (os inputs), mesmo que você não suspeite que aconteça erros. Vamos ver um exemplo geral:
try:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(f'A soma entre {n1} e {n2} é {n1 + n2}')
except:
    print('Ops! Não foi possível calcular a soma entre os dois números!')

# Aqui tentamos realizar a soma entre n1 e n2, mas surge uma pergunta: "Como que isso pode dar um erro?". Uma das respostas é se o usuário digitar um número decimal (float), isso causaria um erro porque declaramos n1 e n2 como inteiros, e não decimais. Outra possível falha é caso o usuário não digitasse nada e apenas apertasse ENTER, isso também seria um erro pois ENTER é um valor nulo, não um inteiro.






# Atenção! Para ter acesso aos módulos, você deve ter um editor de código (Recomendo o VSCode) instalado e o python também! Há o tutorial de como fazer isso na primeira aula do curso!
# Python por si só já possui diversas funcionalidades. Mas imagina só se tivessemos uma chave para descbloquear novas funcionalidades, tornando ele ainda mais funcional e divertido? Então eu gostaria de te apresentar os MÓDULOS! Os módulos são tipo um cofre, aonde você mesmo pode abrir esses cofres com chaves, ou melhor, comandos!
# Um comando essencial para utilizar módulos é o 'pip install'. Você utiliza esse comando no seu prompt de comandos ou no terminal do seu editor de códigos. Vamos utilizar o prompt de comandos.
# [Aqui vai os comandos aí bla bla bla e as fotos]
# Ok, depois de ter feito isso, vamos lá!

# O módulo random
# Imagine brincar de adivinhar o número, mas quem escolher o número é o seu computador e quem faz os chutes é você?? Hah, com o módulo random isso é muito possível e simples fácil de fazer!
# random é um módulo do python que permite que o próprio computador possa escolher números, letras ou até elementos de uma lista! Vamos ver como funciona o random!
# Imagine o seguinte: Você dizer ao computador para escolher um número entre 1 a 100, então vamos ver como fazer isso agora!
# Primeiro importamos o módulo random, basta digitar import random
import random
# A seguir utilizamos o comando random.radint(inicio, fim), onde inicio é o número que desejamos que o computador comece a escolher, e o número fim é o número que desejamos que o computador termine de escolher. Como queremos que ele escolha de um número de 1 a 100, então ficará assim:
escolha = random.randint(1, 101)
print(escolha) # 92

# Repare que dentro dos parênteses de randint, o número começa do 1 e ter,ina até 101, nesse caso na verdade termina em 100, pois o término é sempre subtraído em 1. Mas tirando isso, é super fácil de entender!

# Ok, agora vamos supor que você tenha uma lista, e queira que o computador escolha um elemento dessa lista. Você pode fazer isso utilizando o random.choice(lista). Vamos ver num exemplo:
alimentos = ['Arroz', 'Macarrão', 'Strogonoff']
elemento = random.choice(alimentos)
print(elemento)

# Pronto, simplesmente isso!

# Agora que tal criar um mini joguinho em que você tenta acertar o número aleatório que o programa criar?
# Vamos criar um programa onde seu objetivo é acertar o número que o computador acertar:
import random
numero = random.randint(1, 101)
while True:
    palpite = int(input("Qual é o seu palpite? "))
    if palpite > 101 or palpite < 0:
        print('Por favor, digite um número entre 1 a 100!')
    elif palpite > numero:
        print('Chute alto!')
    elif palpite < numero:
        print('Chute baixo!')
    elif palpite == numero:
        print('Você acertou!')
        break
# Vamos entender: Primeiro importamos o módulo random, depois criamos a variável numero, que recebe um número aleatório entre 1 a 100. Logo em seguida criamos um loop while True, e perguntamos o palpite para o usuário. O programa avalia se o palpite é maior que 101 ou menor que 0 (exceções) e depois verifica se é maior ou menor que o número. A última condição verifica se o palpite é igual ao número aleatório gerado, se for, imprime na tela 'Você acertou' e quebra o loop para não ser executado eternamente.

# Datetime
# Já pensou em aplicar datas e horas no seu programa? É totalmente possível fazer isso utilizando o datetime, uma biblioteca do python que te permite trabalhar com horas e datas, vamos nessa?
# Antes de tudo, você deve ir no seu terminal, ou no seu prompt de comandos, digitar 'python', teclar ENTER e em seguida digitar 'pip install datetime'
# A primeira coisa que se deve fazer é importar o datetime, deste jeito:
import datetime
# Pronto, após isso podemos brincar com as datas e as horas!
# Primeiramente vamos ver como acessar o ano, o mes e o dia:
ano = datetime.datetime.now().year
mes = datetime.datetime.now().month
dia = datetime.datetime.now().day
# Criamos uma variável ano e utilizando as funcionalidades do datetime, atribuímos o seu valor para o ano atual. Fizemos a mesma coisa para o mês e o dia. Isso segue um padrão: datetime.datetime.now() e logo após o now utilizamos a função que queremos em inglês, por exemplo, dia -> day; mês -> month; ano -> year

# Vamos acessar também a hora, o minuto, o segundo e até o microssegundo!
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
segundo = datetime.datetime.now().second
microsegundo = datetime.datetime.now().microsecond
# Novamente segue o mesmo padrão anteriormente já dito. Se você já sabe ano, mês, dia, hora, minuto, segundo e microssegundo em inglês, então pode facilmente entender o conceito de datas e horas utilizando o datetime. 
# Que tal criarmos nossa própria data?
# Utilizando o datetime.datetime(ano, mês, dia) podemos criar nossas próprias datas. Vamos ver um exemplo:
# datetime: Ano, mês, dia {opcional horas, minutos, segundos, microssegundos}
data = datetime.datetime(2025, 5, 4)
print(data) # 2025-05-04 00:00:00
# Não especificamos as horas, mins, segs e microsegs, vamos fazer isso:
data = datetime.datetime(2025, 5, 4, 15, 30, 00)
print(data) # 2025-05-04 15:30:00

# Agora vamos supor que queremos apenas as horas, mins e segs. Podemos criar isso utilizando o datetime.time(horas, minutos, segundos, microssegundos)
# time: horas, minutos, segundos, microssegundos
time = datetime.time(12, 30, 00)
print(time) # 12:30:00


# Também é possível utilizar matemática com datas! Vamos ver como isso funciona:
# Vamos supor que vamos ao cinema, e o cinema fecha daqui 15 minutos, considerando que agora são 13:30.
agora = datetime.datetime(2025, 5, 17, 13, 30, 00)
cinema = datetime.datetime(2025, 5, 17, 13, 45, 00)
print(cinema - agora) # 0:15:00

# Podemos fazer cálculos envolvendo anos, meses, dias, enfim, qualquer função.
amanha = datetime.datetime.now().day + 1
print(amanha)
ano_posterior = datetime.datetime.now().year + 1
print(ano_posterior)


# Criando os seus próprios módulos
# Imagina só agora você comandando seus próprios módulos? Vamos ver isso agora!
# [Blá blá blá prints e dezenas de prints]
# Primeiramente, vamos criar uma pasta nomeada de 'modulos'
# Depois, dentro desta pasta, criamos dois arquivos. O primeiro arquivo será o 'main.py' e depois criaremos mais um, o 'modulo.py'. Dentro do modulo.py, vamos criar uma função:
def prazer():
    return f'Olá, prazer em te conhecer!'
print(prazer())

# Ok, agora vamos ir no 'main.py' e utilizar o seguinte comando:
# import main
# Vamos executar o código
# saída:
# Olá, prazer em te conhecer!