# --- São conhecidos também como operadores matemáticos

# Operador de Adição (+)  
soma = 1 + 2
text_soma = f'Soma: {soma}'
print(text_soma) # resultado = 3

# Operador de Subtração (-)
subtracao = 2 - 1
text_subtracao = f'Subtração: {subtracao}'
print(text_subtracao) # resultado = 1

# Operador de Multiplicação (*)
multiplicacao = 2 * 2 
text_multiplicacao = f'Multiplicação: {multiplicacao}'
print(text_multiplicacao) # resultado = 4

# Operador de Divisão (/) 
divisao = 4 / 2 
text_divisao = f'Divisão: {divisao}'
print(text_divisao) # resultado = 2

# Operador de Divisão Inteira (//)
div_inteira = 5 // 2
text_div_inteira = f'Divisão inteira: {div_inteira}'
print(text_div_inteira) # resultado = 2

# Operador de Módulo (%) 
modulo = 5 % 2
text_modulo = f'Módulo: {modulo}'
print(text_modulo) # resultado = 1

# Operador de Exponenciação (**)
exponenciacao = 2 ** 3
text_exponenciacao = f'Pontenciação: {exponenciacao}'
print(text_exponenciacao) # resultado = 8

# Operador de Radiciação (1/n)
radiciacao = 4 ** (1/2)
text_radiciacao = f'Radiciação: {radiciacao}'
print(text_radiciacao) # resultado = 2.0


# --- Precedência de Operadores 
# 1° parênteses
# 2° expoêntes
# 3° multiplicação e divisão (da esquerda para a direita)
# 4° adição e subtração (da esquerda para a direita)

expressao_1 = 10 + 3 / (4-2)
print(expressao_1)

expressao_2 = (10 + 3) / (4-2)
print(expressao_2)
