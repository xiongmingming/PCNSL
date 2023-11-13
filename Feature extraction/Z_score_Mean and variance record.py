import pandas as pd
####zscore方法三###
from sklearn.preprocessing import StandardScaler
from scipy import stats
import numpy as np
from sklearn import preprocessing
###第一批数据读取###
ori_data = pd.read_csv('E:/feature_output/第一批_feature.csv')
print(ori_data)
data = ori_data.iloc[:,3:1221]
print(data)

# ###第二批数据读取###
# ori_data1 = pd.read_csv('E:/feature_output/第二批_feature.csv')
# print(ori_data1)
# data1 = ori_data1.iloc[:,3:1221]
# print(data1)

# ###第二批使用第一批数据参数数据标准化###
# mean = np.mean(data, axis=0)
# print(mean)    
# std_dev = np.std(data, axis=0)
# print(std_dev)    
# final_data = (data1 - mean) / std_dev

# print(final_data)
# final_data.to_csv('E:/feature_output/第二批zscore使用第一批参数.csv')


# ###方法一 函数中具有均值和方差部分###
# ###可得均值和方差的zscore方法###
# scaler = StandardScaler()
# ###zscore###
# x_train = scaler.fit_transform(data)
# print(x_train)
# ###均值###
# mean = scaler.mean_
# print(mean)
# ###标准差，var_为方差###
# std_dev = np.sqrt(scaler.var_)
# print(std_dev)

# ###方法二直接得出zscore###
# ###一步求得zscore###
# data1 = preprocessing.scale(data, axis=0)
# df=pd.DataFrame(data1)
# print(df)

###方法三 独立得出各部分###
###得出zscore###
zscore = stats.zscore(data, axis=0)
print(zscore)
###得出均值###
mean = np.mean(data, axis=0)
print(mean)
###将均值加入结果###
mean2 = mean.to_frame()
table = pd.concat([zscore, mean2.T])
print(table)
###得出标准差###
std_dev = np.std(data, axis=0)
print(std_dev)
###将标准差加入结果###
std_dev2 = std_dev.to_frame()
final_data = pd.concat([table, std_dev2.T])
print(final_data)
final_data.to_csv('E:/feature_output/第一批zscore及参数.csv')