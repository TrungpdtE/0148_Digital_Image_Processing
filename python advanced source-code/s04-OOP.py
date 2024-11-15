'''

class Vehicle:
    def __init__(self, max_speed):
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

class Bus(Vehicle):
    def __init__(self, max_speed, name, capaticy):
        super().__init__(max_speed)
        self._name = name
        self._capacity = capaticy
        self._num_passenger = 0

    def run(self, distance, duration, num_passenger_in, num_passenger_out):
        super().run(distance, duration)
        self._num_passenger = self._num_passenger + num_passenger_in \
                                - num_passenger_out
        if self._num_passenger > self._capacity:
            self._num_passenger = self._capacity
        
b = Bus(60, '01', 40)
for pi, po in [(10, 0), (10, 5), (5, 10), (3, 10)]:
    b.run(60, 1, pi, po)
    print(b._num_passenger)

'''

class Faculty():
    def __init__(self, name):
        self._name = name
        self._list_students = []

    def notify(self, message):
        for std in self._list_students:
            std.onReceive(message)

    def register(self, std):
        if std not in self._list_students:
            self._list_students.append(std)

    def unregister(self, std):
        if std in self._list_students:
            self._list_students.remove(std)

class OnNotifyListener:
    def onReceive(self, message):
        pass

class Student(OnNotifyListener):
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def onReceive(self, message):
        print(self._name, message)

faculty = Faculty('FIT')
s1 = Student('A', 2020)
s2 = Student('B', 2021)
s3 = Student('C', 2022)

faculty.register(s1)
faculty.register(s2)
faculty.register(s3)

faculty.notify('Đăng ký học phần')
