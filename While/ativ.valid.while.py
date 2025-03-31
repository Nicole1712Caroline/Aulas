while True:
    numero = int(input("Digite um número:"))

    if numero < 0:
        print("O número deve ser POSITIVO!")
        continue
    else:
        print("Parabéns o número é POSITIVO!")
        break