# --- Estruturas Condicionais
## A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
## A estrutura condicional é composta por três partes:  
## 1. A expressão lógica que será avaliada;
## 2. O bloco de código que será executado caso a expressão lógica seja verdadeira;
## 3. O bloco de código que será executado caso a expressão lógica seja falsa.

# Estrutura Condicional Simples (if) 
## A estrutura condicional simples é composta por um bloco de código que será executado caso a expressão lógica seja verdadeira.
import sys


saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Saque aceito!')

if saldo < saque:
    print('Saldo insuficiente!')

# Estrutura Condicional Composta (if-else)
## Caso o if seja verdadeiro, o bloco de código dentro do if será executado. Caso contrário, o bloco de código dentro do else será executado.
idade = int(input('Digite a idade do(a) aluno(a): '))
if idade >=  18:
    print('Aluno(a) com permissão para dirigir!')
else:
    print('Aluno(a) sem permissão para dirigir!')

# Estrutura Condicional Encadeada (if-elif-else)
## A estrutura condicional encadeada é utilizada quando existem mais de duas possibilidades de desvio de fluxo de controle.

opcao = int(input('Informe a opção: \n[1] Sacar \n[2] Extrato \nEscolha:'))

saldo = 3000.0

if opcao == 1:
    saque = float(input('Informe o valor do saque: '))
    if saldo >= saque:
        print('Saque aceito. Saque: %.4f' %saque)
    else:
        print('Saldo insuficiente!')
elif opcao == 2: 
    print('Extrato solicitado. Saldo em conta: %.4f' %saldo)
else: 
    print('Opção inválida!') # sys.exit() ==> utilizado para encerrar programas em Python, através da biblioteca importarda sys.

# if ternário
## Essa forma de condicional permite escrever o if em uma única linha. O if ternário é composto por três partes, a primeira é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão lógica não seja atendida.

saldo = 80.0

saque = float(input('Informe o valor do saque: '))
status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')
