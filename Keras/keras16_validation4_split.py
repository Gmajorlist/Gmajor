import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
#1.데이터
x = np.array(range(1, 17))
y = np.array(range(1, 17))

x_train, x_test, y_train, y_test = train_test_split(x,
    y, test_size=0.2, random_state=12)
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)


#2.모델
model = Sequential()
model.add(Dense(5, input_dim=1))
model.add(Dense(3, activation='relu'))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=10, batch_size=1,
          validation_split=0.25)

#4. 평가 예측
loss = model.evaluate(x_test, y_test)
print('loss :', loss)

result = model.predict([17])
print("17의 예측값 :", result)

