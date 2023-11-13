import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

FilePath = 'E:/feature_output/第一批_combat4类.csv'
file = pd.read_csv(FilePath)

data = file.iloc[:,3:1221]
#print(data)
batch = file.loc[:, ['batch']]
feature_name = data.iloc[1:0, 0:1218]
#print(feature_name)


list_feature = []

for i in feature_name:
    data_i = data.loc[:, i]
    testdata = pd.concat([batch,data_i],axis = 1)
    #print(testdata)

    model = ols(str(i)+'~batch', data = testdata).fit()
    table = anova_lm(model)
    table_PR = table.at['batch','PR(>F)']
    print(table)
    print(table_PR)
    ###如果Pr(>F)值小于0.05，那么就可以认为因素对结果有显著影响。###
    if table_PR<0.05:
        print(i)
        list_feature.append(i)    
    else:
        pass  
print(list_feature)

output = data.drop(list_feature, axis=1)
print(output.shape)
print(output)
outputpath = 'E:/feature_output/'
output.to_csv(outputpath + '第一批_anova.csv')

