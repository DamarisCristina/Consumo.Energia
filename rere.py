temperatura = (float(input ("Qual é a temperatura atual?")))
if temperatura <0:
    print ("Temperatura abaixo de zero! Cuidado com o congelamento.")

elif temperatura <15:
    print("Frio intenso no laboratório.")

elif temperatura <25:
    print("Temperatura agradável.")

else:
    print("Temperatura alta! Ligar sistema de refrigeração.")