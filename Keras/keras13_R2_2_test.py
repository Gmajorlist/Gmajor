#실습
#1. R2를 음수가 아닌 0.5 이하로 줄이기
#2. 데이터는 건들지 말것
#3. 레이어는 인풋 아웃풋 모함 7개 이상
#4. batch_size=1
#5. 히든레이어의 노드는 각각 10개 이상 100개 이하
#6. train 70%
#7. epoch 100번 이상fro
#8. loss지표는 mse 또는 mae

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

#1. 데이터
x = np.array(range(1,21))
y = np.array(range(1,21))

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True 
    )

#2. 모델구성
model = Sequential()
model.add(Dense(10, input_dim=1))
model.add(Dense(20))
model.add(Dense(10))
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(95))
model.add(Dense(95))
model.add(Dense(95))
model.add(Dense(95))
model.add(Dense(95))
model.add(Dense(100))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', 
              metrics=['mae', 'acc'])
model.fit(x_train, y_train, epochs=111, batch_size=1)

#4. 평가, 예측 
loss = model.evaluate(x_test, y_test) #훈련에 관여하지않음-evaluate
print('loss :', loss)
y_predict = model.predict(x_test)


from sklearn.metrics import mean_squared_error, r2_score
def RMSE(Y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE :", RMSE(y_test, y_predict))


r2 = r2_score(y_test, y_predict)
print("R2 :", r2)

