import csv
from ast import literal_eval


d = {}


def initialize():
    with open("../users.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(reader):
            d[i] = {'nome': row[0], 'idade': row[1],
                    'ocupacao': row[2], 'lista': literal_eval(row[3])}


def insertUser(name, age, occupation, friends):
    idx = len(d)
    d[idx] = {'nome': name, 'idade': age,
              'ocupacao': occupation, 'lista': []}
    for friend in friends.split(','):
        friend = str(friend)
        if int(friend) in d:
            d[idx]['lista'].append(int(friend))
            d[friend]['lista'].append(idx)
        else:
            print(friend + " não existe")


def removeFriend(index, friendIndex):
    if friendIndex in d[index]['lista']:
        d[index]['lista'].remove(friendIndex)
        d[friendIndex]['lista'].remove(index)
    else:
        print(friendIndex + " não é amigo de " + d[index]['nome'])


def removeUser(index):
    del d[index]
    for key in d:
        if index in d[key]['lista']:
            d[key]['lista'].remove(index)


def findUser(index):
    return d[index]


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
    if mostFriends == 0:
        print("Nenhum usuario possui amigos")
        return
    print(mostFriendUser + " é o usuario com mais amigos " +
          str(mostFriends) + " amigos")


def main():
    initialize()
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
