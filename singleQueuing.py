import random


def arrival(x):
    if 0 < x < 126:
        return 1
    elif 125 < x < 251:
        return 2
    elif 250 < x < 376:
        return 3
    elif 375 < x < 501:
        return 4
    elif 500 < x < 626:
        return 5
    elif 625 < x < 751:
        return 6
    elif 750 < x < 876:
        return 7
    elif 876 < x < 1001:
        return 8
    else:
        return -1


def service(x):
    if 0 < x < 11:
        return 1
    elif 10 < x < 31:
        return 2
    elif 30 < x < 61:
        return 3
    elif 60 < x < 86:
        return 4
    elif 85 < x < 96:
        return 5
    elif 95 < x < 101:
        return 6
    else:
        return -1


total_customer = 100
current_time = 0
wait_count = 0

arrival_time = []
service_time = []

service_time_begin = []
service_time_end = []

waiting_time = []
idle_time = []
spend_in_system = []

for i in range(0, total_customer):
    if i == 0:
        arrival_time.append(0)
    else:
        interArrivalTime = arrival(random.randint(0, 1000))
        arrival_time.append(interArrivalTime + arrival_time[i - 1])

    service_time.append(service(random.randint(0, 100)))

    service_time_begin.append(max(current_time, arrival_time[i]))
    waiting_time.append(service_time_begin[i] - arrival_time[i])
    service_time_end.append(service_time_begin[i] + service_time[i])
    spend_in_system.append(service_time[i] + waiting_time[i])

    if current_time < arrival_time[i]:
        idle_time.append(arrival_time[i] - current_time)
    else:
        idle_time.append(0)

    if waiting_time[i] != 0:
        wait_count += 1

    current_time = service_time_end[i]

average_waiting_time = float(sum(waiting_time)) / float(total_customer)
probability_wait = float(wait_count) / float(total_customer)
average_service_time = float(sum(service_time)) / float(total_customer)
probability_of_idle_server = float(sum(idle_time)) / float(service_time_end[total_customer - 1])

print("Average Waiting Time = %.2f \n Probability Wait = %.2f \n Average Service Time = %.2f \n Probability of Idle "
      "Server = %.2f" % (average_waiting_time, probability_wait, average_service_time, probability_of_idle_server))
