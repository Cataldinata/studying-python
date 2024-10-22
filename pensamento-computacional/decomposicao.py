descontos = 300.00
salario_fixo = 1650.00
vendas_mes = 50
vendas_comissao = 20.00
valor_total_vendas = vendas_mes * vendas_comissao

salario_liquido = ((salario_fixo + valor_total_vendas) - descontos)

print(salario_liquido)
