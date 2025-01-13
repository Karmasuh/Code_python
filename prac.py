#firstName = input("what is the first name")
#lastName = input("what is the last name")
#birthYear = int(input("when were you born"))
#print(f'', firstName, " ", lastName, " ", birthYear )
#age = 2024 - birthYear
#if age >= 18:
#    print("you are old enough to drink")
#else: print("you are too young")

#time = int(input("tell me how much time you have"))
#tasksCount = int(input("how many tasks do you have"))
#totalTime = []
#for i in range (tasksCount):
   # howLong = int(input("type in how long the first task takes"))
  #  totalTime.append(howLong)
 #   totalTime.sort()
#i = 0
#choresDone = 0
#while time > 0:
  #  if totalTime[i] > time:
     #   break
    #else:
   #     time -= totalTime[i]
  #      choresDone += 1
 #       i += 1
#print(choresDone)

#tileCount = int(input("type in how many tiles u got"))
#luckyShot = pow(tileCount,1/2)
#trueNum = luckyShot//1
#print(f"the biggest square u can make is with the side lengths ", {trueNum})

#sections = 3
#paintNeeded = 0
#for i in range (sections):
#   fenceCount = input()
 #  length = len(fenceCount)
  # paintNeeded += length
#fT = paintNeeded % 12
#count = (paintNeeded - fT) / 12
#if fT > 0:
 #  cost = count * 14.95
  # cost += 14.95
#else:
 #  cost = count * 14.95
#print(f"the cost needed is ", {cost}, " and u need ", {paintNeeded}, " paint cans")

#how = int(input("how much money u got"))
#bigCookie = 0.75
#smallCookie = 0.5
#costBigCookie = 2
#costSmallCookie = 1.25
#cookieOrder = input("type in how many cookies u sold")
#for i in cookieOrder:
 #  if i == "b":
  #    how += costBigCookie - bigCookie
   #else:
 #     how += costSmallCookie - smallCookie
#print(f"u now have ", {how}, " money")
#ask

#month = int(input("type in the month number"))
#date = int(input("day number"))
#if month > 2:
#  print("after")
#elif month < 2:
#  print("before")
#elif date > 18:
#  print("after")
#elif date < 18:
#  print("before")
#else:
#  print("special")

#number = input("type in the last 4 digits of a telemarketer number ")
#if number[0] == '9' or number[0] == '8':
#  if number [1] == number [2]:
#    if number[3] == '9' or number[3] == '8':
#      print("this number is a telemartketer number")

#password generator 
#import random 

#passwordLength = int(input("enter the length of the password"))
#lowerCase = list(range(97 , 123))
#upperCase = list(range(65 , 91))
#specialChar = list(range(33 , 48)) + list(range(58 , 65)) + list(range(91 , 97)) + list(range(121 , 127))
#digits = list(range(48 , 58))

#passwordSymbols = lowerCase.copy()
#hasUpper = input("does ur password have upper case letters")
#if hasUpper == 'Y' or hasUpper == 'y':
 # passwordSymbols.extend(upperCase)

#hasSpecial = input("does ur password have special characters")
#if hasSpecial == 'Y' or hasSpecial == 'y':
#  passwordSymbols.extend(specialChar)

#hasDigits = input("does ur password have digits")
#if digits == 'Y' or digits == 'y':
#  passwordSymbols.extend(digits)

#newPassword = ""
#for i in range(passwordLength):
#  randomSymbol = chr(random.choice(passwordSymbols)) #chr turns the numbers found in the ascii table into their respective characters 
#  newPassword = newPassword + randomSymbol

#print(f'your new pass word is ', {newPassword})

#adding capitals and countries in 2 separate lists 
#def dataMaker(capitals):
  #city = []
  #country = []
  #for i in range(len(capitals)):
    #if i % 2 == 0:
    #  city.append(capitals[i])
   # else: 
  #    country.append(capital[i])
  #return city , country # this returns a tuple becuase a function can't return multiple items so it turns the lit into a tuple 

#aDict = {}
#for i in range(len(city)):
 # aDict[country[i]] = city[i]
#country.sort()
#city = []
#for c in country:
#  city.append(aDict[c])

#function practice/bubble sort

#def sortt(array):
#  i = 1
#  if not array:
#    return []
 # elif len(array) == [1]:
 #   return array
#  else:
  #  while i < len(array):
 #     j = i
#      while j > 0 and array[j - 1] > array[j]:
      #  l = array[j]
     #   array[j] = array[j - 1]
    #    array[j - 1] = l
   #     j -= 1
  #    i += 1
 #   return array
#aList = [13 , 12 , 17, 16 , 5]
#sortt(aList)
#print(f'the array is ' , aList)


#recursion problems

#def multip(num):
#  if num == 0:
#    return 0
#  elif num == 1:
#    return 1
#  else:
#    return num * multip(num - 1)
#print(f"the thing fully multiplyed is " , multip(6))


#def expo(base,power):
#  if power == 0:
#    return 1
#  elif power == 1:
#    return base
#  else: 
#    return base * expo(base , power - 1)
#print(f"the answer is " , expo(2,4))

#ask tmrw
#def palindrome(word):
#  aList = list(word)
#  j == len(aList) - 1
#  if word == "":
#    return "is a palindrome"
#  elif len(word) == 1:
#    return "yes is a palindrome"
#  else:
#    for i in range(0, len(aList)//2):
#      if aList[i] == aList[j]:
#        j -= 1
#      else:
#        return "not a palindrome"
#    return "is a palindrome"
#value = "hello"
#print(f"the word  " , palindrome(value))

#aList = [1 , 5 , 7 , 2]
#bList = []

#while aList:
#  bList.append(min(aList))
#  aList.remove(min(aList))
#print(bList)

#def func(array , array2):
#  if not array:
#    return []
#  elif len(array) == 1:
#    return array
#  else:
#    while array:
#      array2.append(min(array))
#      array.remove(min(array))
#    return array2
#print(f"the sorted list is " , func(aList , bList))


#methods are just functions that belong to a class
# first oop 
class Dog:
  def__init__(self , name):
    self.name == name
  def bark(self, scared):
    if scared:
      return "woof"
    else:
      return "BARK BARK"
dog1 = Dog("Marshall", "westie")
dog2 = Dog("Freya" , "samoyed")
print(dog1.name , dog2.breed)
print(dog2.name , dog2.breed)
print(dog1.bark(True))
print(dog2.bark(False))