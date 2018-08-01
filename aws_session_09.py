import string
import random
import numpy as np
import pandas as pd
from faker import Faker

def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits + 'abcdef'):
    return ''.join(random.choice(chars) for _ in range(size))


fake = Faker('en_US')
pq_batch = 5000
# Category, Total Price , Gender, Age, Time, State , Job

category_selection = ['digital', 'grocery', 'beauty', 'automotive', 'sports', 'jewelry', 'baby', 'books']
gender_selection = ['male', 'female', 'unknown']
total_price_selection = np.arange(39, 800)
age_selection = np.arange(18, 74)
time_selection = ['morning', 'afternoon', 'evening', 'night']

category = np.random.choice(category_selection, pq_batch, p=[0.1, 0.15, 0.15, 0.05, 0.15, 0.1, 0.15, 0.15])
total_price = np.random.choice(total_price_selection, pq_batch)
gender = np.random.choice(gender_selection, pq_batch, p=[0.47, 0.47, 0.06])
age = np.random.choice(age_selection, pq_batch)
time = np.random.choice(time_selection, pq_batch, p=[0.25, 0.25, 0.35, 0.15])

state = []
#job = []
month = np.repeat('Jan', pq_batch)

for _ in range(pq_batch):
    state.append(fake.state())

df = pd.DataFrame (data={'category': category, 'total_price': total_price, 
'gender': gender, 'age': age, 'time': time, 'state': state, 'month': month})

df.to_parquet(random_string_generator() + '_sales_pq.gzip', compression='gzip')
