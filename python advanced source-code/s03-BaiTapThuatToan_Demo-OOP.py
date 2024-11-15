'''
a = ['Nguyen An', 'Tran Binh', 'Le Chi', 'Vu Duong']

#interchange sort
n = len(a)
for i in range(0, n-1, 1): # 0 -> n-2
    for j in range(i+1, n, 1):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
'''
'''
def sort_evens(a):
    n = len(a)
    for i in range(0, n-1, 1):
        if a[i] % 2 == 0:
            for j in range(i+1, n, 1):
                if a[j] % 2 == 0 and a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
        print(a)
    return a

a = [1, 4, 6, 0, 5, 2, 8]
print(a)
sort_evens(a)
'''
'''
import random

a = [random.randint(0, 100) for i in range(10)]
print(a)

# ky thuat dat co hieu
def get_max(a):
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

print(get_max(a))
'''
'''
class Student:
    def __init__(self, ten='', diem=0.):
        self.name = ten
        self.gpa = diem
    
    def __greet(self):
        print('Hi, I am', self.name)

    def evaluate(self, diem_chuan=7.):
        if self.gpa < diem_chuan:
            return 'failed'
        else:
            return 'pass'

    def __str__(self):
        return self.name + '_' + str(self.gpa)


an = Student()
print(str(an))
'''
'''
class Student:
    count = 0

    def __init__(self, name, gpa=0):
        self._name = name
        self._gpa = gpa
        Student.count += 1

    @staticmethod
    def print_classname():
        print('Student')

print(Student.count)
a = Student('A')
print(Student.count)
b = Student('B')
print(Student.count)

Student.print_classname()
'''

class Vehicle:
    def __init__(self, category, max_speed):
        self._category = category
        self._max_speed = max_speed
        self._distance = 0

    def run(self, distance, duration):
        avg_speed = distance / duration

        actual_distance = 0
        if avg_speed > self._max_speed:
            actual_distance = self._max_speed * duration
        else:
            actual_distance = distance
        self._distance += actual_distance

        return actual_distance

v = Vehicle('Car', 200)
print(v.run(1000, 1))
print(v._distance)
print(v.run(150, 3))
print(v._distance)