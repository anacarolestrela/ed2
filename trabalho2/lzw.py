from ast import literal_eval


def createAscDictionary():
    table = {}
    for i in range(256):
        table[chr(i)] = i
    return table


def loadCSVContent(filename):
    data = []
    with open(filename, 'r') as csvfile:
        data = csvfile.read()
    return data


def lzwCompress(data, dictionary):
    compressedData = []
    p = ''
    for i in range(len(data)):
        c = data[i]
        if p + c in dictionary:
            p = p + c
        else:
            compressedData.append(dictionary[p])
            dictionary[p + c] = len(dictionary)
            p = c
    if p != '':
        compressedData.append(dictionary[p])
    return compressedData


def writeCompressedDataToFile(dictionary, data):
    with open('lzwCompressed', 'w') as file:
        file.write(dictionary)
        file.write('\n')
        file.write(data)


def decompressLZWDataFromFile(filename):
    with open(filename, 'r') as file:
        [dictionary, compressed] = file.read().split('\n')
        compressedArray = literal_eval(compressed)
        dict = literal_eval(dictionary)
        for i in compressedArray:
            value = list(dict.values()).index(i)
            key = list(dict.keys())[value]
            print(key, end='')


def main():
    dictionary = createAscDictionary()
    users = loadCSVContent('lzw.csv')
    compressedUsers = lzwCompress(users, dictionary)

    writeCompressedDataToFile(str(dictionary), str(compressedUsers))
    decompressLZWDataFromFile('lzwCompressed')


main()
