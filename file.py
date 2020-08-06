# Start
nameCliente = 'Enter your name:'
print('Be welcome {:=^50}!'.format(nameCliente))

# Itens
term = 'Item'
itemOne = int(1)
itemTwo = int(2)
itemTree = int(3)
itemFour = ''

print(term, ' {:*^5}, {:*^5} or {:*^5}'.format(itemOne, itemTwo, itemTree))
# Item **1**, **2** or **3**

# Select Itens
select = input('Select your item')
select = input('Select term')

listItens = list()
listItens.append('item list 01')

listItens2 = list()
listItens2.append(listItens[:])

def printItens(* dados)
    x = 0
    for num in dados
        x += num
    print('Itens {x} values')