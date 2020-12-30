from PIL import Image
import os, glob, numpy as np
from keras.models import load_model

test_dir = "D:\\work\\testdata"

img_w = 64
img_h = 64

pixels = img_h * img_w * 3

X = []
filenames = []
files = glob.glob(test_dir + "/*.*")
for o, f in enumerate(files):
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((img_w, img_h))
    data = np.asarray(img)
    filenames.append(f)
    X.append(data)

print(o)
print(f)
X = np.array(X)

model = load_model('./model/multi_img_classification.model')

prediction = model.predict(X)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
cnt = 0

for i in prediction:
    pre_ans = i.argmax()  # 예측 레이블
    print(i)
    print(pre_ans)
    pre_ans_str = ''
    print(pre_ans)

    if pre_ans == 0:
        pre_ans_str = "은행"
    elif pre_ans == 1:
        pre_ans_str = "소철"

    if i[0] >= 0.8:
        print("해당 " + filenames[cnt].split("\\")[1] + "이미지는 " + pre_ans_str + "로 추정됩니다.")
    if i[1] >= 0.8:
        print("해당 " + filenames[cnt].split("\\")[1] + "이미지는 " + pre_ans_str + "으로 추정됩니다.")

    cnt += 1
