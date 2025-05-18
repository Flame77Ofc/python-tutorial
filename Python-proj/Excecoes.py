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