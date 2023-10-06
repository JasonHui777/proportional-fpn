import pandas as pd
import os
#/home/lucky/data_calculate/changed_weight/change_2/r18_culane_change_normalweight.csv
#/home/lucky/CLRNet-main/data/CULane/list/test.txt
import csv

# 读取csv文件
with open('/home/lucky/data_calculate/changed_weight/change_2/r18_culane_change_normalweight.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_list = list(csv_reader)

# 处理第二个txt文件
with open('/home/lucky/CLRNet-main/data/CULane/list/val.txt') as f:
    txt_list = f.readlines()

for i in range(len(txt_list)):
    txt_list[i] = './data/CULane' + txt_list[i].strip() # 在每行前面加上路径

i = 0
# 遍历csv_list，找到txt_list中存在的行并将三个参数赋值为1
for row in csv_list:
    if row['name'] in txt_list:
        i += 1
        row['weight_1'] = 1.0
        row['weight_2'] = 1.0
        row['weight_3'] = 1.0

for row in csv_list:
    if row['name'] in txt_list:
        print(row['weight_1'], '', row['weight_2'], '', row['weight_3'])
print(i)
# 写回csv文件
with open('/home/lucky/data_calculate/changed_weight/change_2/r18_culane_change_normalweight.csv', mode='w', newline='') as csv_file:
    fieldnames = ['name', 'weight_1', 'weight_2', 'weight_3']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv_list:
        writer.writerow(row)