import scipy.stats as stats
import pandas as pd

outputpath = 'E:/feature_output/'
train_path = 'E:/feature_output/第一批_anova_negative_original.csv'
valida_path = 'E:/feature_output/第一批_anova_positive_original.csv'
train_data = pd.read_csv(train_path)
valida_data = pd.read_csv(valida_path)
feature_name = train_data.iloc[1:0, 3:103]
print(feature_name)
train_feature = train_data.iloc[:,3:103]
#print(train_feature)
valida_feature = valida_data.iloc[:,3:103]
#print(valida_feature)
output = []
list_pvalue = []
list_feature = []
for i in feature_name:
    #print(i)
    train = train_feature.loc[0:,i]
    valida = valida_feature.loc[0:,i]
    #print(train)
    u, p=stats.mannwhitneyu(train,valida,alternative='two-sided')
    pvalue = pd.Series(p, index = [i])
    list_pvalue.append(pvalue)
    list_feature.append(i)

    # ###筛选p值，p值大于0.05不相关，p值越大越不相关###
    # print(p)
    # if p < 0.05:
    #     pvalue = pd.Series(p, index = [i])
    #     print(pvalue)
    #     output.append(pvalue)
    # else:
    #     pass

    # pvalue = pd.Series(p, index = [i])
    # if pvalue < 0.05:
    #     output.append(pvalue)


#print(output)
print(list_pvalue)
pvalue_data = pd.concat(list_pvalue, axis=0)
print(pvalue_data)
paixv = pvalue_data.sort_values()
print(paixv)
indices = paixv[::1][:60]
print(indices)
index = indices.index
#print(type(index))
train_data1 = train_data.loc[:, index]
print(train_data1)
valida_data1 = valida_data.loc[:, index]
print(valida_data1)
train_data1.to_csv(outputpath + '第一批_negetive_original_U升序p值前5%.csv')
valida_data1.to_csv(outputpath + '第一批_positive_original_U升序p值前5%.csv')