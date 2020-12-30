from django.test import TestCase

# Create your tests here.
import json

with open("D:\Pycharm_pro\Django_Web\media\location\location.json","r") as f:
    json_data = json.load(f)
print(json.dumps(json_data))