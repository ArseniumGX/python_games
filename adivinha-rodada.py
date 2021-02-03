import random

print("+------------------------------+")
print("|           The Game           |")
print("+------------------------------+")
print("\nObjetivo: Adivinhe o número. Simple e fácil.\nO número secreto é gerado aleatoriamente entre 0 e 100\nBoa sorte!\n\n")
print("Escolha a dificuldade desejada: ")
print("_____ 1 - Easy")
print("_____ 2 - Medium")
print("_____ 3 - Hard")

numero_secreto = random.randint(0, 100)
total_tentativa = None
dificuldade = int(input("_____:"))
pontuacao = 1000

if dificuldade == 1:
    total_tentativa = 20
elif dificuldade == 2:
    total_tentativa = 10
elif dificuldade == 3:
    total_tentativa = 5
else:
    print("Opção inválida, aplicação encerrada!\nExecute novamente para tentar de novo.")
    exit()



for rodada in range(1, total_tentativa + 1):
    print("Tentativa {} de {}. Você tem {} pontos".format(rodada, total_tentativa, pontuacao))

    chute = int(input("Digite um número: "))

    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acerto:
        print("Parabéns, vc acertou!")
        print("\n\nVocê fez {} pontos".format(pontuacao))
        break
    elif maior: # Equibalente a else if
        print("É menos!\n\n")
    elif menor:
        print("É mais!\n\n")
    
    pontuacao = pontuacao - abs(chute - numero_secreto)

print("\n\n\n\nObrigado por jogar meu joguinho!")