# --- Operadores de Identidade
## Estes são usados para comparar os objetos, não se são iguais, mas se eles forem realmente o mesmo objeto, com o mesmo local de memória.

# Operador is
## Retorna True se ambos os operandos forem o mesmo objeto.
# Operador is not
# Retorna True se ambos os operandos não forem o mesmo objeto.  
curso = 'Curso de Python'
nome_curso = curso 
saldo, limite = 200, 200

print(curso is nome_curso) # True

print(curso is not nome_curso) # False

print(saldo is limite) # True

print(limite is not saldo) # False

