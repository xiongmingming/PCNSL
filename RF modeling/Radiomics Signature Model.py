import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier



#设置训练集和验证集
train_path = 'E:/feature_output/第一批统计学特征整合_utest+pearson.csv'
valida_path = 'E:/feature_output/第二批_combat3类.csv'
train_data = pd.read_csv(train_path)
valida_data = pd.read_csv(valida_path)
list_feature = ['wavelet_LLH_glcm_MaximumProbability', 'wavelet_LLH_firstorder_Variance', 'log_sigma_1_0_mm_3D_firstorder_Skewness', 'wavelet_LLH_firstorder_InterquartileRange', 'log_sigma_3_0_mm_3D_glcm_Idm', 'wavelet_LLH_glcm_Imc2', 'wavelet_LLH_gldm_DependenceNonUniformityNormalized', 'wavelet_LLH_firstorder_Skewness']

###统计出频率最高的特征###
#Y是因变量，X是自变量
X_train = train_data.loc[:, list_feature]
Y_train = train_data.loc[:, ['diagnose']]
X_test = valida_data.loc[:, list_feature]
Y_test = valida_data.loc[:, ['diagnose']]




#算5个决策树模型拟合的准确度
from sklearn.ensemble import RandomForestClassifier
###为训练集计算AUC###
model = RandomForestClassifier(n_estimators=5, random_state=281522)
model.fit(X_train, Y_train)
y_pred = model.predict(X_train)
y_proba = model.predict_proba(X_train)[:, 1]
print(y_pred)
print(y_proba)    
y_pred1 = model.predict(X_test)
y_proba1 = model.predict_proba(X_test)[:, 1]
print(y_pred1)
print(y_proba1) 
    
#混淆矩阵以及分类报告
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_train, y_pred)
print('混淆矩阵\n\n',cm)
print('\n真阳性(TP) = ', cm[0,0])
print('\n真阴性(TN) = ', cm[1,1])
print('\n假阳性(FP) = ', cm[0,1])
print('\n假阴性(FN) = ', cm[1,0])

#sns.heatmap(cm,annot= True, fmt='d', cmap='rocket')
#plt.show()

#混淆矩阵以及分类报告
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred1)
print('混淆矩阵\n\n',cm)
print('\n真阳性(TP) = ', cm[0,0])
print('\n真阴性(TN) = ', cm[1,1])
print('\n假阳性(FP) = ', cm[0,1])
print('\n假阴性(FN) = ', cm[1,0])


 
from sklearn.metrics import classification_report
print(classification_report(Y_train, y_pred))
print(classification_report(Y_test, y_pred1)) 
#看下ROC曲线和AUC值
from sklearn.metrics import roc_auc_score
train_ROC_AUC = roc_auc_score(Y_train, y_proba)
print('ROC AUC : {:.4f}'.format(train_ROC_AUC))
#看下ROC曲线和AUC值
from sklearn.metrics import roc_auc_score
valida_ROC_AUC = roc_auc_score(Y_test, y_proba1)
print('ROC AUC : {:.4f}'.format(valida_ROC_AUC))

