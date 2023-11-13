from neuroCombat import neuroCombat
import pandas as pd
import numpy as np


# Getting example data
# 200 rows (features) and 10 columns (scans)
datapath = pd.read_csv('E:/feature_output/第二批zscore.csv')
outputpath = 'E:/feature_output/'
data = datapath.iloc[:, 3:1221]
print(data)
dat = data.values.transpose()
print(dat.shape)




covars = datapath.iloc[:, 1:3]
print(covars)
# To specify names of the variables that are categorical:
categorical_cols = ['diagnose']
# To specify the name of the variable that encodes for the scanner/batch covariate:
batch_col = 'batch'
#print(batch_col)
#Harmonization step:
data_combat = neuroCombat(dat=dat,
    covars=covars,
    batch_col=batch_col,
    categorical_cols=categorical_cols)["data"]

result = pd.DataFrame(data_combat)
output = result.transpose()
print(output)

output.to_csv(outputpath + '第二批_combat3类.csv')