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
queue1.enqueue(2)

print(queue1.is_full())  # Output: False
print(queue1.get_front())    # Output: 1
print(queue1.dequeue())  # Output: 1
print(queue1.get_front())    # Output: 2
print(queue1.is_empty())  # Output: False
