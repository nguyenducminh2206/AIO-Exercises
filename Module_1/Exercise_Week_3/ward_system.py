class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name} - YOB: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - Name: {self.name} - YOB: {self.yob} - Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - Name: {self.name} - YOB: {self.yob} - Subject: {self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YOB: {self.yob} - Specialist: {self.specialist}"


class Ward:
    def __init__(self, name):
        self.name = name
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.persons)

    def sort_age(self):
        return sorted(self.persons, key=lambda x: x.yob)

    def compute_average(self):
        teachers = [
            person for person in self.persons if isinstance(person, Teacher)]
        if teachers:
            return sum(person.yob for person in teachers) / len(teachers)
        return None


# Create instances
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")

# Create ward and add persons
ward = Ward(name="Ward1")
ward.add_person(student1)
ward.add_person(teacher1)
ward.add_person(doctor1)

# Output descriptions and counts
for person in ward.persons:
    print(person.describe())

print("Number of doctors:", ward.count_doctor())
print("Sorted by age:", [person.describe() for person in ward.sort_age()])
print("Average YOB of teachers:", ward.compute_average())
