nota = float(input("Digite sua nota: "))
if nota >= 9:
    print("?? Excelente desempenho!")

else:
    if nota >= 7:
        print("Aprovado!")
    else:
        if nota >= 5:
            print(" Recuperação.")
        else:
            print(" Reprovado.")