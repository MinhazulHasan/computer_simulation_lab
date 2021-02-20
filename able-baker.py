import random


def arrival(x):
    if 0 < x < 26:
        return 1
    elif 25 < x < 66:
        return 2
    elif 65 < x < 86:
        return 3
    elif 85 < x < 101:
        return 4
    else:
        return -1


def able_service(x):
    if 0 < x < 31:
        return 2
    elif 30 < x < 59:
        return 3
    elif 58 < x < 84:
        return 4
    elif 83 < x < 101:
        return 5
    else:
        return -1


def baker_service(x):
    if 0 < x < 36:
        return 3
    elif 35 < x < 61:
        return 4
    elif 60 < x < 81:
        return 5
    elif 80 < x < 101:
        return 6
    else:
        return -1


total_customer = 100

arrival_time = []
service_time = []

able_available = 0
baker_available = 0
wait_count = []

service_time_begins = []
service_time_end = []

waiting_time = []
idle_time = []
spend_in_system = []


def calculation(current_available, i, service_func):
    service_time.append(service_func(random.randint(0, 100)))

    service_time_begins.append(max(current_available, arrival_time[i]))
    waiting_time.append(service_time_begins[i] - arrival_time[i])
    service_time_end.append(service_time_begins[i] + service_time[i])
    spend_in_system.append(service_time[i] + waiting_time[i])

    if able_available < arrival_time[i]:
        idle_time.append(arrival_time[i] - current_available)
    else:
        idle_time.append(0)

    if waiting_time[i] != 0:
        wait_count.append(1)


for i in range(0, total_customer):
    if i == 0:
        arrival_time.append(0)
    else:
        arrivalTime = arrival(random.randint(1, 100))
        arrival_time.append(arrival_time[i - 1] + arrivalTime)

    if arrival_time[i] >= able_available:
        calculation(able_available, i, able_service)
        able_available = service_time_end[i]

    elif arrival_time[i] >= baker_available:
        calculation(baker_available, i, baker_service)
        baker_available = service_time_end[i]

    else:
        if able_available <= baker_available:
            calculation(able_available, i, able_service)
            able_available = service_time_end[i]
        else:
            calculation(baker_available, i, baker_service)
            baker_available = service_time_end[i]


average_waiting_time = float(sum(waiting_time)) / float(total_customer)
probability_wait = float(sum(wait_count)) / float(total_customer)
average_service_time = float(sum(service_time)) / float(total_customer)
probability_of_idle_server = float(sum(idle_time)) / float(service_time_end[total_customer - 1])

print("Average Waiting Time = %.2f \n Probability Wait = %.2f \n Average Service Time = %.2f \n Probability of Idle "
      "Server = %.2f" % (average_waiting_time, probability_wait, average_service_time, probability_of_idle_server))
