import scipy.stats as stats
import pandas as pd

dataset = pd.read_csv('chi-data.csv')

categories = dataset.iloc[:4, 1:6]
chi_value, p_value, dof, exp = stats.chi2_contingency(categories)
print("Chi Square Value = %.2f \n Degree's of Freedom = %d \n P value = %.2f" % (chi_value, dof, p_value))

alpha = 0.05

if p_value <= alpha:
    print('Reject Ho,There is a relationship between 2 categorical variables')
else:
    print('Retain Ho,There is no relationship between 2 categorical variable')
