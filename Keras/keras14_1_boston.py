# [실습]
# 1. train 0.7 이상
# 2. R2 : 0.8 이상 / RMSE 사용

from sklearn.datasets import load_boston
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np

#1. 데이터
dataset = load_boston()
x = dataset.data
y = dataset.target
print(x)
print(x.shape) #506, 13
print(y)
print(y.shape) #506, 
print(dataset.feature_names)
#['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO'   
#  'B' 'LSTAT']
print(dataset.DESCR)
x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True, random_state=14)

#2.  모델 구성

model = Sequential()
model.add(Dense(131, input_dim=13))
model.add(Dense(261))
model.add(Dense(3915))
model.add(Dense(1))

#3. 컴파일 , 훈련
model.compile(loss='mse', optimizer='adam', 
              metrics=['mae', 'acc'])
model.fit(x_train, y_train, epochs=2162, batch_size=69)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss :', loss)

y_predict = model.predict(x_test)

from sklearn.metrics import mean_squared_error, r2_score
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE :", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 :", r2)

# R2 : 0.6305459654973594