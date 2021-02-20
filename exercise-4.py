import random


def arrival(x):
    if 1 <= x <= 20:
        return 5
    elif 21 <= x <= 90:
        return 6
    else:
        return 7


def duration(x):
    if 1 <= x <= 15:
        return 2
    elif 16 <= x <= 75:
        return 3
    elif 76 <= x <= 90:
        return 4
    else:
        return 5


total_callers = 100
current_time = 0
wait_count = 0

arrival_time = []
call_duration = []

call_duration_begin = []
call_duration_end = []

waiting_time = []
idle_time = []
spend_in_system = []

for i in range(total_callers):
    if i == 0:
        arrival_time.append(0)
    else:
        interArrivalTime = arrival(random.randint(0, 99))
        arrival_time.append(interArrivalTime + arrival_time[i - 1])

    call_duration.append(duration(random.randint(0, 99)))

    call_duration_begin.append(max(current_time, arrival_time[i]))
    waiting_time.append(call_duration_begin[i] - arrival_time[i])
    call_duration_end.append(call_duration_begin[i] + call_duration[i])
    spend_in_system.append(call_duration[i] + waiting_time[i])

    if current_time < arrival_time[i]:
        idle_time.append(arrival_time[i] - current_time)
    else:
        idle_time.append(0)

    if waiting_time[i] != 0:
        wait_count += 1

    current_time = call_duration_end[i]

probability_wait = float(wait_count) / float(total_callers)
print("Probability Wait = %.2f" % probability_wait)

if int(probability_wait) == 0:
    print('The proposal to add another telephone to the booth, is not justified!')
