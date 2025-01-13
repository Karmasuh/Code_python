roomNums = (2, 216, 15, 109, 156, 120, 93, 18, 21, 56)
def bills(number, kkk = roomNums):
    if number in roomNums:
        return "paid"
    else:
        return "havent paid"
x = int(input("type in number"))
people = bills(x)
print(f"the people in room ", {x}, {people})
listB = []
listA = list(roomNums)
g = len(listA)
while x > 0:
    maxValue = max(listA)
    listA.remove(maxValue)
    listB.append(maxValue)
print(listB)

#separate codes 
def pow1(base, exponent):
  if exponent = 1:
    return 1
  elif exponent = 0:
    return base
  else: #work toward base case
    return base * pow1(base, exponent - 1) #recursive function call
print(pow1(3, 5))

def pow2(base, exponent, answer=1):
  if exponent == 0:
    return answer
  else:
    return pow2(base, exponent-1, answer * base)
print(pow2(3,5))

def isPali(word):
  def helper(word, left, right):
    if left > right:
      return True
    elif word(left) != word(right):
      return False
    else:
      return helper(word, left+1, right-1)
  if not word:
     return True
  elif len(word) <= 3:
    return word(0) == word(-1)
  else:
    retunr helper(word, left=0, right=len(word)-1)




def maximum(aList):
  if not aList:
    return - 1 #a common error code for programming
  elif len(aList) == 1:
    return aList[0]
  elif len(aList) == 2:
    if aList[0] > aList[1]:
