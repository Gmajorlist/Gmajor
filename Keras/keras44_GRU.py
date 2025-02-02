
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , SimpleRNN, LSTM, GRU


#1.데이터
dataset = np.array([1,2,3,4,5,6,7,8,9,10])   #(10, )
# y = ???

x = np.array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9]])
# 3일치 데이터로 잘랐다.
y = np.array([4,5,6,7,8,9,10])

print(x.shape, y.shape)   #(7, 3) (7, )

x = x.reshape(7, 3, 1)    # [[1], [2], [3]]
                          # [[2], [3], [4]].....
print(x.shape)  #(7, 3, 1)         //  3,1  input shape가 된다


#모델구성
# SimpleRNN 잘 쓰지않음                    RNN 상당히 좋은 알고리즘이다         GRU는 많이 사용함
model = Sequential()
# model.add(SimpleRNN(10, input_shape=(3, 1)))
# model.add(LSTM(units=10, input_shape=(3, 1)))
              # 성능과 구조가 다름  / 속도가 느리다                
model.add(GRU(units=10, input_shape=(3, 1)))
                            
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

model.summary()



#SimpleRNN
# 10* (10 + 1 + 1 ) = 120
# units * ( feature + bias + units ) = prams 

#LSTM 
#4*(10* (10 + 1 + 1 ) = 120
 # 4 * units * ( feature + bias + units ) = prams 
 
 # GRU
 
#3 * units * ( feature + 2bias + units ) = prams 

