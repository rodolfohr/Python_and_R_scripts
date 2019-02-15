library(plyr)
install.packages("tidyverse")
library(tidyverse)
library(readr)
library(rpart)
library(rpart.plot)

#Importing the data 

setwd("C:/Users/Rodolfo Herrera/Documents/HULT MIB/Dual Degree/Intro to R/r_scripts/Data_sets")

fertility <- read.csv('fertility.csv',fileEncoding="UTF-8-BOM")

# Basic exploratory analysis
head(fertility)
tail(fertility)
summary(fertility)
str(fertility)

typeof(fertility)

fertility <- as.data.frame(fertility)

#Check for missing numbers 

fertility[is.na(fertility)]
sum(is.na(fertility))

#Turn character variables into numeric: 
fertility_num <- fertility

fertility_num$output <- gsub('O',1,fertility_num$output)
fertility_num$output <- gsub('N',0,fertility_num$output)

fertility_num$output <- as.numeric(fertility_num$output)

#As there are no missing values, we do not need to massage the data

##########################################################################################
#Create a logistic model 
colnames(fertility_num)

fertility_num <- as.data.frame(fertility_num)

log <- glm(output~season+age+accident+surgical_inter+smoking+sitting+high_fever+frequency_alcohol, 
           data = fertility_num, family = "binomial")
summary(log)

#Note, as we had no deeper knowledge of the database, it was decided to check every parameter and eliminate them one by one
#Eliminating non-significant variables:

log1 <- glm(output~age+accident+high_fever+frequency_alcohol, data = fertility_num, family = "binomial")
summary(log1)


log2 <- glm(output~accident+frequency_alcohol, data = fertility_num, family = "binomial")
summary(log2)


#Compare the different models using the AIQ and use the one with the lowest relative value. In this case it 
# is the second 

plot(log1)

#In this case, both values had a significant p-value. Therefore, we should try to get more data before using
#them for predictive analysis. 

#If this was not the case, we could have made a decision tree.
#I will use data from the Titanic database to ilustrate this principle:

##############################
#Creating a tree for titanic
##############################
library(titanic)
titanic_tree <- rpart(Survived ~ Pclass + Sex + Age+ SibSp, data = titanic_train, method = "class")#, control=rpart.control(minsplit=50, cp=0.013))
#The plot bellow can be called by only using rpart.plot:
rpart.plot(mytree, type = 1, extra=1, box.palette =c("pink", "green"), branch.lty=3, shadow.col = "gray")

#To see the best size of tree: 
plotcp(mytree)


#We can use this model to predict the values of our data: 

val_1 <- predict(titanic_tree, titanic_train, type="prob")
print(val_1)
