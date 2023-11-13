import pandas as pd
from sklearn.linear_model import Lasso
import warnings
warnings.filterwarnings('ignore')



###读取测试集x和y###
train_path = 'E:/feature_output/第一批统计学特征整合_utest+pearson.csv'
train_file = pd.read_csv(train_path)
x_train = train_file.iloc[: , 3:40]
#print(x_train)
y_train = train_file.loc[: , ['diagnose']]
#print(y_train)
feature_name = x_train.T.index
#feature_name = x_train.iloc[1:0, 0:37]



###未统计出频率最高的特征###
#Step2 定义LASSO模型    
#提取五个特征
lasso = Lasso(alpha=0.00335982)
lasso.fit(x_train,y_train)
#lasso筛选的特征
coef = pd.Series(lasso.coef_, index = x_train.columns)
paixv = coef.sort_values()
#print(paixv)
lasso_feature = paixv[coef > 0]
#print(lasso_feature)
indices = lasso_feature[::-1][:5]
print(indices)
list_feature = indices.index.values.tolist()
print(list_feature)

