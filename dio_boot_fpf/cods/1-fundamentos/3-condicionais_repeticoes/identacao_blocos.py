# --- Identação e Blocos
## Antes de começar, é importante ter noção sobre identação e blocos de código no Python.
## Em muitas linguagens, a identação é somente algo estético, não interferindo em nada na execução do código.
## Porém, em Python, a identação é obrigatória e define os blocos de código.
## Em Python, um bloco de código é definido por um conjunto de linhas de código que estão identadas com a mesma quantidade de espaços.  
## Por convenção, utiliza-se 4 espaços para cada nível de identação.
## Em Python, os bloco de código têm início com dois pontos (:), porém não há pontuação para definir o fim do bloco a não ser a própria identação.

def sacar(valor): # início do bloco de método
    saldo = 500000

    if saldo >= valor: # início do bloco de condição
        print('Valor sacado!')
        print('Retiro o seu dinheiro na boca do caixa.')
        # fim do bloco de condição
    print('Obrigado por ser nosso cliente!')
    
# fim do bloco de método    

sacar(10000) 