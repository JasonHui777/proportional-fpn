import pandas as pd
import numpy as np

# 读入原始CSV文件
df = pd.read_csv('/home/lucky/changed_weight/change_1/r34_culane_change_iouloss.csv')


# 带有可调参数a的的权重计算公式
# alpha = 0.5
# weight_1 = np.exp(-alpha * df['tensor1'])
# weight_2 = np.exp(-alpha * df['tensor2'])
# weight_3 = np.exp(-alpha * df['tensor3'])

# 计算新的权重
total_loss = df['tensor1'] + df['tensor2'] + df['tensor3']
weight_1 = np.exp(-df['tensor1'] / total_loss)
weight_2 = np.exp(-df['tensor2'] / total_loss)
weight_3 = np.exp(-df['tensor3'] / total_loss)

# 计算权重总和
# weight_sum = weight_1 + weight_2 + weight_3
#
# # 归一化处理
# weight_1_normalized = weight_1 / weight_sum
# weight_2_normalized = weight_2 / weight_sum
# weight_3_normalized = weight_3 / weight_sum

# 创建新的DataFrame对象，包括name、weight_1_normalized、weight_2_normalized和weight_3_normalized列
new_df = pd.DataFrame({'name': df['name'], 'weight_1': weight_1, 'weight_2': weight_2, 'weight_3': weight_3})

# 将新的DataFrame对象保存到CSV文件中
new_df.round({'weight_1': 4, 'weight_2': 4, 'weight_3': 4}).to_csv('new.csv', index=False)

#/home/lucky/changed_weight/change_1/r18_culane_change_iouloss.csv