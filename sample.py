import json
import os, sys
import random 
import datetime  
with open('./templates.py', 'r') as fr:
    content = fr.readlines()
content_str = "".join(content)
data = eval(content_str)
random_keys = random.sample(data.keys(), 3)
date = datetime.datetime.now().strftime('%Y%m%d')
with open('template_practice_'+date, 'w') as fw:
    print(list(random_keys), file=fw)
    for k in random_keys:
        print(k, file=fw)
        print("Input: ", data[k]["input"], file=fw)
        print("Output: ", data[k]["output"], file=fw)
        print("\n", file=fw)