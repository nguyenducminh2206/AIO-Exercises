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


def main():
    capacity = int(input("Enter the capacity of the stack: "))
    stack = MyStack(capacity)

    while True:
        choice = input(
            "1) Push 2) Pop 3) Show Top 4) Full 5) Empty 6) Quit\n-> ")

        if choice == '1':
            element = int(input("Enter an element to push: "))
            stack.push(element)
        elif choice == '2':
            pop_element = stack.pop()
            print(f"Popped element: {pop_element}")
        elif choice == '3':
            top_element = stack.top()
            print(f"Top element: {top_element}")
        elif choice == '4':
            if stack.is_full():
                print("True")
            else:
                print("False")
        elif choice == '5':
            if stack.is_empty():
                print("True")
            else:
                print("False")
        elif choice == '6':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
