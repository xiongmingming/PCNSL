import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import ExtraTreesClassifier

###读取测试集x和y###
train_path = 'E:/feature_output/第一批统计学特征整合_utest+pearson.csv'
train_file = pd.read_csv(train_path)
x_train = train_file.iloc[: , 3:40]
y_train = train_file.loc[: , ['diagnose']]
feature_name = x_train.T.index


###未统计出频率最高的特征###
#Step2 定义RF模型
#使用极端随机树模型进行拟合的过程
feat_labels = x_train.columns
#clf = ExtraTreeClassifier(random_state=a)
clf = ExtraTreesClassifier(n_estimators=3,  random_state=4334)
clf.fit(x_train, y_train)
importance = clf.feature_importances_

#np.argsort()返回待排序集合从下到大的索引值，[::-1]实现倒序，即最终indices内保存的是从大到小的索引值
indices = np.argsort(importance)[::-1][:5]

#按重要性从高到低输出属性列名和其重要性
list_feature = []
for f in range(len(indices)):
    output = feat_labels[indices[f]]
    # print(("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importance[indices[f]])))
    list_feature.append(output)
print(list_feature)





