import pandas as pd
import json

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,"sheet1")
    writer.save()

#jsonString = open("./nonPayment.json").read()
df = pd.read_data("./nonPayment.json")

print(df.count())

save(df, "nonPayment.xlsx")