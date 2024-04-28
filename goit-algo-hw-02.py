# Завдання 1:
from queue import Queue
import random

q = Queue()

def generate_request():
    unique_id = random.randint(1, 10)
    q.put(unique_id)
    print("Generate request")
    print("Queue content:", list(q.queue))
    print("Queue size:", q.qsize())

def process_request():
    if not q.empty():
        print("Process request")
        ticket = q.get()
        print("Processed ticket ID:", ticket)
        print("Queue content:", list(q.queue))
        print("Queue size:", q.qsize())
    else:
        print("You do not have any request")

try:
    while True:
        generate_request()
        process_request()
except KeyboardInterrupt:
    print("Program has been stopped by the user.")

# Завдання 2: 
from collections import deque

def is_palindrome(s):
   # Create a deque with characters of the string directly
    d = deque(s)
    
    # Compare symbols from both ends
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True



