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