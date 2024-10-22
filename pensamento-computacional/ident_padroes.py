arroz_kg = 7.00
feijao_kg = 9.00
carne_kg = 35.00


for i in range(3):
    valor = input()
    valor = float(valor)
    if valor <= 10:
        print ("Posso comprar!")
    else:
        print ("Não posso comprar!")
