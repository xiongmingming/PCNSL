#------------------------------------------使用广义线性模型进行临床指标显著性检验--------------------------------------#
library(glm2)
train_clinical = read.csv("E:/feature_output/训练集_radscore_临床特征筛选.csv",header = TRUE,fileEncoding = 'GBK')
######平均值为mean，中位数为median###
train_clinical$ IELSG.score[is.na(train_clinical$IELSG.score)] <- median(train_clinical $ IELSG.score,na.rm=T)
train_clinical$ LDH.level[is.na(train_clinical$LDH.level)] <- median(train_clinical $ LDH.level,na.rm=T)
####
logit.fit <- glm2(diagnose1~batch+negative+IELSG.score+MSKCC.score+deep.lesions+gender+age+ONLY.MTX+multiple.lesions+ECOG.score+ALL.CYCLE
                  ,family=gaussian(link = "identity"),data=data.frame(train_clinical),control=list(maxit=30))
summary(logit.fit)

valida_clinical = read.csv("E:/feature_output/验证集_radscore_临床特征筛选.csv",header = TRUE,fileEncoding = 'GBK')
######平均值为mean，中位数为median###
valida_clinical$ IELSG.score[is.na(valida_clinical$IELSG.score)] <- median(valida_clinical $ IELSG.score,na.rm=T)
valida_clinical$ LDH.level[is.na(valida_clinical$LDH.level)] <- median(valida_clinical $ LDH.level,na.rm=T)
####
logit.fit <- glm2(diagnose1~batch+negative+IELSG.score+MSKCC.score+deep.lesions+gender+age+ONLY.MTX+multiple.lesions+ECOG.score+ALL.CYCLE
                  ,family=gaussian(link = "identity"),data=data.frame(valida_clinical),control=list(maxit=30))
summary(logit.fit)

#------------------------------------------使用岭回归进行临床评分AUC计算--------------------------------------#
setwd("E:/python to R")
#文件读取
train_data = read.csv("E:/feature_output/训练集_概率储存_test.csv",header = TRUE,fileEncoding = 'GBK')
valida_data = read.csv("E:/feature_output/验证集_概率储存_test.csv",header = TRUE,fileEncoding = 'GBK')
prob_train<-data.frame(lable=train_data[,1],IELSG=train_data[,4],MSKCC=train_data[,7],radscore=train_data[,10],
                       IELSG1=train_data[,13],MSKCC1=train_data[,16],clinical=train_data[,19])
prob_valida<-data.frame(lable=valida_data[,1],IELSG=valida_data[,4],MSKCC=valida_data[,7],radscore=valida_data[,10],
                        IELSG1=valida_data[,13],MSKCC1=valida_data[,16],clinical=valida_data[,19])



library(glmnet)
#创建设计矩阵和响应变量：将数据转化为设计矩阵X和响应变量y的形式
data_matrix <- model.matrix(diagnose ~ IELSG.score, data = train_data)
y <- train_data$diagnose
#执行岭回归：使用alpha = 0来指定您想进行L2正则化
cv_fit <- cv.glmnet(data_matrix, y, alpha = 0)
#这里使用了交叉验证函数cv.glmnet来选择最佳的λ值
#查看选择的λ值：
best_lambda <- cv_fit$lambda.min
print(best_lambda)
#预测新数据：
new_data_matrix <- model.matrix(diagnose ~ IELSG.score, data = valida_data)
predictions <- predict(cv_fit, newx = new_data_matrix, s = best_lambda, type = "response")
# 计算AUC
actual <- valida_data$diagnose
# 将预测值转换为数值向量
predictions <- as.numeric(predictions)
# 计算AUC
auc <- auc(roc(actual, predictions))
print(auc)

#预测旧数据：
predictions1 <- predict(cv_fit, newx = data_matrix, s = best_lambda, type = "response")
# 计算AUC
actual1 <- train_data$diagnose
# 将预测值转换为数值向量
predictions1 <- as.numeric(predictions1)
# 计算AUC
auc1 <- auc(roc(actual1, predictions1))
print(auc1)



#创建设计矩阵和响应变量：将数据转化为设计矩阵X和响应变量y的形式
data_matrix <- model.matrix(diagnose ~ MSKCC.score, data = train_data)
y <- train_data$diagnose
#执行岭回归：使用alpha = 0来指定您想进行L2正则化
cv_fit <- cv.glmnet(data_matrix, y, alpha = 0)
#这里使用了交叉验证函数cv.glmnet来选择最佳的λ值
#查看选择的λ值：
best_lambda <- cv_fit$lambda.min
print(best_lambda)
#预测新数据：
new_data_matrix <- model.matrix(diagnose ~ MSKCC.score, data = valida_data)
predictions <- predict(cv_fit, newx = new_data_matrix, s = best_lambda, type = "response")
# 计算AUC
actual <- valida_data$diagnose
# 将预测值转换为数值向量
predictions <- as.numeric(predictions)
# 计算AUC
auc <- auc(roc(actual, predictions))
print(auc)

#预测旧数据：
predictions1 <- predict(cv_fit, newx = data_matrix, s = best_lambda, type = "response")
# 计算AUC
actual1 <- train_data$diagnose
# 将预测值转换为数值向量
predictions1 <- as.numeric(predictions1)
# 计算AUC
auc1 <- auc(roc(actual1, predictions1))
print(auc1)





#------------------------------------------使用岭回归进行临床评分AUC计算后的概率储存--------------------------------------#
new_data <- data.frame(IELSG.score = valida_data$IELSG.score, diagnose = valida_data$diagnose)
# 预测每一个值的概率
probabilities <- rep(NA, nrow(new_data))
for(i in 1:nrow(new_data)){
  data_matrix_i <- model.matrix(diagnose ~ IELSG.score, data = new_data[i, ])
  probabilities[i] <- predict(cv_fit, newx = data_matrix_i, s = best_lambda, type = "response")
}

# 将预测概率存储到新的数据框中
new_data$probabilities <- probabilities
# 将结果存储到csv文件
write.csv(new_data, file = "E:/feature_output/predictions.csv", row.names = FALSE)

new_data <- data.frame(MSKCC.score = valida_data$MSKCC.score, diagnose = valida_data$diagnose)
# 预测每一个值的概率
probabilities <- rep(NA, nrow(new_data))
for(i in 1:nrow(new_data)){
  data_matrix_i <- model.matrix(diagnose ~ MSKCC.score, data = new_data[i, ])
  probabilities[i] <- predict(cv_fit, newx = data_matrix_i, s = best_lambda, type = "response")
}

# 将预测概率存储到新的数据框中
new_data$probabilities <- probabilities
# 将结果存储到csv文件
write.csv(new_data, file = "E:/feature_output/predictions1.csv", row.names = FALSE)
