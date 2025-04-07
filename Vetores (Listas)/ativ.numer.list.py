itens = []
print("Bem vindo a lista de itens automática!")
while True:
    print(" ")
    print("1 para Adicionar itens na sua lista, ")
    print( "2 para Remover itens da sua lista,")
    print("3 para Ver o Tamanho da sua lista,")
    print("4 para Ver os Itens,")
    print("5 para Sair.")
    print(" ")
    decisao = int(input("O que deseja fazer? "))
    if decisao == 1:
        itens.append(input("Adicione o item: "))
        continue
    elif decisao == 2:
        itens.remove(input("Qual item deseja remover?"))
        continue
    elif decisao == 3:
        tamanhodaLista = len(itens)
        print(f'O tamanho da Lista é: {tamanhodaLista}')
    elif decisao == 4:
        for i in itens:
            print(i)
    elif decisao == 5:
        print("Obrigado por usar a lista automática!")
        break
    else:
        print("Esse comando não existe!!")