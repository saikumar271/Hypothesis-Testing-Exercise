# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 02:45:46 2023
Hypothesis Testing Exercise
"""

"1)Minitab File : Cutlets.mtw"
import pandas as pd
from scipy import stats
# Load the data
data = pd.read_csv('F:\cutlets.csv')  # Replace with the actual file path
data
# Extract data for each unit
unit1 = data['Unit1']
unit2 = data['Unit2']
# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(unit1, unit2)
# Set the significance level (alpha)
alpha = 0.05
# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# Make a decision based on the p-value
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in cutlet diameter between the two units.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in cutlet diameter between the two units.")



"2)Minitab File: LabTAT.mtw"

import pandas as pd
from scipy import stats
# Load the data
data = pd.read_csv(r'F:\LabTAT.csv')
data
# Group the data by laboratory
grouped_data= [group[1]['TAT'] for group in data.groupby("Laboratory")]
grouped_data
# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(*grouped_data)
# Define the significance level (alpha)
alpha = 0.05
# Report the findings
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in average TAT among the laboratories.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in average TAT among the laboratories.")



"3)Buyer Ratio.mtw"

import pandas as pd
from scipy.stats import chi2_contingency
# Load the data from the CSV file
data = pd.read_csv(r"F:\BuyerRatio.csv")#correct file path data
data
# Assuming that the CSV file has columns named 'Region', 'Gender', and 'Count'
# Adjust column names accordingly
observed = pd.crosstab(data["Region"], data["Gender"])
observed
# Perform the chi-squared test
chi2, p, dof, expected = chi2_contingency(observed)
# Set your chosen alpha level (significance level)
alpha = 0.05
# Print the results
print("Chi-squared statistic:", chi2)
print("Degrees of freedom:", dof)
print("P-value:", p)
if p < alpha:
    print("Reject the null hypothesis (H0): Not all proportions are equal.")
else:
    print("Fail to reject the null hypothesis (H0): All proportions are equal.")



"4)Minitab File: CustomerOrderForm.mtw"

import pandas as pd
from scipy.stats import chi2_contingency
# Load the Minitab file into a DataFrame
data = pd.read_csv("F:\CustomerOrderForm.csv")  # Replace with the actual file path if it's a CSV file
# Display the loaded data to understand its structure
print(data.head())
# Assuming the data has columns like 'Center' and 'Defective'
# Adjust column names accordingly
observed = pd.crosstab(data['Center'], data['Defective'])
# Perform the chi-squared test for independence
chi2, p, dof, expected = chi2_contingency(observed)
# Set significance level (alpha)
alpha = 0.05
# Print the results
print("Chi-squared statistic:", chi2)
print("Degrees of freedom:", dof)
print("P-value:", p)
# Make a decision based on the p-value
if p < alpha:
    print("Reject the null hypothesis: The defective percentage varies by center.")
else:
    print("Fail to reject the null hypothesis: The defective percentage does not vary by center.")

























