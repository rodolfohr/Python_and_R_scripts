#Profits
setwd('C:/Users/Rodolfo Herrera/Documents/HULT MIB/Dual Degree/Intro to R/files')

case_data <- read_excel('Air France Case Doubleclick.xls')
summary(case_data)

library(sqldf)

#CHange names of some columns 

case_data$Click_Charges <- NULL

colnames(case_data)
colnames(case_data)[21] = "Total_Cost"
colnames(case_data)[22] = "Total_Volume_Bookings"
colnames(case_data)[16] = "Engine_Click_Thru"
colnames(case_data)[18] = "Conversion_Rate"


#Separate data between profitable and unprofitable
profitables <- subset(case_data, case_data$Amount > 0)

money_hose <- subset(case_data, case_data$Amount == 0)

summary(profitables)

#Costs and revenue by Company

sqldf("SELECT Publisher_Name, SUM(Total_Cost) as cost
       FROM case_data
      Group BY Publisher_Name
      Order by cost DESC
      ")

sqldf("SELECT Publisher_Name, SUM(Amount) as revenue
       FROM case_data
      Group BY Publisher_Name
      Order by revenue DESC
      ")

#Profits by company 
sqldf("SELECT Publisher_Name, (SUM(Amount)- SUM(Total_Cost)) AS profit
        FROM case_data c
      GROUP BY Publisher_Name
      ORDER BY profit DESC
      ")

sqldf("SELECT Publisher_Name, (SUM(Amount)- SUM(Total_Cost))/SUM(Total_Cost)
      FROM profitables
      GROUP BY Publisher_Name
      ")

#ROI 

sqldf("SELECT Publisher_Name, (SUM(Amount)- SUM(Total_Cost))/SUM(Total_Cost) AS ROI
        FROM case_data
      GROUP BY Publisher_Name
      ")


sqldf("SELECT Publisher_Name, (SUM(Amount)- SUM(Total_Cost))/SUM(Total_Cost) AS ROI 
        FROM profitables
      GROUP BY Publisher_Name
      ")

#Based on these results, we will focus on Yahoo and Google, as they are the most relevant companies

#########################################################################################################
#Quick grouping and analysis of data

#Profits by Keyword

sqldf("SELECT Keyword_Group,Campaign, (SUM(Amount)- SUM(Total_Cost)) AS profit
        FROM case_data
        GROUP BY Keyword_Group, Campaign
        Order BY profit")

sqldf("SELECT Keyword_Group, (SUM(Amount)- SUM(Total_Cost)) AS profit
        FROM profitables
      GROUP BY Keyword_Group
      Order BY profit")

#Profit by campaign and publisher 

campaign_profit_filtered <- sqldf("SELECT Campaign,  (SUM(Amount) - SUM(Total_Cost)) AS profit
        FROM case_data
        WHERE Publisher_Name IN ('Yahoo - US', 'Google - US', 'Google - Global') AND Campaign IN ('Air France Branded')
        GROUP BY Campaign
        Order BY profit")


sqldf("SELECT Campaign,  SUM(Amount) as rev
        FROM case_data
        GROUP BY Campaign
        Order BY rev ")

#By Match_Type

sql_matchs_ROA <- sqldf("SELECT Match_Type, (SUM(Amount)- SUM(Total_Cost))/SUM(Total_Cost) AS ROI
      FROM profitables
      GROUP BY Match_type
      Order BY ROI")

profit_sql_match <- sqldf("SELECT Match_Type, (AVG(Amount)- AVG(Total_Cost)) AS Profit
      FROM profitables
      GROUP BY Match_type
      Order BY Profit")


###############################Creating correlation matrix, based of subset ##################################################

for(i in 1:nrow(sql_profit)) {
  if(sql_profit$Match_Type[i] == "Advanced") { sql_profit$Match_Type[i] <- 1
  }  else if(sql_profit$Match_Type[i] == "Exact" ) {sql_profit$Match_Type[i] <-2
  }  else if(sql_profit$Match_Type[i]== "Broad") {sql_profit$Match_Type[i] <- 3
  }  else if(sql_profit$Match_Type[i] == "Standard") {sql_profit$Match_Type[i] <- 4
  }  else if(sql_profit$Match_Type[i] == "N/A") {sql_profit$Match_Type[i] <- 5}}

sql_profit$Match_Type <- as.numeric(sql_profit$Match_Type)
sql_profit$Campaign <- as.numeric(sql_profit$Campaign)

library(Hmisc)
myvars <- c("Match_Type","Engine_Click_Thru", "Impressions", "Total_Cost",  "Conversion_Rate", "Total_Volume_Bookings", "profit")
korr_test <- sql_profit[myvars]


res2 <- cor(korr_test)


library(corrplot)
corrplot(res2, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45)


