#'/home/lucky/base_weight/r18_culane_baseweight.csv'
import csv

import csv
with open('/home/lucky/changed_weight/base_weight/r101_culane_baseweight.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 跳过第一行列名
    with open('new_file.csv', 'w', newline='') as g:
        writer = csv.writer(g)
# 写入表头
        writer.writerow(['name', 'tensor1', 'tensor2', 'tensor3'])
        for row in reader:
            if row:
                name = row[0]
                tensors = row[1:]
# 将tensors中的tensor值转换为float类型，如果值不存在则设置为1.0
                tensors = [float(tensor.split('(')[1].split(',')[0]) if tensor else 1.0 for tensor in tensors]
# 写入新的一行数据
                writer.writerow([name] + tensors)