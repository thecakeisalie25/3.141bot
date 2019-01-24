import numpy as np
import keras

np.random.seed(7)

dataset = np.loadtxt("test.txt", delimiter=",")

X = dataset[:, 0]
Y = dataset[:, 1]

print(X)
print(Y)

model = keras.Sequential()
model.add(keras.layers.Dense(4, input_dim=1, activation='relu'))
model.add(keras.layers.Dense(1, activation='relu'))

model.compile(loss='mse', optimizer='adam', metrics=['mse'])

model.fit(X, Y, epochs=150, batch_size=10)