import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

dataset = np.array([1,2,3,4,5,6,7,8,9,10])
x = np.array([[1,2,3], [2,3,4], [3,4,5],
              [4,5,6], [5,6,7], [6,7,8],
              [7,8,9], [8,9,10],[9,10,11],
              [10,11,12],[20,30,40],
              [30,40,50],[40,50,60]])
y = np.array([4, 5, 6, 7, 8, 9, 10,11,12,13,50,60,70])

print( dataset.shape)
print( x.shape, y.shape)

x = x.reshape(13, 3, 1)


model = Sequential()              # ( N, 3 , 1)  아래 64가 1 로 올라옴
model.add(LSTM(units = 64, input_shape=(3, 1), activation='relu' ,
               return_sequences=True))  # return_sequences 디폴트는 false
model.add(LSTM(32))
model.add(Dense(64, activation = 'relu'))
model.add(Dense(32))
model.add(Dense(1))
model.summary() 

model.compile(loss='mse', optimizer= 'adam')
model.fit(x, y, epochs=512)


loss = model.evaluate(x, y)
print(loss)

y_predict = np.array([[50, 60, 70]]) #또는 .reshape(1, 3, 1)

result = model.predict(y_predict)

print('prediction result: ', result) 


