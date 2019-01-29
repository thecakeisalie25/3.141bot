import numpy as np
import keras

np.random.seed(70)

dataset = np.loadtxt("test.txt", delimiter=",")

print(dataset)

X = dataset[:, 0]
Y = dataset[:, 1]

print(X)
print(Y)

model = keras.Sequential()
model.add(keras.layers.Dense(4, input_dim=1, activation='linear'))
# model.add(keras.layers.Dense(6, activation='linear'))
model.add(keras.layers.Dense(1, activation='linear'))



model.compile(loss='mae', optimizer='adam', metrics=['mse'])

model.fit(X, Y, epochs=1, batch_size=1)
model.fit(X, Y, epochs=100, batch_size=10000)
model.fit(X, Y, epochs=10, batch_size=100000)
print(model.predict(
    x=[10e36,10e8,10]
))