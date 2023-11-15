d = {
    'Yan': {'idade': 25, 'ocupacao': 'Estudante', 'lista': ['Ana']},
    'Ana': {'idade': 20, 'ocupacao': 'Estudante', 'lista': ['Yan']}
}

def insertUser(name, age, occupation, friends):
    d[name] = {'idade': age, 'ocupacao': occupation, 'lista': []}
    for friend in friends.split(','):
        if friend in d:
            d[friend]['lista'].append(name)
            d[name]['lista'].append(friend)
        else:
          print(friend +" não existe")

def removeFriend(name, friend):
    if friend in d[name]['lista']:
        d[name]['lista'].remove(friend)
        d[friend]['lista'].remove(name)
    else:
        print(friend +" não é amigo de "+ name)

def removeUser(name):
    del d[name]
    for key in d:
        if name in d[key]['lista']:
          d[key]['lista'].remove(name)

def findUser(name):
    return d[name]

def printAlfabetical():
    for key in sorted(d.keys()):
        print(key, d[key])

def calculateMostFriends():
    mostFriendUser = ''
    mostFriends = 0
    for key in d:
        if len(d[key]['lista']) > mostFriends:
            mostFriendUser = key
            mostFriends = len(d[key]['lista'])
    print(mostFriendUser + " é o usuario com mais amigos " + str(mostFriends) + " amigos")

def main():
    print('Escolha uma opcao:')
    print('1 - Inserir usuario')
    print('2 - Remover amigo')
    print('3 - Remover usuario')
    print('4 - Buscar usuario')
    print('5 - Imprimir usuarios em ordem alfabetica')
    print('6 - Exibir quem tem mais amigos')
    print('0 - Sair')

    value = int(input('Digite o valor: '))
    print("-------------------")

    if value == 1:
        name = input('Digite o nome: ')
        age = int(input('Digite a idade: '))
        occupation = input('Digite a ocupacao: ')
        friends = input('Digite os amigos: ')
        insertUser(name, age, occupation, friends)
    elif value == 2:
        name = input('Digite o nome: ')
        friend = input('Digite o amigo: ')
        removeFriend(name, friend)
    elif value == 3:
        name = input('Digite o nome: ')
        removeUser(name)
    elif value == 4:
        name = input('Digite o nome: ')
        print(findUser(name))
    elif value == 5:
        printAlfabetical()
    elif value == 6:
        calculateMostFriends()
    elif value == 0:
        exit()
    print("-------------------")
    main()

main()
