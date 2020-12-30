from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
import os, glob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from keras.models import load_model
from static import imform
import time
import json
from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
img_w = 64
img_h = 64
model = load_model('./static/model/multi_img_classification.model')

from Imageanalysis.models import mage2
def Imageanalysis(req):
    context = {

    }
    return render(req, 'Imageanalysis.html', context={ 'email': req.session.get('user') })

def Imageanalysis_detail(request):
    global inputImage
    if(request.method == 'POST'):
        post = mage2()
        # post.title = request.POST['title']
        # post.text = request.POST['text']
        latit = request.POST['pro']
        print(latit)

        long = request.POST['por']
        print(long)
        # print(post.text)
        X = []

        for img in request.FILES.getlist('imgs'):
            inputImage = Image.open(img)
            img = inputImage.convert("RGB")
            img = img.resize((img_w, img_h))
            data = np.asarray(img)
            X.append(data)
        X = np.array(X)
        prediction = model.predict(X)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        cnt = 0

        for i in prediction:
            pre_ans = i.argmax()  # 예측 레이블
            print(i)
            print(pre_ans)
            pre_ans_str = ''
            print(pre_ans)
            B = ''
            C = ''
            A = ''
            title = ''

            if pre_ans == 0:
                pre_ans_str = "CorprinusComatus"
                B = "/static/mush_img/Corprinus.jpg"
                C = imform.corp
                A = imform.C
                title = imform.CTitle
            elif pre_ans == 2:
                pre_ans_str = "Morel"
                B = "/static/mush_img/Morel.jpg"
                C = imform.more
                A = imform.M
                title = imform.MTitle
            elif pre_ans == 1:
                pre_ans_str = "LingzhiMushroom"
                B = "/static/mush_img/LingzhiMushroom.jpg"
                C = imform.ling
                A = imform.L
                title = imform.LTitle
            elif pre_ans == 3:
                pre_ans_str = "OysterMushroom"
                B = "/static/mush_img/OysterMushroom.jpg"
                C = imform.oys
                A = imform.O
                title = imform.OTitle
            elif pre_ans == 4:
                pre_ans_str = "PineMushroom"
                B = "/static/mush_img/PineMushroom.jpg"
                C = imform.pine
                A = imform.P
                title = imform.PTitle
            elif pre_ans == 5:
                pre_ans_str = "Polyozellus"
                B = "/static/mush_img/Polyozellus.jpg"
                C = imform.poly
                A = imform.PL
                title = imform.PTitlee
            elif pre_ans == 6:
                pre_ans_str = "SarcodonAspratus"
                B = "/static/mush_img/SarcodonAspratus.jpg"
                C = imform.sar
                A = imform.S
                title = imform.Stitle
            elif pre_ans == 7:
                pre_ans_str = "TrenellaFuciformis"
                B = "/static/mush_img/TrenellaFuciformis.jpg"
                C = imform.tren
                A = imform.T
                title = imform.TTitle
            # savingImg(inputImage, pre_ans_str)
            # savingData(pre_ans_str)
            savingLocation(pre_ans_str, long, latit)



            return render(request, "Imageanalysis_detail.html",context= {'mush':pre_ans_str,
                                                              'ti':title, 'imim': B, 'txt':C, 'A': A, 'email': request.session.get('user') })

def savingImg(inputImage, pre_ans_str):

    timesource = time.localtime()
    now = "%04d-%02d-%02d %02d_%02d_%02d" % (timesource.tm_year, timesource.tm_mon, timesource.tm_mday, timesource.tm_hour, timesource.tm_min, timesource.tm_sec)
    inputdir = "./media/inputImages/{}".format(pre_ans_str)
    if not os.path.exists(inputdir):
        os.mkdir(inputdir)
    os.chdir(inputdir)

    inputImage.save("{} {}.jpg".format(pre_ans_str, now))
    os.chdir("D:\Pycharm_pro\Django_Web")

def savingData(pre_ans_str):

    timesource = time.localtime()
    now = "%04d-%02d-%02d %02d_%02d_%02d" % (timesource.tm_year, timesource.tm_mon, timesource.tm_mday, timesource.tm_hour, timesource.tm_min, timesource.tm_sec)
    inputFile = open('D:\Pycharm_pro\Django_Web\media\inputData\inputData.txt', 'a')
    inputFile.write("{0},{1},{2}".format(now,pre_ans_str,1) + '\n')
    inputFile.close()

# def makeJson(pre_ans_str):

def savingLocation(pre_ans_str, long, latit):
    times = time.localtime()
    nowtime = "%04d-%02d-%02d %02d_%02d_%02d" % (times.tm_year, times.tm_mon, times.tm_mday, times.tm_hour, times.tm_min, times.tm_sec)
    locationDir = "D:\Pycharm_pro\Django_Web\static\location"
    os.chdir(locationDir)

    fi_path = "{}\location.json".format(locationDir)
    j_data = {}
    with open(fi_path, "r") as j_file:
        j_data = json.load(j_file)

    j_data['positions'].append({
        "name":pre_ans_str,
        "longitude":long,
        "latitude":latit,
        "time":nowtime
    })

    with open(fi_path, 'w') as out_fi:
        json.dump(j_data, out_fi, ensure_ascii=False, indent="\t")



