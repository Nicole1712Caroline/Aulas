lista = []

while True:
    addItem = input('Adicione um Item: ')
    if addItem == 'fim':
        break

    lista.append(addItem)

print(f'O tamanho da minha lista é: {len(lista)}')