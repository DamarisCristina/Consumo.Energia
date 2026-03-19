# ⚡ Calculadora de Consumo de Energia ⚡

aparelho = input ("Qual o nome do aparelho? ")
potencia = float(input("Qual a potência do aparelho em watts (W): "))
horasdia = float (input ("Qual o tempo médio de uso diário em horas? "))
preco = float (input("Qual preço estimado do kWh? "))

# Calcula o consumo mensal (em kWh)
consumoMensal = (potencia*horasdia*30) / 1000

# Calcula o custo de kWh vezes o preço escolhido por você
custo = consumoMensal * preco 

# - Descrevendo -
print(f"Aparelho: {aparelho}")
print(f"Consumo Estimado: {consumoMensal:.2f} kWh/mês")
print(f"O Custo mensal estimado é de: {custo:.2f}")