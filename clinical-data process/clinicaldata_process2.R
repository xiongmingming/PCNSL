setwd("E:/python to R")
library(Hmisc); library(grid); library(lattice);library(Formula); library(ggplot2) 
library(rms)
library(survival)
library(pROC)
library(glm2)
library(PredictABEL)
source('HLtest.r')
source('dca.r')
source('val.prob.ci.dec08.r')
source('accuracy.r')




#文件读取
train_data = read.csv("E:/feature_output/训练集_概率储存_test.csv",header = TRUE,fileEncoding = 'GBK')
valida_data = read.csv("E:/feature_output/验证集_概率储存_test.csv",header = TRUE,fileEncoding = 'GBK')
prob_train<-data.frame(lable=train_data[,1],IELSG=train_data[,23],MSKCC=train_data[,24],radscore=train_data[,10],
                       IELSG1=train_data[,13],MSKCC1=train_data[,16],clinical=train_data[,19])
prob_valida<-data.frame(lable=valida_data[,1],IELSG=valida_data[,23],MSKCC=valida_data[,24],radscore=valida_data[,10],
                       IELSG1=valida_data[,13],MSKCC1=valida_data[,16],clinical=valida_data[,19])

#------------------------------------------NRI & IDI--------------------------------------#
#训练集
IELSG.vs.radscore<-reclassification(data=prob_train,cOutcome = 1,predrisk1 = prob_train$IELSG,
                                        predrisk2 = prob_train$radscore,cutoff = c(0,0.5,1))
radscore.vs.IELSG1<-reclassification(data=prob_train,cOutcome = 1,predrisk1 = prob_train$radscore,
                                    predrisk2 = prob_train$IELSG1,cutoff = c(0,0.5,1))
MSKCC.vs.radscore<-reclassification(data=prob_train,cOutcome = 1,predrisk1 = prob_train$MSKCC,
                                    predrisk2 = prob_train$radscore,cutoff = c(0,0.5,1))
radscore.vs.MSKCC1<-reclassification(data=prob_train,cOutcome = 1,predrisk1 = prob_train$radscore,
                                    predrisk2 = prob_train$MSKCC1,cutoff = c(0,0.5,1))
IELSG1.vs.MSKCC1<-reclassification(data=prob_train,cOutcome = 1,predrisk1 = prob_train$IELSG1,
                                    predrisk2 = prob_train$MSKCC1,cutoff = c(0,0.5,1))
#验证集
IELSG.vs.radscore<-reclassification(data=prob_valida,cOutcome = 1,predrisk1 = prob_valida$IELSG,
                                    predrisk2 = prob_valida$radscore,cutoff = c(0,0.5,1))
radscore.vs.IELSG1<-reclassification(data=prob_valida,cOutcome = 1,predrisk1 = prob_valida$radscore,
                                     predrisk2 = prob_valida$IELSG1,cutoff = c(0,0.5,1))
MSKCC.vs.radscore<-reclassification(data=prob_valida,cOutcome = 1,predrisk1 = prob_valida$MSKCC,
                                    predrisk2 = prob_valida$radscore,cutoff = c(0,0.5,1))
radscore.vs.MSKCC1<-reclassification(data=prob_valida,cOutcome = 1,predrisk1 = prob_valida$radscore,
                                     predrisk2 = prob_valida$MSKCC1,cutoff = c(0,0.5,1))
IELSG1.vs.MSKCC1<-reclassification(data=prob_valida,cOutcome = 1,predrisk1 = prob_valida$IELSG1,
                                       predrisk2 = prob_valida$MSKCC1,cutoff = c(0,0.5,1))


#--------------------------------------radiomics train&test roc-----------------------------------#
IELSG_train_roc<-roc(prob_train$lable,prob_train$IELSG,ci=TRUE)
IELSG1_train_roc<-roc(prob_train$lable,prob_train$IELSG1,ci=TRUE)
MSKCC_train_roc<-roc(prob_train$lable,prob_train$MSKCC,ci=TRUE)
MSKCC1_train_roc<-roc(prob_train$lable,prob_train$MSKCC1,ci=TRUE)
radscore_train_roc<-roc(prob_train$lable,prob_train$radscore,ci=TRUE)
clinical_train_roc<-roc(prob_train$lable,prob_train$clinical,ci=TRUE)
IELSG_valida_roc<-roc(prob_valida$lable,prob_valida$IELSG,ci=TRUE)
IELSG1_valida_roc<-roc(prob_valida$lable,prob_valida$IELSG1,ci=TRUE)
MSKCC_valida_roc<-roc(prob_valida$lable,prob_valida$MSKCC,ci=TRUE)
MSKCC1_valida_roc<-roc(prob_valida$lable,prob_valida$MSKCC1,ci=TRUE)
radscore_valida_roc<-roc(prob_valida$lable,prob_valida$radscore,ci=TRUE)
clinical_valida_roc<-roc(prob_valida$lable,prob_valida$clinical,ci=TRUE)


#------------------------------------------delong test--------------------------------------#
roc.test(IELSG_train_roc,radscore_train_roc)
roc.test(radscore_train_roc,IELSG1_train_roc)
roc.test(MSKCC_train_roc,radscore_train_roc)
roc.test(radscore_train_roc,MSKCC1_train_roc)
roc.test(IELSG1_train_roc,MSKCC1_train_roc)
roc.test(IELSG_valida_roc,radscore_valida_roc)
roc.test(radscore_valida_roc,IELSG1_valida_roc)
roc.test(MSKCC_valida_roc,radscore_valida_roc)
roc.test(radscore_valida_roc,MSKCC1_valida_roc)
roc.test(IELSG1_valida_roc,MSKCC1_valida_roc)

