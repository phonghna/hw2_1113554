# question4.py
# 湖阮英風
# 1113554
# Date of Submission: TBD

import heapq

def schedule_tasks(tasks):
    tasks.sort(key=lambda x: -x[0])  # Sort by profit in descending order
    max_deadline = max(task[1] for task in tasks)
    result = [None] * max_deadline
    max_profit = 0

    for profit, deadline in tasks:
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if result[i] is None:
                result[i] = profit
                max_profit += profit
                break

    scheduled_tasks = [task for task in result if task is not None]
    return max_profit, scheduled_tasks


#READ THIS: if you are lazy to type the input then comment all the lines inside "input zone" and uncomment the "lazy input"

#------INPUT ZONE---------
tasks = []
n = int(input("Enter number of tasks: "))
for i in range(n):
    data = tuple(map(int, input().split()))
    tasks.append(data)
#-----INPUT ZONE----------

#------LAZY INPUT---------
#tasks = [(100, 2), (19, 1), (27, 2), (25, 1)]
#-----LAZY INPUT---------


print("Inputed tasks: ", tasks)


max_profit, scheduled_tasks = schedule_tasks(tasks)
scheduled_tasks.reverse()
print("\nOutput:")
print("Maximum Profit:", max_profit)  # Output: 127
print("Scheduled Tasks:", scheduled_tasks)  # Output: [100, 27]

