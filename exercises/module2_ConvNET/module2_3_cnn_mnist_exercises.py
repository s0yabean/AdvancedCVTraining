# Advanced Computer Vision Training
# Module 2 Convnet
# MNIST CNN exercise

import keras


from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D, Flatten, Dense

# Step 2: Build the CNN Model

model = Sequential()
model.add(Conv2D(32,(3,3),input_shape=(28,28,1),
                 activation='relu',padding = 'same'))

model.add(MaxPool2D((2,2,)))
model.add(Conv2D(64,(3,3), activation='relu',padding = 'same'))
model.add(MaxPool2D((2,2,)))
model.add(Conv2D(128,(3,3), activation='relu',padding = 'same'))
model.add(MaxPool2D((2,2,)))
model.add(Conv2D(256,(3,3), activation='relu',padding = 'same'))
model.add(MaxPool2D((2,2,)))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(10,activation='softmax'))

# print(model.summary())

# Step 3: Compile the Model

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Step 4: Train the Model

history = model.fit(X_train,y_train,batch_size=100,
	epochs=3,validation_data=(X_test,y_test))


# Step 5: Evalute the Model
# loss,accuracy = model.evaluate(X_test,y_test)
# print("Accuracy: %.2f%%" % (accuracy*100))



import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')

plt.legend()

plt.show()

# Step 6: Save the Model
model.save('mnist_cnn_2.h5')

