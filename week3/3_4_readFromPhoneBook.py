from random import choice, randint
import time

def readFromPhoneBookToDictionary():
  """Чтение из файла телефонной книги в словарь"""
  phoneBookTxtAddress = 'D:\\phoneBook.txt'
  phoneBookFile = open(phoneBookTxtAddress, 'r')
  phoneBookDict = {}
  while True:
    line = phoneBookFile.readline()
    if line == "":
      break
    phoneBookDict[line[:7]] = line[10:]
  phoneBookFile.close()
  #print(phoneBookDict)
  return phoneBookDict
#readFromPhoneBookToDictionary()
  
def readFromPhoneBookToListTuple():
  """Чтение из файла телефонной книги в список кортежей"""
  phoneBookTxtAddress = 'D:\\phoneBook.txt'
  phoneBookFile = open(phoneBookTxtAddress, 'r')
  phoneBookList = []
  while True:
    line = phoneBookFile.readline()
    if line == "":
      break
    phoneBookList = phoneBookList + [(int(line[:7]), line[10:])]
  phoneBookFile.close()
  #print(phoneBookList)
  return phoneBookList
#readFromPhoneBookToListTuple()

def readFromPhoneBookToListTupleSorted():
  """Чтение из файла телефонной книги в список кортежей, отсортированный методом .sort()"""
  phoneBookTxtAddress = 'D:\\phoneBook.txt'
  phoneBookFile = open(phoneBookTxtAddress, 'r')
  phoneBookList = []
  while True:
    line = phoneBookFile.readline()
    if line == "":
      break
    phoneBookList = phoneBookList + [(int(line[:7]), line[10:])]
  phoneBookFile.close()
  phoneBookList.sort()
  #print(phoneBookList)
  return phoneBookList

def getName(phone):
  """Поиск в словаре имени по номеру телефона"""
  phoneBookDict = readFromPhoneBookToDictionary()
  return phoneBookDict[str(phone)]
#getName(1099971)
  
def getNameList(phone):
  """Поиск в списке имени по номеру телефона"""
  phoneBookList = readFromPhoneBookToListTuple()
  for i in range(0, len(phoneBookList)):
    if phoneBookList[i][0] == phone:
      return phoneBookList[i][1]
#getNameList(1000006)

def getNameBin(phone):
  phoneBookList = readFromPhoneBookToListTupleSorted()
  low = 0
  middle = int((len(phoneBookList) - 1) / 2)
  high = len(phoneBookList) - 1
  while phoneBookList[middle][0] != phone and low < high:  
    if phone > phoneBookList[middle][0]:
      low = middle + 1
    else:
      high = middle - 1
    middle = int((low + high) / 2)
  if low >= high:
    print("no item")
  else:
    return phoneBookList[middle][1]
#print(getNameBin(1099981))

def compare_functions(f, g, arg):
  i = 0
  t1 = 0
  t2 = 0
  while i < 1000:
    last_time = time.clock()
    f(arg)
    t1 += time.clock() - last_time
    last_time = time.clock()
    g(arg)
    t2 += time.clock() - last_time
    i += 1
  print(t2 / t1)

#compare_functions(getNameBin, getNameList, 1099982)
  
