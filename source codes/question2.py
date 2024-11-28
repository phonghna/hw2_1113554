# question2.py
# 湖阮英風
# 1113554
# Date of Submission: TBD

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add_task(self, task_name, priority):
        heapq.heappush(self.heap, (-priority, task_name))

    def get_highest_priority_task(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def display_remaining_tasks(self):
        return sorted([(t, -p) for p, t in self.heap])


#READ THIS: if you are lazy to type the input then comment all the lines in the line "input zone" and uncomment the "lazy input". 
#------------input zone--------------
commands = []
num_ops = int(input("Enter the number of operations: "))
for i in range(num_ops):
    data = input()
    commands.append(data)
#------------input zone--------------

#----------------LAZY INPUT_-----------------
#commands = ["ADD Task1 10", "ADD Task2 15", "ADD Task3 5", "GET", "ADD Task4 20", "GET"]
#----------------LAZY INPUT-------------------


print("Your commands:", commands)
pq = PriorityQueue()

print("\n\nOutput:")
for cmd in commands:
    if cmd.startswith("ADD"):
        _, task, priority = cmd.split()
        pq.add_task(task, int(priority))
    elif cmd == "GET":
        print(pq.get_highest_priority_task())

print("Remaining tasks:", pq.display_remaining_tasks())

