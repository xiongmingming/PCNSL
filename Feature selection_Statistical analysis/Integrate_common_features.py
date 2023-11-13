import pandas as pd


outputpath = 'E:/feature_output/'
utest_path = 'E:/feature_output/第一批_U升序p值前5%_original.csv'
pearson_path = 'E:/feature_output/第一批_皮尔逊升序p值前5%_original.csv'
utest = pd.read_csv(utest_path)
pearson = pd.read_csv(pearson_path)
output = pd.concat([utest,pearson], axis = 0, join = "inner")###此处axis应为1###
print(output)
output.to_csv(outputpath + '第一批统计学特征整合_utest+pearson_original.csv')
