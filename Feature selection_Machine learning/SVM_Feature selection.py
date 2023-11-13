import pandas as pd
import numpy as np 
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
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


###未统计出频率最高的特征###
#Step2 定义线性SVC的迭代模型
list_feature = []
def SVC_RFE():
    svc = SVC(kernel = "linear", C=1, random_state = 4469)
    rfe = RFE(estimator=svc, n_features_to_select=5, step=1)
    rfe.fit(x_train, np.ravel(y_train))
    #print(rfe.n_features_ )  # 打印最优特征变量数
    #print(rfe.support_)  # 打印选择的最优特征变量
    X = rfe.support_
    Y = [i for i, x in enumerate(X) if x]
    

    #倒来倒去把最优特征变量提出来        
    for i in Y:
        A = feature_name[i]
        #print(A)
        #print(type(A))
        list_feature.append(A)
    print(list_feature)

SVC_RFE()





