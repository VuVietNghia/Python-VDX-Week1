class Student:
    def __init__(self, id, name, point, subject):
        self.id = id
        self.name = name
        self.point = point
        self.subject = subject

student1 = Student(1, "Nghia", 8.2, "Software Development")
student2 = Student(2, "Huy", 7.5, "Software Development")
student3 = Student(3, "Minh", 9.0, "Software Development")

print(f"Student 1: ID {student1.id}, Name {student1.name}, Point {student1.point}, Subject {student1.subject}")
print(f"Student 2: ID {student2.id}, Name {student2.name}, Point {student2.point}, Subject {student2.subject}")
print(f"Student 3: ID {student3.id}, Name {student3.name}, Point {student3.point}, Subject {student3.subject}")
