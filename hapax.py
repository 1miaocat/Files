# import re

# book = open('In His Image.txt', 'r')
# text = book.read().lower()

# word_regex = re.compile(r'\w+')
# word =  word_regex.findall(text)
# hapax_dict = {}
# for i in word:
#     hapax_dict[i] = hapax_dict.setdefault(i, 0) + 1
#     for i in hapax_dict:
#         if hapax_dict[i] == 1:
#             print(i)
import string

def replacePunc(stringValue):
    dPunc = string.punctuation

    for i in dPunc:
        stringValue = stringValue.replace(i,'')

    return stringValue

def hapax(filename):
    filename = filename.lower()

    readFile = open(filename, 'r')
    data = readFile.read().lower()
    data = data.split()

    listOccurs = {}
    for i in data:
        current = replacePunc(i)
        listOccurs.setdefault(current,0)
        listOccurs[current] += 1

    print('Total words: ' + str(len(listOccurs)))
    print('Happax words: ')
    for i in listOccurs.keys():
        nOccurs = listOccurs.get(i)
        if nOccurs == 1:
            print(i, end=',')
    print('Most common word')
    maximum = max(listOccurs, key = listOccurs.get)
    print(maximum,listOccurs[maximum])

def get_average(filename):
    filename = filename.lower()

    readFile = open(filename, 'r')
    data = readFile.read().lower()
    data = data.split()

    for i in data:
        totalLengthWord += len(i)
    average = totalLengthWord / len(data)
    return average

hapax('inHisImage.txt')
print(get_average('inHisImage.txt'))
