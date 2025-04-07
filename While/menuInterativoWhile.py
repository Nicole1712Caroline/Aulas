while True:
    operacao = input("Digite uma operação: (+ / - / *)")

    if operacao == '+':
        numero1 = int(input("Digite 1° número que deseja somar: "))
        numero2 = int(input("Digite 2° número que deseja somar: "))
        print(f"O resultado da sua operação é: {numero1+numero2}")
        continue
    elif operacao == '-':
        numero1 = int(input("Digite 1° número que deseja subtrair: "))
        numero2 = int(input("Digite 2° número que deseja subtrair: "))
        print(f"O resultado da sua operação é: {numero1 - numero2}")
        continue
    elif operacao == '*':
        numero1 = int(input("Digite 1° número que deseja multiplicação: "))
        numero2 = int(input("Digite 2° número que deseja multiplicação: "))
        print(f"O resultado da sua operação é: {numero1 * numero2}")
        continue