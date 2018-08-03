import string
import random
import numpy as np
import pandas as pd
from faker import Faker

fake = Faker('en_US')
num_records = 5000
str_month = '01_2018'
num_files = 5

category_selection = ['digital', 'grocery', 'beauty', 'automotive', 'sports', 'jewelry', 'baby', 'books']
gender_selection = ['male', 'female', 'unknown']
total_price_selection = np.arange(39, 800)
age_selection = [' - 17' ,'18 - 35', '36 - 50' , '51 - 65' , '65 - ']
time_selection = ['morning', 'afternoon', 'evening', 'night']
state_selection = ['California',
'Texas',
'New York',
'Florida',
'Illinois',
'Pennsylvania',
'Ohio',
'Georgia',
'Michigan',
'North Carolina',
'New Jersey',
'Virginia',
'Washington',
'Massachusetts',
'Arizona',
'Indiana',
'Tennessee',
'Missouri',
'Maryland',
'Wisconsin',
'Minnesota',
'Colorado',
'Alabama',
'South Carolina',
'Louisiana',
'Kentucky',
'Oregon',
'Oklahoma',
'Connecticut',
'Iowa',
'Mississippi',
'Arkansas',
'Utah',
'Kansas',
'Nevada',
'New Mexico',
'Nebraska',
'West Virginia',
'Idaho',
'Hawaii',
'Maine',
'New Hampshire',
'Rhode Island',
'Montana',
'Delaware',
'South Dakota',
'Alaska',
'North Dakota',
'Vermont',
'Wyoming']

p_state =[0.121256008,
0.083662702,
0.062161766,
0.061850921,
0.040749636,
0.040406946,
0.036601558,
0.031607895,
0.031302497,
0.031152046,
0.028150988,
0.026129869,
0.024097311,
0.021171191,
0.020961783,
0.020785519,
0.020548514,
0.019119328,
0.018754423,
0.018165736,
0.01714611,
0.016665253,
0.015290354,
0.015104092,
0.014631598,
0.013903493,
0.012431846,
0.012180376,
0.011375362,
0.009775812,
0.009461987,
0.009361288,
0.009176233,
0.009154359,
0.008825946,
0.00659632,
0.005910615,
0.005865659,
0.005099617,
0.004441398,
0.004201774,
0.004186454,
0.00332621,
0.003211238,
0.002928391,
0.002672572,
0.002325419,
0.002288285,
0.001982198,
0.001843103]


def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits + 'abcdef'):
    return ''.join(random.choice(chars) for _ in range(size))


def random_csv_generator():
    category = np.random.choice(category_selection, num_records, p=[0.1, 0.15, 0.15, 0.05, 0.15, 0.1, 0.15, 0.15])
    total_price = np.random.choice(total_price_selection, num_records)
    gender = np.random.choice(gender_selection, num_records, p=[0.47, 0.47, 0.06])
    age = np.random.choice(age_selection, num_records, p[0.1, 0.4, 0.3, 0.15, 0.05])
    time = np.random.choice(time_selection, num_records, p=[0.25, 0.25, 0.35, 0.15])
    state = np.random.choice(state_selection,num_records, p_state)
    month = np.repeat(str_month, num_records)
    df = pd.DataFrame (data{'category': category, 'total_price': total_price, 'gender': gender, 'age': age, 'time': time, 'state': state, 'month': month})
    df.to_csv(random_string_generator() + '_sales_csv.csv', sep='\t', encoding='utf-8', compression='gzip')


def main():
    random_csv_generator()


if __name__ == '__main__':
    main()
