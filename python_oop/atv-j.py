# Write a Python program to create a class representing a queue data structure.
# Include methods for enqueueing and dequeueing elements.


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):  ## add element to the start of the queue
        self.queue.insert(0, value)
        return self.queue

    def dequeue(self):  ## remove element from the front of the queue
        return self.queue.pop()

    def __str__(self):
        return str(self.queue)


def main():
    try:
        queue = Queue()
        print("enqueue 1, 2")
        queue.enqueue(1)
        queue.enqueue(2)
        print(queue)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        print("enqueue 1, 2, 3, 4, 5")
        print(queue)
        print(f"dequeue: {queue.dequeue()}")
        print(queue)
        print(f"dequeue: {queue.dequeue()}")
        print(queue)
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
