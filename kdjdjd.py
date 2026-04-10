opcao = input ("Digite uma opção (1 - PCs. 2 - manutenção. 3 - Regras): ")
manutencao = input ("Digite qual computador é necessário de manutenção: ")

match opcao:
    case "1" |"um" | "Um":
        print("Esses são os computadoress disponíveis: L445 e F53.")
    case "2"|"dois" | "Dois":
        print("Abrindo chamado para manutenção do computador {manutencao}, descreva o problema: ")
    case "3"|"três" | "Três":
        print('Regras: uso individual, silêncio e não alterar configurações')
    case _:
        print ("Opção inválida. Tente novamente.")

print(f"O computador {manutencao} precisa de manunteção.")