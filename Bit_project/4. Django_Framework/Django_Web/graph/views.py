from django.shortcuts import render
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')
import pandas as pd

from django.shortcuts import render

from time import mktime, strptime

# Create your views here.
# class ResultAPIView(APIView):
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# @csrf_exempt
def Realtimegraph(request):
    df = pd.read_csv("D:\Pycharm_pro\Django_Web\media\inputData\inputData.txt")

    def graph(df):
        source = sourcedata(df)
        namelist = nlist(source)
        data = datax(source, namelist)
        data.plot(kind='bar', figsize=(10, 5))
        plt.legend(data.columns)
        plt.savefig("D:\\PyCharm_pro\\Django_Web\\static\\graph\\timeGraph\\month.png")
        plt.clf()

    def sourcedata(df):
        dfg = df['InputTime']
        gg = df.drop(['InputTime'], axis=True)
        king = []
        for i in dfg:
            i = i[0:7]
            king.append(i)
        king = pd.DataFrame(king)
        result = pd.concat([king, gg], axis=1)
        result = result.rename(columns={0: 'InputTime'})
        return result

    def nlist(result):
        data = result["Name"].tolist()
        data1 = set(data)
        data2 = list(data1)
        return data2

    def datax(source, namelist):
        forx = source.groupby(['Name', 'InputTime'])
        listdata = sourcefordata(forx, namelist)
        frame = pd.concat(listdata, axis=1).fillna(0)
        return frame

    def sourcefordata(forx, namelist):
        buckly = []
        for i in namelist:
            ddata = forx.size()[i]
            ddata1 = pd.DataFrame(ddata).reset_index()
            ddata2 = ddata1.rename(columns={0: i})
            ddata3 = ddata2.set_index("InputTime")
            buckly.append(ddata3)
        return buckly

    def daysource(df):
        dfg = df['InputTime']
        gg = df.drop(['InputTime'], axis=True)
        king = []
        for i in dfg:
            i = i[0:10]
            king.append(i)
        king = pd.DataFrame(king)
        result = pd.concat([king, gg], axis=1)
        result = result.rename(columns={0: 'InputTime'})
        return result

    def daygraph(df):
        source = daysource(df)
        namelist = nlist(source)
        data = datax(source, namelist)
        data.plot(kind='bar', figsize=(30, 5))
        plt.legend(data.columns)
        plt.savefig("D:\\PyCharm_pro\\Django_Web\\static\\graph\\timeGraph\\day.png")
        plt.clf()

    def yearsource(df):
        dfg = df['InputTime']
        gg = df.drop(['InputTime'], axis=True)
        king = []
        for i in dfg:
            i = i[0:4]
            king.append(i)
        king = pd.DataFrame(king)
        result = pd.concat([king, gg], axis=1)
        result = result.rename(columns={0: 'InputTime'})
        return result

    def yeargraph(df):
        source = yearsource(df)
        namelist = nlist(source)
        data = datax(source, namelist)
        data.plot(kind='bar', figsize=(10, 5))

        plt.legend(data.columns)
        plt.savefig("D:\\PyCharm_pro\\Django_Web\\static\\graph\\timeGraph\\year.png")
        plt.clf()

    def pielist(df):
        ry = df["Name"]
        r1 = ry.tolist()
        r2 = set(r1)
        r3 = list(r2)
        return r3

    def piegraph(df):
        rc = df.drop(['InputTime'], axis='columns')
        nlist = pielist(df)
        rr = rc.groupby(['Name'])
        ra = rr.size()
        fo = []
        foo = []
        for i in nlist:
            a = i
            b = ra[i]
            foo.append(a)
            fo.append(b)
        plt.pie(fo, labels=foo, autopct='%0.1f%%')
        plt.savefig("D:\\PyCharm_pro\\Django_Web\\static\\graph\\pieGraph\\pie.png")
        plt.clf()

    def SData(SNData):
        Sdata = SNData[['Name', 'InputTime']]
        return Sdata

    def namelist(result):
        ForName = result["Name"].tolist()
        ForN = set(ForName)
        FN = list(ForN)
        return FN

    def SpeciesData(df):
        SpeTimeData = df['InputTime']
        OutOfTimeData = df.drop(['InputTime'], axis=True)
        TimeList = []
        for i in SpeTimeData:
            i = i[0:7]
            TimeList.append(i)
        TimeList = pd.DataFrame(TimeList)
        Nresult = pd.concat([TimeList, OutOfTimeData], axis=1)
        Nresult = Nresult.rename(columns={0: 'InputTime'})
        return Nresult

    def speciesGraph(df):
        SNData = SpeciesData(df)
        SD = SData(SNData)
        SList = namelist(SD)
        sd1 = SD.groupby(['Name', 'InputTime']).size()
        for ng in SList:
            sd1[ng].plot(kind='bar', color='black', title=ng, figsize=(10, 5))
            plt.savefig("D:\\PyCharm_pro\\Django_Web\\static\\graph\\nameGraph\\{}".format(ng))
            plt.clf()

    piegraph(df)

    daygraph(df)

    graph(df)

    yeargraph(df)

    speciesGraph(df)

    # year = "D:\\Pycharm_pro\\djangoProject3\\static\\graph\\year.png"
    # month = "D:\\Pycharm_pro\\djangoProject3\\static\\graph\\month.png"
    # day = "D:\\Pycharm_pro\\djangoProject3\\static\\graph\\day.png"

    return render(request, 'Real-time graph.html', { 'email': request.session.get('user') })