# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record = [[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)

census = np.concatenate((data, new_record), axis = 0)

age = census[:,0]

max_age = max(age)
min_age = min(age)
age_mean = round(age.mean(), 2)
age_std = round(np.std(age), 2)

race_0 = census[:,2][census[:,2]  == 0]
race_1 = census[:,2][census[:,2]  == 1]
race_2 = census[:,2][census[:,2]  == 2]
race_3 = census[:,2][census[:,2]  == 3]
race_4 = census[:,2][census[:,2]  == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

lnt = 0
minority_race = 0
for i in range(0, 5):
  if i == 0:
    lnt = len(census[:,2][census[:,2]  == i])
  else:
    if lnt > len(census[:,2][census[:,2]  == i]):
      minority_race = int(census[:,2][census[:,2]  == i][0])
      lnt = len(census[:,2][census[:,2]  == i])

senior_citizens = census[:, 0][census[:, 0] > 60]
working_hours_sum = sum(census[:, 6][census[:, 0] > 60])
senior_citizens_len = len(senior_citizens)
avg_working_hours = round(working_hours_sum / senior_citizens_len, 2)

high = census[:][census[:, 1] > 10]
low = census[:][census[:, 1] <= 10]

avg_pay_high = round(np.mean(high[:,7]), 2)
avg_pay_low = round(np.mean(low[:,7]), 2)
#Code starts here


