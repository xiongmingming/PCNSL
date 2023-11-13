import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')


###读取测试集x和y###
train_path = 'E:/feature_output/第一批统计学特征整合_utest+pearson.csv'
train_file = pd.read_csv(train_path)
x_train = train_file.iloc[: , 3:40]
y_train = train_file.loc[: , ['diagnose']]
feature_name = x_train.T.index



###未统计出频率最高的特征###
#Step2 定义LASSO模型    
#提取五个特征
LR = LinearRegression()
LR.fit(x_train,y_train)
coef = np.split(LR.coef_, 37, axis=1)
#lasso筛选的特征
coef = pd.Series(coef, index = x_train.columns)
paixv = coef.sort_values()
#print(paixv)
lasso_feature = paixv[coef > 0]
#print(lasso_feature)
indices = lasso_feature[::-1][:5]
print(indices)
list_feature = indices.index.values.tolist()
print(type(list_feature))
