import math
import coden
import os

fileExist = os.path.exists("encrypted file.txt")
if not fileExist:
    file = open('encrypted file.txt', 'x')
    file.close()

newList = []


def encrypt(data):
    data *= 8
    data += 128
    data /= 64
    data = data * data
    data = round(data)
    data = hex(data)

    data = (data.replace('0x', '')).upper()

    data = coden.hex_to_bin(data)

    return data


def decrypt(enter):
    global newList
    newList.clear()

    for data in enter:
        data = coden.bin_to_hex(data)
        data.lower()
        data = int(data, 16)
        data = math.sqrt(data)
        data *= 64
        data -= 128
        data /= 8

        data = round(data)

        newList.append(data)

    tempList = []

    for i in newList:
        value = chr(i)
        tempList.append(value)

    tempStr = ''

    for i in tempList:
        tempStr += i

    return tempStr


def option1(message):
    global newList
    for i in message:
        value = ord(i)
        newList.append(encrypt(value))

    return newList


def option2(message):
    listv = []

    for i in message:
        listv.append(i)

    return decrypt(listv)


def option3(enter):
    print(option1(enter))
    newList.clear()
    print(option2(option1(enter)))


print(
    "1 - Encrypt Message and save to file,\n2 - Decrypt Message from file,\n3 - Outputs the encrypted message and decrypted message.")

choice = str(input('Enter 1/2/3: '))

if choice == '1':
    entry = input('Enter data: ')
    listTing = option1(entry)

    tempStr = '['
    index = 0
    for i in listTing:
        if index != len(listTing) - 1:
            tempStr += ("'" + str(i) + "',")
        else:
            tempStr += ("'" + str(i) + "'")
        index += 1

    tempStr += ']'

    file = open('encrypted file.txt', 'w')
    file.write(tempStr)

    print(listTing)

if choice == '2':
    file = open('encrypted file.txt', 'r')
    read = (file.readlines()[0]).replace('[', '').replace(']', '')
    read = read.split(',')
    file.close()

    temp = []

    for i in read:
        temp.append((i.replace("'", '').replace(' ', '')))

    read = temp

    print(option2(read))

if choice == '3':
    entry = input('Enter data: ')
    option3(entry)
