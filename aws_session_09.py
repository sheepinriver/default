import sys
import random
import s3fs
import pyarrow as pa
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from pyarrow.filesystem import S3FSWrapper
from faker import Faker

fake = Faker('en_US')

# Category, Total Price , Gender, Age, Time, State , Job

category_selection = ['digital', 'grocery', 'beauty', 'automotive', 'sports', 'jewelry', 'baby', 'books']
gender_selection = ['male', 'female', 'unknown']
total_price_selection = np.arange(39, 800)
age_selection = np.arange(18, 74)
time_selection = ['morning', 'afternoon', 'evening', 'night']

category = np.random.choice(category_selection, 5000, p=[0.4, 1.0, 1.0, 0.1, 0.9, 0.4, 0.5, 0.3])
total_price = np.random.choice(total_price_selection, 5000)
gender = np.random.choice(gender_selection, 5000, p=[1.0, 1.0, 0.05])
age = np.random.choice(age_selection, 5000)
time = np.random.choice(time_selection, 5000, p=[0.7, 0.8, 1, 0.8])

state = []
#job = []

for _ in range(5000):
    state.append(fake.state())

df = pd.DataFrame (data{'category': category, 'total_price': total_price, 
'gender': gender, 'age': age, 'time': time, 'state': state})

df.to_parquet('df.parquet.gzip', compression='gzip')
