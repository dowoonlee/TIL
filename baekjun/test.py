import sys

###한 개의 정수를 입력받을 때
#n = int(sys.stdin.readline())

###정해진 개수의 정수를 한줄에 입력받을 때
#a, b = map(int, sys.stdin.readline().split())

###임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
#data = list(map(int,sys.stdin.readline().split()))


###임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
#data = []
#n = int(sys.stdin.readline())
#for i in range(n):
#    data.append(list(map(int,sys.stdin.readline().split())))

###문자열 n줄을 입력받아 리스트에 저장할 때
#import sys
#n = int(sys.stdin.readline())
#data = [sys.stdin.readline().strip() for i in range(n)]



class Doggy:
    def __init__(self,name_dog, type_dog):
        self.name_dog = name_dog
        self.type_dog = type_dog
        self.num_of_dogs = 0
        self.birth_of_dogs = 0

    @staticmethod
    def birth(cls):
        cls.num_of_dogs += 1
        cls.brith_of_dogs += 1
    @staticmethod
    def death(cls):
        cls.num_of_dog -=1
    @staticmethod
    def bark():
        print('Bow Wow')
    def get_status(self):
        return Doggy.num_of_dogs, Doggy.birth_of_dogs

a = Doggy('k', 'www')

a.birth(a)
print(a.num_of_dogs)