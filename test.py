from datetime import datetime
from meteostat import Point, Daily
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression

# Set time period
start = datetime(2018, 1, 1)
end = datetime.today()

# Create Point for waterloo, ON
location = Point(43.4643, -80.5204, 329)

# Get daily data from 2018 
data = Daily(location, start, end)
data = data.fetch()

# import data into numpy
# tavg, tmix, tmax: column names 
train_data = np.array(data[['tavg', 'tmin', 'tmax']].values)

# to see data frame dimensions
# print(train_data.shape)

# Define sequence length in days
n = 14
train_data_seq = []
# chunk 14 days at a time 
for i in range(len(train_data) - n + 1):
    train_data_seq.append(train_data[i:i+n])
    
train_data_seq = np.array(train_data_seq)
# print(train_data_seq.shape)
# (1962, 14, 3)
# with 3 being the number of features in each chunk
# and each chunk length 14 each 

