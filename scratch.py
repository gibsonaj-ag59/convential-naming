import threading
import time

# Function to print items in an iterable
def print_items(iterable):
    for item in iterable:
        print(item)

# Define an iterable
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Create threads targeting the print_items function with different iterables
thread1 = threading.Thread(target=print_items, args=(my_list,))
thread2 = threading.Thread(target=print_items, args=(my_dict.items(),))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads finished execution.")
