#---- Estruturas de Repetição
## Estruturas de repetição são utilizadas para executar um bloco de código várias vezes, até que determinada condição seja atendida. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica. 

# Comando for
## O comando for é utilizado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código dever ser executado, ou quando queremos percorrer um objeto iterável. 

texto1 = input('Informe um texto: ')
vogais = 'AEIOU'

for letra1 in texto1: 
    if letra1.upper() in vogais:
        print(letra1, end='')

print() # adiciona uma quebra de linha

# Comando for/else

texto2 = input('Informe um texto: ') 
VOGAIS = 'AEIOU'

for letra2 in texto2: 
    if letra2.upper() in VOGAIS:
        print(letra2, end= ' ')
else:
    print() # adiciona uma quebra de linha
    print('Executa no final do laço.')

# Função range
## Range é uma função built-in do python que é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: 
# i, i+1, i+2, i+3, ..., j-1...
# ela recebe três argumentos: stop (obrigatório), start (opcional) e step (opcional).

for numero in range(0,11):
    print(numero, end=" ")
    print()

## tabuada de 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
print()

# Comando while
## É usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado. F
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n"))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigado por usar nosso sistema bancário, até logo!')

# Comando break
## O comando break é usado para sair de um laço de repetição.

while True: #loop infinito
    numero = int(input('Informe o número:'))

    if numero == 10:
        break

    print(numero)

# Comando continue
## O comando continue é usado para pular a iteração atual e continuar para a próxima iteração.

for numero in range(45):
    if numero == 12:
        continue

    print(numero, end=' ')