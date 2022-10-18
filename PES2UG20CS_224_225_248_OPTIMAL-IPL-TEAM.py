import pandas as pd
import numpy as np
from IPython.display import display

df_matches = pd.read_csv('matches.csv')
df_deliveries = pd.read_csv('deliveries.csv')
#Check number of NULL values in the matches and deliveries csv files
# print(df_deliveries['player_dismissed'].isna().sum()+df_deliveries['dismissal_kind'].isna().sum()+df_deliveries['fielder'].isna().sum())

#Replace NULL values with NA
df_deliveries= df_deliveries.fillna('NA')
print("First we do the preprocessing and cleaning for the matches dataset:")
print("Checking for null values in the dataset:")
print(df_matches.isna().sum().sum())
df_matches= df_matches.fillna('NA')
print("On filling the null values with NA we re check the number of null values=",df_matches.isna().sum().sum())
print("Checking for all columns and number of rows in the dataset:")
print("columns=",df_matches.columns.tolist())
print("No of rows=",df_matches.shape[0])
print("Now we drop the not required columns umpire1,umpire2,umpire3-")
df_matches=df_matches.drop(['umpire1', 'umpire2','umpire3'], axis=1)
print("columns=",df_matches.columns.tolist())
print("Next we deal with duplicates or incorrect data:\n Our data will have duplicated in terms of city,venue,team1,team2,toss_winner,toss_decision etc but all these are necessary for being able to predict \n accurate performace of players and hence cant be deleted.Hence we have no unecessary duplicate data")
print ("Next we check for incorrect data:")
print(df_matches["venue"].unique())
print("From the above we see that M Chinnaswamy Stadium has 2 different spellings so we replace all with a common spelling")
df_matches=df_matches.replace('M. Chinnaswamy Stadium','M Chinnaswamy Stadium')
print(df_matches["winner"].unique())
print(df_matches["toss_winner"].unique())


# print(df_deliveries.isna().sum().sum())
# print(df_deliveries.columns.tolist())
# #Check for incorrect data or spelling mistakes
# print(df_matches["venue"].unique())
# #Replace stadiums with different spellings with a common spelling
# df_matches=df_matches.replace('M. Chinnaswamy Stadium','M Chinnaswamy Stadium')
# print(df_deliveries.columns.tolist())
# print(df_deliveries["inning"].unique())
# #innings cannot have values  3,4 and 5
# df_deliveries["inning"] = np.where(df_deliveries["inning"] == "4" or df_deliveries["inning"] == "5" or df_deliveries["inning"] == "3",df_deliveries["is_super_over"]='TRUE')
# print(df_deliveries["bowler"].unique())
# print(df_deliveries["batsman"].unique())
# #Check for incorrect data in innings