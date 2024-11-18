#TIPOS DE DADOS - os mais comuns
# Texto: str
# Numérico: int, float, complex
# Sequência: list, tuple, range
# Mapa: dict
# Coleção: set, fronzenset
# Booleano: bool
# Binário: bytes, bytearray, memoryview

print(1 + 10)
print(1.6 + 8.09)
print(True)
print(False)
print("Python")

#CONVERSÃO DE TIPOS DE DADOS

# --- numérico para outro tipo de númerico
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

preco = 10.00
print(preco)

preco = int(preco)
print(preco)

print(preco / 2)

print(preco // 2) # conserva o tipo inteiro

# numérico para string
idade = 28
preco = 10.80
print(str(preco))
print(str(idade))

texto = f'idade {idade} preco {preco}'
print(texto)

# string para número
preco = '10.50'
idade = '28'

print(int(idade))
print(float(preco))

# -- ERRO DE CONVERSÃO --> se tentar converter uma sequência de letras para número
