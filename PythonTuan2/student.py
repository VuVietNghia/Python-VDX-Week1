class Student:
    def __init__(self, id, name, point, subject):
        self.id = id
        self.name = name
        self.point = point
        self.subject = subject

    def displayStudent(self):
        print(f"ID: {self.id}, Name: {self.name}, Point: {self.point}, Subject: {self.subject}")

    def update_name(self, newName):
        self.name = newName
        print(f"Đã cập nhật: {self.name}")

student1 = Student(1, "Nghia", 8.2, "Software Development")
student2 = Student(2, "Huy", 7.5, "Software Development")
student3 = Student(3, "Minh", 9.0, "Software Development")

print(f"Student 1: ID {student1.id}, Name {student1.name}, Point {student1.point}, Subject {student1.subject}")
print(f"Student 2: ID {student2.id}, Name {student2.name}, Point {student2.point}, Subject {student2.subject}")
print(f"Student 3: ID {student3.id}, Name {student3.name}, Point {student3.point}, Subject {student3.subject}")

b = {
    "name": "Nghia",
    "age": 20,
    "gender": "Male"
}

a = ("Nghia", 20, "Male")

c = {"Nghia", "Son", "Minh"}
searchInput = input("Nhap gia tri can tim: ")

if searchInput in c:
    print("Tim thay")
else:
    print("Khong tim thay")

print(a[2])

print(b["name"])

setList = {"Nghia", "Son", "Truong"}
print(setList)

for x in setList:
    print(x)