import csv

with open('/media/lucky/4124B1EA0575413A/data_calculate/changed_weight/change_2/r18_culane_change_normalweight.csv', 'r') as f:
    reader = csv.reader(f)
    num_rows = len(list(reader))

print(f'The CSV file has {num_rows} rows.')

#home/lucky/r18_culane_baseweight.csv 1333350
#tran 1333200

#'/home/lucky/r34_culane_baseweight.csv' 1333352
#tran 1333201