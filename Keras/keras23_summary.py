from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np


#데이터

x = np.array([1,2,3])
y = np.array([1,2,3])


#모델구성
model = Sequential()
model.add(Dense(5, input_dim=1))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(1))

model.summary() # 모델  가져왔을 때 쓰임
 




