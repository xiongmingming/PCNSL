import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneOut

#设置训练集和验证集
train_path = 'E:/feature_output/第一批统计学特征整合_utest+pearson.csv'
valida_path = 'E:/feature_output/第二批_combat3类.csv'
train_data = pd.read_csv(train_path)
valida_data = pd.read_csv(valida_path)

list_feature = ['wavelet_LLH_glcm_MaximumProbability', 'wavelet_LLH_firstorder_Variance', 'log_sigma_1_0_mm_3D_firstorder_Skewness', 'wavelet_LLH_firstorder_InterquartileRange', 'log_sigma_3_0_mm_3D_glcm_Idm', 'wavelet_LLH_glcm_Imc2', 'wavelet_LLH_gldm_DependenceNonUniformityNormalized', 'wavelet_LLH_firstorder_Skewness']
df = pd.DataFrame(columns=['negative', 'positive', 'patient'])
###统计出频率最高的特征###
#Y是因变量，X是自变量
X_train = train_data.loc[:, list_feature]
Y_train = train_data.loc[:, ['diagnose']]
X_test = valida_data.loc[:, list_feature]
Y_test = valida_data.loc[:, ['diagnose']]

# 使用留一交叉验证划分样本
loo = LeaveOneOut()
for train_index, test_index in loo.split(valida_data):#data为读取进来的csv文件数据
    x_test = pd.DataFrame(valida_data.iloc[test_index, 3:1221])
    x_test = x_test.loc[:, list_feature]
    print(x_test)
    y_test = pd.DataFrame(valida_data.iloc[test_index, 2:3])
    print(y_test)
    patient_name = pd.DataFrame(valida_data.iloc[test_index, 1221:1222])
    patient_name = patient_name.iloc[0,0]
    print(patient_name)

    #算5个决策树模型拟合的准确度
    from sklearn.ensemble import RandomForestClassifier
    ###为训练集计算AUC###
    model = RandomForestClassifier(n_estimators=5, random_state=281522)
    model.fit(X_train, Y_train)
    y_pred = model.predict(x_test)
    y_proba1 = model.predict_proba(x_test)[:, 0]
    y_proba2 = model.predict_proba(x_test)[:, 1]
    print(y_proba1)
    print(y_proba2)
    df.loc[len(df)] = [y_proba1, y_proba2, patient_name]
    print(df)
outputpath = 'E:/feature_output/'
df.to_csv(outputpath + '验证集_radscore_test.csv', index=False)

# 使用留一交叉验证划分样本
loo = LeaveOneOut()
for train_index, test_index in loo.split(train_data):#data为读取进来的csv文件数据
    x_test = pd.DataFrame(train_data.iloc[test_index, 3:40])
    x_test = x_test.loc[:, list_feature]
    print(x_test)
    y_test = pd.DataFrame(train_data.iloc[test_index, 2:3])
    print(y_test)
    patient_name = pd.DataFrame(train_data.iloc[test_index, 40:41])
    patient_name = patient_name.iloc[0,0]
    print(patient_name)

    #算5个决策树模型拟合的准确度
    from sklearn.ensemble import RandomForestClassifier
    ###为训练集计算AUC###
    model = RandomForestClassifier(n_estimators=5, random_state=281522)
    model.fit(X_train, Y_train)
    y_pred = model.predict(x_test)
    y_proba1 = model.predict_proba(x_test)[:, 0]
    y_proba2 = model.predict_proba(x_test)[:, 1]
    print(y_proba1)
    print(y_proba2)
    df.loc[len(df)] = [y_proba1, y_proba2, patient_name]
    print(df)
outputpath = 'E:/feature_output/'
df.to_csv(outputpath + '训练集_radscore_test.csv', index=False)
