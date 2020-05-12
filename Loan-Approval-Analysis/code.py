# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)

#Code starts here
bank = pd.DataFrame(bank_data)

categorical_var = bank.select_dtypes(include = 'object')
numerical_var = bank.select_dtypes(include = 'number')
print(categorical_var.shape)
print(numerical_var.shape)

banks = bank.drop(['Loan_ID'], axis = 1)
banks.isnull().sum()

bank_mode = banks.mode()

banks.fillna(bank_mode.iloc[0], inplace = True)
print(banks.shape)
print(banks.isnull().sum().values.sum())

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc = 'mean')
print(avg_loan_amount['LoanAmount'][1].round(2))

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

percentage_se = round((len(loan_approved_se) / len(banks) * 100), 2)
percentage_nse = round((len(loan_approved_nse) / len(banks) * 100), 2)
print(percentage_se)
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x / 12)
big_loan_term = list(loan_term.apply(lambda x: x >= 25)).count(True)
print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(round(mean_values.iloc[1,0], 2))


