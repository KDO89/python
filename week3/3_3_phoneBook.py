from random import choice, randint
def phoneBook():
  """Генерация случайно телефонной книги с уникальными 100000 номерами и записью их в файл"""
  phoneBookTxtAddress = 'D:\\phoneBook.txt'
  phoneBookFile = open(phoneBookTxtAddress, 'w')
  phoneBookDict = {}
  for i in range(0, 100000):
    phoneNumber = 1000000 + i
    name = ""
    for j in range (0, randint(4, 10)):
      name = name + choice('abcdefghijklmnopqrstuvwxyz')
    phoneBookDict[phoneNumber] = name
    phoneBookFile.write(str(phoneNumber) + " : ")
    phoneBookFile.write(phoneBookDict[phoneNumber] + '\n')  
  phoneBookFile.close()
phoneBook()
