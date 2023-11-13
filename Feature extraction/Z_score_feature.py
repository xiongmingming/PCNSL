import pandas as pd
# from sklearn.preprocessing import StandardScaler

import numpy as np
df_sum = pd.read_csv('E:/feature_output/第一批_feature.csv')
print(df_sum)
def z_score_normalize(data):    
    mean = np.mean(data, axis=0)    
    std_dev = np.std(data, axis=0)    
    normalized_data = (data - mean) / std_dev    
    return normalized_data
ori_data = df_sum.iloc[:,3:1221]
print(ori_data)
b=z_score_normalize(ori_data)
print(b)

b.to_csv('/data_raid5_21T/xiong/feature/Z_score_T1+C_MRI imgdata_part1.csv')