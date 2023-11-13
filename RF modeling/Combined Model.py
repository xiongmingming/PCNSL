import numpy as np 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer


###数据读取###
train_data = pd.read_csv('E:/feature_output/训练集_数据整理_6模型.csv', encoding='GBK')
valida_data = pd.read_csv('E:/feature_output/验证集_数据整理_6模型.csv', encoding='GBK')
#print(valida_data)
# 创建简单填充器
imputer = SimpleImputer(strategy='mean')  # 填充策略可以根据需要选择'mean'、'median'或'most_frequent'
#patient_name = train_data.iloc[0:76,6:7]
#print(type(patient_name))
y_train = train_data.iloc[0:76,1:2]
y_valida = valida_data.iloc[0:29,1:2]
# 创建ColumnTransformer对象，指定要转换的列及转换方式
transformer = ColumnTransformer(transformers=[('imputer', imputer, ['number', 'diagnose', 'negative', 'positive', 'IELSG score_4', 'MSKCC_score', 'gender', 'age', 'LDH level', 'KPS score', 'ECOG score', 'deep lesions', 'multiple lesions', 'ONLY MTX', 'ALL CYCLE'])],
                                remainder='passthrough')
# 使用ColumnTransformer对象对训练集进行缺失值填充
data_filled = transformer.fit_transform(train_data)
# 将填充后的结果转换为DataFrame
train_data1 = pd.DataFrame(data_filled, columns=train_data.columns)

# 使用ColumnTransformer对象对训练集进行缺失值填充
data_filled = transformer.fit_transform(valida_data)
# 将填充后的结果转换为DataFrame
valida_data1 = pd.DataFrame(data_filled, columns=valida_data.columns)
# 打印处理后的DataFrame
print(valida_data1)



###为IELSG+radscore计算逻辑回归概率###
###划分数据集###
x_train_IELSG = train_data.iloc[0:76,2:5]
x_train_IELSG = imputer.fit_transform(x_train_IELSG)
x_valida_IELSG = valida_data.iloc[0:29,2:5]
x_valida_IELSG = imputer.fit_transform(x_valida_IELSG)
#算5个决策树模型拟合的准确度
# ###为训练集计算AUC###
model = RandomForestClassifier(n_estimators=5, random_state=34174, class_weight = 'balanced')
model.fit(x_train_IELSG, y_train)
###训练集概率和AUC###
pred_train_IELSG = model.predict(x_train_IELSG)
proba_train_IELSG_positive = model.predict_proba(x_train_IELSG)[:, 1]
#ROC-AUC
from sklearn.metrics import roc_auc_score
train_ROC_AUC = roc_auc_score(y_train, proba_train_IELSG_positive)
print(train_ROC_AUC)
###验证集概率和AUC###
pred_valida_IELSG = model.predict(x_valida_IELSG)
proba_valida_IELSG_positive = model.predict_proba(x_valida_IELSG)[:, 1]
#ROC曲线-AUC
from sklearn.metrics import roc_auc_score
valida_ROC_AUC = roc_auc_score(y_valida, proba_valida_IELSG_positive)
print(valida_ROC_AUC)




###为MSKCC+radscore计算逻辑回归概率###
###划分数据集###
x_train_MSKCC = train_data.iloc[0:76,np.r_[2:4,5:6]]
x_train_MSKCC = imputer.fit_transform(x_train_MSKCC)
x_valida_MSKCC = valida_data.iloc[0:29,np.r_[2:4,5:6]]
x_valida_MSKCC = imputer.fit_transform(x_valida_MSKCC)
#算5个决策树模型拟合的准确度
# ###为训练集计算AUC###
model = RandomForestClassifier(n_estimators=5, random_state=44392, class_weight = 'balanced')
model.fit(x_train_MSKCC, y_train)
###训练集概率和AUC###
pred_train_MSKCC = model.predict(x_train_MSKCC)
proba_train_MSKCC_positive = model.predict_proba(x_train_MSKCC)[:, 1]
#ROC-AUC
from sklearn.metrics import roc_auc_score
train_ROC_AUC = roc_auc_score(y_train, proba_train_MSKCC_positive)
print(train_ROC_AUC)
###验证集概率和AUC###
pred_valida_MSKCC = model.predict(x_valida_MSKCC)
proba_valida_MSKCC_positive = model.predict_proba(x_valida_MSKCC)[:, 1]
#ROC曲线-AUC
from sklearn.metrics import roc_auc_score
valida_ROC_AUC = roc_auc_score(y_valida, proba_valida_MSKCC_positive)
print(valida_ROC_AUC)