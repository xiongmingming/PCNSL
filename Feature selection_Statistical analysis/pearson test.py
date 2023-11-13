import pandas as pd
from scipy.stats import pearsonr

FilePath = 'E:/feature_output/第一批_anova_减9.csv'
file = pd.read_csv(FilePath)
outputpath = 'E:/feature_output/'

data = file.iloc[:,3:1212]
#print(data)
diagnose = file.loc[:, ['diagnose']]
#print(diagnose.shape)
print(diagnose)
#print(type(diagnose))
#feature_name = data.iloc[1:0, 0:1218]
feature_name = data.columns
#print(feature_name)


list_pearson = []
list_pvalue = []
for i in feature_name:
    data_i = data.loc[:, i]
    # dict_data_i = {str(i):data_i.values}
    # df_data_i = pd.DataFrame(dict_data_i)
    # print(df_data_i)
    # print(df_data_i.shape)
    # print(type(df_data_i))
    ###皮尔逊相关系数###
    # testdata = pd.concat([diagnose,data_i],axis = 1)
    # #print(testdata)
    # pre_pearson=testdata.corr(method='pearson')
    # pearson_num = pre_pearson.at['diagnose',str(i)]
    # #print(pearson_num)
    # pearson = pd.Series(pearson_num, index = [str(i)])
    # #print(pearson)
    # if pearson_num>0.3:
    #     print(i)
    #     list_pearson.append(pearson)    
    # else:
    #     pass

    ###皮尔逊相关系数为corr,P值为p###
    corr,p = pearsonr(diagnose.iloc[:, 0],data_i)
    #print(corr)
    #print(p)
    
    p_value = pd.Series(p, index = [str(i)])
    list_pvalue.append(p_value)
pvalue_data = pd.concat(list_pvalue, axis=0)
print(pvalue_data) 
paixv = pvalue_data.sort_values()
print(paixv)
indices = paixv[::1][:60]
print(indices)
index = indices.index
#print(type(index))
data1 = data.loc[:, index]
print(data1)
data1.to_csv(outputpath + '第一批_皮尔逊升序p值前5%_original.csv')
#df_data = pd.concat(list_pearson, axis=0)
#print(df_data)
# paixv = pearson.sort_values()
# print(paixv)
# pearson_feature = paixv[pearson > 0.85]
# print(pearson_feature)