import random
import math
import numpy as np


def calculate_demand(x):
    table = {(1, 10): 0, (11, 35): 1, (36, 70): 2, (71, 91): 3, (92, 100): 4}

    for key in table:
        if key[0] <= x <= key[1]:
            return table[key]


def calculate_leadTime(x):
    table = {(1, 6): 1, (7, 9): 2, (10, 10): 3}

    for key in table:
        if key[0] <= x <= key[1]:
            return table[key]


def main(m, n):
    # assigning value
    numberOfCycle = 5
    iteration = n * numberOfCycle
    startDaysStore = 3
    startDaysArrival = 2 - 1

    # generate random Number
    random_number_for_demand = [random.randint(0, 100) for _ in range(n*numberOfCycle)]
    random_number_for_leadTime = [random.randint(1, 10) for _ in range(numberOfCycle)]

    # declaration variable
    cycle = [0] * iteration
    days = [i for i in range(1, iteration + 1)]
    beginningInventory = [0] * iteration
    demand = [0] * iteration
    endingInventory = [0] * iteration
    shortageQuantity = [0] * iteration
    order_quantity = ["-"] * iteration
    randomNumberForLeadTime = ["-"] * iteration
    daysUntilArrival = ["-"] * iteration

    beginningInventory[0] = startDaysStore
    daysUntilArrival[0] = startDaysArrival

    previousOrderQuantity = 8
    previousShortage = 0
    cnt = 0

    # start iteration
    for i in range(0, iteration):
        cycle[i] = math.ceil(float(days[i]) / n)

        if i != 0:
            if daysUntilArrival[i - 1] == 0:
                beginningInventory[i] = endingInventory[i - 1] + previousOrderQuantity
                previousOrderQuantity = 0
            else:
                beginningInventory[i] = endingInventory[i - 1]

        demand[i] = calculate_demand(random_number_for_demand[i])
        dem_tot = demand[i] + previousShortage
        endingInventory[i] = max(0, beginningInventory[i] - dem_tot)

        if beginningInventory[i] - dem_tot < 0:
            shortageQuantity[i] += (dem_tot - beginningInventory[i])
            previousShortage = shortageQuantity[i]
        else:
            previousShortage = 0

        if i % n == n - 1:
            order_quantity[i] = (11 - endingInventory[i]) + previousShortage
            previousOrderQuantity = order_quantity[i]
            randomNumberForLeadTime[i] = random_number_for_leadTime[cnt]
            cnt += 1
            daysUntilArrival[i] = calculate_leadTime(randomNumberForLeadTime[i])
        else:
            if i != 0 and type(daysUntilArrival[i - 1]) == int:
                if daysUntilArrival[i - 1] != 0:
                    daysUntilArrival[i] = daysUntilArrival[i - 1] - 1

    arr = np.column_stack((cycle, days, beginningInventory, random_number_for_demand, demand, endingInventory,
                           shortageQuantity, order_quantity, randomNumberForLeadTime, daysUntilArrival))
    print(arr)

    np.savetxt("MN Inventory.csv", arr, delimiter=',',
               header='Cycle,Days,BeginningInventory,Random Number For Demand,Demand,Ending Inventory,'
                      'Shortage Quantity,Order Quantity,Random Number For LeadTime,Days Until Arrival',
               fmt='%s')


if __name__ == '__main__':
    main(11, 5)
