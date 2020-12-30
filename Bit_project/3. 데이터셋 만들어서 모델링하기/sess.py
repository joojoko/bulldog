import glob
from PIL import Image
import numpy as np
import os
import shutil
import keras
from keras.preprocessing import image
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from tensorflow.python.keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


import keras.backend as k
import tensorflow as tf
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from keras.wrappers.scikit_learn import KerasClassifier

np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
X_train, X_test, y_train, y_test = np.load("D:\\work\\koko\\kgkg.npy")

print(X_train.shape)
print(X_train.shape[0])

kookoodass= []
for i in os.listdir("D:\\Mush"):

  kookoodass.append(i)

categories = kookoodass
nb_classes = len(categories)

X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255

print(len(X_train))
print(len(y_train))

#__________________________________________
model = Sequential()
model.add(Conv2D(32, (3, 3), padding="same", input_shape=X_train.shape[1:], activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model_dir = './model'

if not os.path.exists(model_dir):
    os.mkdir(model_dir)

model_path = model_dir + '/multi_img_classification.model'
checkpoint = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)
early_stopping = EarlyStopping(monitor='val_loss', patience=6)

model.summary()

history = model.fit(X_train, y_train, batch_size=1, epochs=50,
                    validation_data=(X_test, y_test), callbacks=[checkpoint, early_stopping])

# # from keras.models import model_from_json
# #
# # model_json = model.to_json()
# # with open("CNN_model.json", "w") as json_file:
# #     json_file.write(model_json)
# #
# # model.save_weights("CNN_model.h5")
# # print("Saved model to disk")


print("정확도: %.4f" % (model.evaluate(X_test, y_test)[1]))

#
# y_vloss = history.history['val_loss']
# y_loss = history.history['loss']
#
# x_len = np.arange(len(y_loss))
#
# plt.plot(x_len, y_vloss, marker='.', c='red', label='val_set_loss')
# plt.plot(x_len, y_loss, marker='.', c='blue', label='train_set_oss')
# plt.legend()
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.grid()
# plt.show()
