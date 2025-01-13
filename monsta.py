# # from random import randrange
# # class Monsta:
# #     def__init__(self, name):
# #         self.name = name
# #         self.hp = 10
# #         self.dmg = randrange(1 , 10)
# #     def info(self):
# #         return f"{self.name} (HP:{self.hp}, DMG:{self.dmg})"
# #     def brainrot(self):
# #         if self.hp >= 9:
# #             self.hp += 1
# #         else:
# #             self.hp += 2
# #     def attack(self, other):
# #         other.hp = other.hp - self.dmg


# # m1 = Monsta("hawk tuah girl")
# # m2 = Monsta("low taper fade meme")
# # print(m1.info())
# # print(m2.info())
# # m1.attack(m2)
# # print(m1.info())
# # print(m2.info())

# #ctrl a then ctrl ?


# # class Person:
# #     def__init__(self, name, wealth):
# #         self.name = name
# #         self.__wealth = wealth #is encapsulated when u put __ in front 
# #     #getter are created to be able to "read" an attribute value
# #     #@property #this is a decorateor
# #     def wealth(self):
# #         return self.__wealth
    
# #     #setter = a controlled way to add a encapsulated attribute
# #     @wealth.setter
# #     def wealth(self, newValue):
# #         self.__wealth = newValue

    
# #     def info(self):
# #         return f"Person(n:{self.name}, w:{self.__wealth})"
# # p1 = Person("Mr park", 69)
# # p2 = Person("Marshall", 1000000)
# # p1.name = "Lebron James"
# # print(p1.__wealth) #cant access encaplusaltes things outside the function
# # p1.wealth = 10000
# # p1.wealth = 69000000
# # print(p1.info())


# # class Book:
# #     def __init__(self, title, author, pages, genre, year):
# #         self.title = title
# #         self.author = author
# #         self.pages = pages
# #         self.type = genre
# #         self.year = year
# #     def__str__(self): #lets our class to be turned into a string
# #         return f"book by {self.author}"
# #     def __repr__(self): # allows our class to be printed even if our objects are in other objects
# #         return self.__str__ #option 1
# #         return f"book({self.title}, {self.author}, {self.year})"
   
# #     @info
    
# #     def info(self):
# #         return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Type: {self.type}, Pages: {self.pages}"

# # b1 = Book()
# # b2 = Book()
# # library = [b1 , b2]
# # print(library)





# class Animal:
#     def __init__(self, name): #overide happening
#         self.name = name  #attribute creation is this line 
#     def __str__(self): #method happening here 
#         return f"Animal({self.name})"
#     def __repr__(self): #method happening here 
#         return self.__str__()
# class Dog(Animal):
#     def __str__(self):
#         return f"Dog ({self.name})"
#     def info(self): #method happening here 
#         return f"yo imma dog named {self.name}"
# a1 = Animal("lion")
# print(a1)
# d1 = Dog("marshall")
# print(d1)
# print(d1.info())

# #disadvantage of inhereitance if u change smth in animal class that gets passed on to every single class that is getting a inheritance of animal class
# #you create dependencies where if 1 gets fucked the rest get fucked together 

class Stack:
    def __init__(self):
        self.__storage = []
        self.__length = 0
        self.__isEmpty = True
    @proptery
    def isEmpty(self):
        return self.__isEmpty
   
    def push(self, value):
        if self.__size == 0:
            self.__isEmpty = False
        self.__size += 1
        self.__storage.append(value)
    def peak(self):
        if self.__size == 0:
            return None
        else:
            return self.__storage[-1]
    def pop(self):
        if self.__isEmpty:
            print("you cant pop an empty stack")
        else:
            self.__size -= 1
            if self.__size == 0:
                self.__isEmpty = True
            return self.__storage.pop()
    def __len__(self):
        return self.__size

test = Stack()
print(f"is our stack empty?: {test.isEmpty}")
test.push("yo")
test.push("how u doin")
print(f"the last value of our stack is: {test.peek()}")
removed = test.pop()
print(f"we popped out: {removed}")
# for things like getters u dont need to have brakets but for every function and method you need brackets

