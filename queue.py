"""Queue Exercise"""

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
    
    def getItems(self):
        return self.queue


input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('test1')
input_queue.enqueue('test2')
input_queue.enqueue('test3')

print(input_queue.getItems())

key_pressed = input_queue.dequeue() # 'test1'
key_pressed = input_queue.dequeue() # 'test2'
key_pressed = input_queue.dequeue() # 'test3'

print(input_queue.getItems())

