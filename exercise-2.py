import random


def calculate_customer(x):
    if 1 <= x <= 35:
        return 8
    elif 36 <= x <= 65:
        return 10
    elif 66 <= x <= 90:
        return 12
    else:
        return 14


def calculate_order(x):
    if 1 <= x <= 4:
        return 1
    elif 5 <= x <= 7:
        return 2
    elif 8 <= x <= 9:
        return 3
    else:
        return 4


bagels = int(input('Enter the number of Bagels you want to baked per Day :'))
making_cost = float(bagels * 5.8)
day = 5
excess_demand = 0

all_order = []
profit = []

for i in range(day):
    number_of_customer = calculate_customer(random.randint(0, 99))
    order = []
    for j in range(number_of_customer):
        order.append(calculate_order(random.randint(0, 9)))

    all_order.append(order)
    total_order = sum(order)

    if bagels >= total_order:
        revenue_from_sell = total_order * 8.4
        revenue_from_grocery = (bagels - total_order) * 4.2
        profit.append(revenue_from_sell - making_cost + revenue_from_grocery)
    else:
        excess_demand = (total_order - bagels) * 8.4
        revenue_from_sell = bagels * 8.4
        profit.append(float(revenue_from_sell - making_cost - excess_demand))
        print('Day %d has excess demand!' % (i + 1))
        excess_demand += 1

print('Total Profit = %.2f' % float(sum(profit)))
if excess_demand:
    print('%d bagels should not be baked per day...!' % bagels)
# print(all_order)
