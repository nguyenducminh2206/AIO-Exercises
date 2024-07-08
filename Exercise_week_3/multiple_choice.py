# Question 8
print('Question 8')


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


student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.count_doctor())

# Question 9
print('Question 9')


class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.capacity - 1

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
            self.top_idx += 1
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            self.top_idx -= 1
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def top(self):
        if not self.is_empty():
            return self.stack[self.top_idx]
        else:
            raise Exception("Stack is empty")


stack1 = MyStack(capacity=5)
stack1.push
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())

# Question 10
print('Question 10')
print(stack1.top())

# Question 11
print('Question 11')


class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        temp = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.size -= 1
        return temp

    def get_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())

# Question 12
print('Question 12')

print(queue1.get_front())