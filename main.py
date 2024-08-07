# CRUD create, read, update e delete - fundamentos de LISTA
#lista de compras
compras = ['ovos', 'macarrao', 'feijão', 'arroz', 'leite', 'chocolate']

#exibir lista
for i in range(len(compras)):
    print(f'Inice {i}: {compras[i]}.')

#usurio informa o item que deseja retirar - tratamento de exceção try
try:
    indice = int(input('\nInforme o indice do item a ser retirado: '))
    del(compras[indice]) # comando para deletar del(aqui dentro a variavel que tem os itens[aqui dentro a variavel de indices])
    print('\nItem retirado com sucesso.\n')

except:
    print('\nNão foi possivel excluir.\n')
finally: # comando que mostra a lista de itens de novo quando a opção escolhida for a exceção
    for i in range(len(compras)):
        print(f'Indice {i}: {compras[i]}.')

    
