import random


def arrival(x):
    if x == 1:
        return 5
    elif 2 <= x <= 5:
        return 6
    elif 6 <= x <= 8:
        return 7
    else:
        return 8


def transaction(x):
    if 1 <= x <= 15:
        return 2
    elif 16 <= x <= 65:
        return 3
    elif 66 <= x <= 85:
        return 4
    else:
        return 5


total_student = 100
current_time = 0
wait_count = 0
balking = 0

arrival_time = []
transaction_time = []

transaction_time_begin = []
transaction_time_end = []

waiting_time = []
idle_time = []
spend_in_system = []

for i in range(total_student):
    if i == 0:
        arrival_time.append(0)
    else:
        interArrivalTime = arrival(random.randint(0, 9))
        arrival_time.append(interArrivalTime + arrival_time[i - 1])

    transaction_time.append(transaction(random.randint(0, 99)))

    transaction_time_begin.append(max(current_time, arrival_time[i]))
    waiting_time.append(transaction_time_begin[i] - arrival_time[i])
    transaction_time_end.append(transaction_time_begin[i] + transaction_time[i])

    if waiting_time[i] != 0:
        wait_count += 1

    current_time = transaction_time_end[i]

# print(arrival_time)
# print(transaction_time)

balking_rate = ((wait_count / 3) / total_student) * 100
print('Balking Rate = %.2f%% \n' % balking_rate)