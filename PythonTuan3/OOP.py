class Student:
    def __init__(self, name, age, subject, point):
        self.name = name
        self.age = age
        self.subject = subject
        self.point = point

    def get_all_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Point: {self.point}")

    def remove_student(self, name):
        if name == self.name:
            print(f"Đã xóa: {self.name}")

    def update_name(self, newName):
        self.name = newName
        print(f"Đã cập nhật: {self.name}")

student1 = Student("Nghia", 20, "Software Development", 8.2)
student2 = Student("Huy", 20, "Software Development", 7.5)
student3 = Student("Minh", 20, "Software Development", 9.0)

student1.get_all_student()
student2.get_all_student()
student3.get_all_student()

thisDict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

listCompre = [(x,y) for x, y in thisDict.items() if x == "a"]
thisSet = list(listCompre)

print(thisSet)

thisDict = {
    "name": "Nghia",
    "age": 20,
    "gender": "Male"
}

for x in thisDict.values():
    print(x)

x = lambda a, b: a + b
print(x(5, 8))

class Cats:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        print(f"{self.name} says Meow!")