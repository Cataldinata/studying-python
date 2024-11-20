# ---- Operadores Lógicos
## Eles são utilizados para combinar comandos condicionais, em conjunto com operadores de comparação, para montar uma expressão lógica. Retonará umvalor booleano.

# Operador and
a, b, c = 1, 2, 3
print(a > c and b > a) # Retorna True se ambos os comandos são verdadeiros. Neste caso mostrará false

# Operador or
print(a==b or a<c) # Retorna True se um dos comandos é verdadeiro. Neste caso mostrará True 

# Operador not
print(not a>c) # Reverte o resultado, transformando True em False e vice-versa. Neste caso mostrará True