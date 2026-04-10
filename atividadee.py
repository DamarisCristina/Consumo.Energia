print("Para seguirmos com a avaliação da empresa TudoWeb, nos informe seu nome, idade e a sua avaliação sendo: excelente, bom ou ruim.")

excelente = 0
ruim = 0
contador = 1

for i in range(1,3):   
    nome = input("Digite seu nome: ")
    idade = (int(input("Digite sua idade: ")))
    opniao = input("Sua opnião sobbre o atendimento prestado: ")
    print(f"Nome {nome}, idade {idade} e avaliação do atendimento {opniao}")
    contador +=1

    if opniao == "excelente" or opniao == "Excelente" or opniao == "EXCELENTE":
        print("Ficamos felizes que sua nota seja excelente!")

    elif opniao == "Ruim" or opniao == "ruim":
        ruim += 1
        print("Agradecemos o feedback e vamos melhorar!")

    else:
        print("Não entendemos sua resposta")

print(f"O total de pessoas que avaliaram com Excelente foi {excelente} e o total de pessoas que avaliaram com ruim foi {ruim}")