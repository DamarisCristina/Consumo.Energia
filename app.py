aparelho = input ("Qual o nome do aparelho? ")
potencia = float(input("Qual a potência do aparelho em watts (W): "))
horasdia = float (input ("Qual o tempo médio de uso diário em horas? "))

consumoMensal = (potencia*horasdia*30) / 1000
custo = consumoMensal * 0.65

print(f"Aparelho: {aparelho}")
print(f"Consumo Estimado: {consumoMensal:.2f} kWh/mês")
print(f"Um watt é R$0,65. Sendo assim o custo total de Watts é de: {custo:.2f}")