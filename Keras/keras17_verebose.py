from sklearn.datasets import load_boston
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

#1.데이터
datasets = load_boston()
x = datasets.data
y = datasets.target
# print(x.shape, y.shape) #(506, 13) (506,) 행무시 열 ! 열이중요! 
x_train, x_test, y_train, y_test = train_test_split(x, y ,
    shuffle= True, random_state=333, test_size=0.2)

#2.모델구성
model = Sequential()
model.add(Dense(5, input_dim=13)) # 행과 열
model.add(Dense(5, input_shape=(13, ))) #(13, )
model.add(Dense(4))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(1))


#3. 컴파일 훈련
import time as t
model.compile(loss='mse', optimizer='adam')
start = t.time()
model.fit(x_train, y_train, epochs=50, batch_size=1,
          validation_split=0.2, verbose=3)
end = t.time()


#4.평가 예측
loss = model.evaluate(x_test, y_test)
print('loss:', loss)

print("걸린시간:",  end - start)

