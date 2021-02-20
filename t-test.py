import numpy as np
from statsmodels.stats.weightstats import ttest_ind


ger_sales = [5255, 6677, 5320, 2747, 4863, 723, 1115, 974, 5, 1495, 1653, 2050, 2034, 4927, 5708, 6008, 5388, 5264,
             2619, 3384, 3008, 1062, 2279, 2512, 3032, 2750, 3719, 4638, 4558, 3977, 483, 1873, 2220, 2180, 2946, 1706,
             1866, 2635, 2544, 4991, 4604, 5291, 4579, 2183, 2251, 2375, 3372, 2842, 2075, 2508, 2583, 2877, 5455, 5787,
             5845, 5396, 2636, 2470, 2755, 3443, 3661, 2302, 2541, 2548, 2906]

fr_sales = [0, 168, 123, 317, 130, 203, 277, 276, 416, 89, 188, 703, 109, 215, 1537, 2032, 1674, 1558, 2030, 1838, 1810,
            2418, 124, 1463, 1297, 1169, 1511]


def compare_2_groups(arr_1, arr_2, alpha):
    t_value, p_value, dof = ttest_ind(arr_1, arr_2)
    print(t_value)
    print('T Value=%.3f, P Value=%.3f' % (t_value, p_value))
    if p_value > alpha:
        print('Same distributions (fail to reject Ho)')
    else:
        print('Different distributions (reject Ho)')


sample_size = 15
ger_sampled = np.random.choice(ger_sales, sample_size)
fr_sampled = np.random.choice(fr_sales, sample_size)
compare_2_groups(ger_sampled, fr_sampled, 0.05)

# from scipy.stats import ttest_ind
#
# t_value, p_value = ttest_ind(drinks_before, drinks_after)
# print(t_value)
