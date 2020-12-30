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

kookoodass= []
for i in os.listdir("D:\\Mush"):

  kookoodass.append(i)

caltech_dir = "D:\\Mush"
catgories = kookoodass
nb_classes = len(catgories)

image_w = 64
image_h = 64


pixel = image_h * image_w * 3

generator = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

X =[]
y =[]

for idx, gin in enumerate(catgories):

    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "\\" + gin
    files = glob.glob(image_dir + "\\*.jpg")

    print(files[0])
    im_dir = 'D:\\Copdata\\'
    os.mkdir(im_dir + gin)

    for m in files:
        i = 0
        m = Image.open(m)
        m = img_to_array(m)
        m = m.reshape((1,) + m.shape)
        for batch in generator.flow(m, batch_size=1,
                                    save_to_dir=(im_dir + gin), save_format='jpg'):
            i += 1
            if i > 3:
                break


    files = glob.glob(im_dir + gin + "\\*.jpg")

    print(gin, "파일 길이:", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)


        X.append(data)
        y.append(label)

        if i % 700 == 0:
            print(gin, " : ", f)

X = np.array(X)
y = np.array(y)

print(y[0])

X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)

np.save("D:\\MDataset\\kgkg", xy)

print("ok", len(y))


#
#
# import keras.backend as k
# import tensorflow as tf
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from keras.wrappers.scikit_learn import KerasClassifier
#
# np_load_old = np.load
# np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
# X_train, X_test, y_train, y_test = np.load("D:\\work\\koko\\kgkg.npy")
#
# print(X_train.shape)
# print(X_train.shape[0])
#
# categories = ['Ginkgo', 'SagoPalm']
# nb_classes = len(categories)
#
# X_train = X_train.astype(float) / 255
# X_test = X_test.astype(float) / 255
#
# model = Sequential()
# model.add(Conv2D(32, (3, 3), padding="same", input_shape=X_train.shape[1:], activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
#
# model.add(Conv2D(64, (3, 3), padding="same", activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
#
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(nb_classes, activation='softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# model_dir = './model'
#
# if not os.path.exists(model_dir):
#     os.mkdir(model_dir)
#
# model_path = model_dir + '/multi_img_classification.model'
# checkpoint = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)
# early_stopping = EarlyStopping(monitor='val_loss', patience=6)
#
# model.summary()
#
# history = model.fit(X_train, y_train, batch_size=16, epochs=50,
#                     validation_data=(X_test, y_test), callbacks=[checkpoint, early_stopping])
#
# # from keras.models import model_from_json
# #
# # model_json = model.to_json()
# # with open("CNN_model.json", "w") as json_file:
# #     json_file.write(model_json)
# #
# # model.save_weights("CNN_model.h5")
# # print("Saved model to disk")
#
#
# print("정확도: %.4f" % (model.evaluate(X_test, y_test)[1]))
#
# from PIL import Image
# import os, glob, numpy as np
# from keras.models import load_model
#
# test_dir = "D:\\work\\testdata"
#
# img_w = 64
# img_h = 64
#
# pixels = img_h * img_w * 3
#
# X = []
# filenames = []
# files = glob.glob(test_dir + "/*.*")
# for o, f in enumerate(files):
#     img = Image.open(f)
#     img = img.convert("RGB")
#     img = img.resize((img_w, img_h))
#     data = np.asarray(img)
#     filenames.append(f)
#     X.append(data)
#
# print(o)
# print(f)
# X = np.array(X)
#
# model = load_model('./model/multi_img_classification.model')
#
# prediction = model.predict(X)
# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
# cnt = 0
#
# # from tensorflow.compat.v2.keras.models import model_from_json
# #
# # json_file = open("CNN_model.json", "r")
# # loaded_model_json = json_file.read()
# # json_file.close()
# # # json파일로부터 model 로드하기
# # loaded_model = model_from_json(loaded_model_json)
# # # 로드한 model에 weight 로드하기
# # loaded_model.load_weights("CNN_model.h5")
# # print("Loaded model from disk")
# #
# # model = loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# for i in prediction:
#     pre_ans = i.argmax()  # 예측 레이블
#     print(i)
#     print(pre_ans)
#     pre_ans_str = ''
#     print(pre_ans)
#
#     if pre_ans == 0:
#         pre_ans_str = "소철"
#     elif pre_ans == 1:
#         pre_ans_str = "은행"
#
#     if i[0] >= 0.8:
#         print("해당 " + filenames[cnt].split("\\")[1] + "이미지는 " + pre_ans_str + "로 추정됩니다.")
#     if i[1] >= 0.8:
#         print("해당 " + filenames[cnt].split("\\")[1] + "이미지는 " + pre_ans_str + "으로 추정됩니다.")
#
#     cnt += 1
#
#

