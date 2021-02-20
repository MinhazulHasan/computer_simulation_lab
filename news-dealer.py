import random


def calculate_demand(x, y):
    # GOOD
    if 1 <= x <= 35:
        if 1 <= y <= 3:
            return 40
        elif 4 <= y <= 8:
            return 50
        elif 9 <= y <= 23:
            return 60
        elif 24 <= y <= 43:
            return 70
        elif 44 <= y <= 78:
            return 80
        elif 79 <= y <= 93:
            return 90
        else:
            return 100
    # FAIR
    elif 36 <= x <= 80:
        if 1 <= y <= 10:
            return 40
        elif 11 <= y <= 28:
            return 50
        elif 29 <= y <= 68:
            return 60
        elif 69 <= y <= 88:
            return 70
        elif 89 <= y <= 96:
            return 80
        else:
            return 90
    # POOR
    else:
        if 1 <= y <= 44:
            return 40
        elif 45 <= y <= 66:
            return 50
        elif 67 <= y <= 82:
            return 60
        elif 83 <= y <= 94:
            return 70
        else:
            return 80


total_day = 20

# random_digit_for_newsday = [58, 17, 21, 45, 43, 36, 27, 73, 86, 19, 93, 45, 47, 30, 12, 41, 65, 57, 18, 98]
# random_digit_for_demand = [93, 63, 31, 19, 91, 75, 84, 37, 23, 2, 53, 96, 33, 86, 16, 7, 64, 94, 55, 13]
random_digit_for_newsday = []
random_digit_for_demand = []

demand = []
revenue_from_sales = []
lost_profit_excess_demand = []
sale_of_scalp = []
profit_list = []

for i in range(total_day):
    random_digit_for_newsday.append(random.randint(0, 99))
    random_digit_for_demand.append(random.randint(0, 99))

    demand.append(calculate_demand(random_digit_for_newsday[i], random_digit_for_demand[i]))

    if demand[i] > 70:
        extra = demand[i] - 70
        revenue_from_sales.append(float(70 * 0.5))
        lost_profit_excess_demand.append(float(extra * 0.17))
        sale_of_scalp.append(0)

    elif demand[i] < 70:
        extra = 70 - demand[i]
        revenue_from_sales.append(float(demand[i] * 0.5))
        lost_profit_excess_demand.append(0)
        sale_of_scalp.append(float(extra * 0.05))

    else:
        revenue_from_sales.append(float(70 * 0.5))
        lost_profit_excess_demand.append(0)
        sale_of_scalp.append(0)

    profit = revenue_from_sales[i] - (70 * 0.33) - lost_profit_excess_demand[i] + sale_of_scalp[i]
    profit_list.append(profit)

print('Total Profit = %.2f' % sum(profit_list))

