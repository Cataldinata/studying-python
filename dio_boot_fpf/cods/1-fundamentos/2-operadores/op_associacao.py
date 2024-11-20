# Operadores de Membros ou Operadores de Associação
## Estes operadores testam se um valor ou variável é membro de uma sequência, como strings, listas ou tuplas, ou se uma sequência é apresentada em um objeto.

# Operador in 
## Retorna True se um valor específico for encontrado em um objeto, caso contrário, retorna False.

# Operador not in   
## Retorna True se um valor específico não for encontrado em um objeto, caso contrário, retorna False.  

curso = 'Cruso de Python'
frutas = ['maçã', 'banana', 'uva', 'laranja']
saques = [1500, 100]

print('Python' in curso) # mostrará True

print('Kiwi' in frutas) # mostrará False

print(1500 not in saques) # mostrará False

print(100 in saques) # mostrará True  