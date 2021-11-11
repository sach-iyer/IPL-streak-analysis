# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:46:47 2020

@author: sachin
"""
import pandas as pd
"""
df_ipl = []
sheets = ["Sheet1","Sheet2","Sheet3","Sheet4","Sheet5","Sheet6","Sheet7","Sheet8","Sheet9","Sheet10","Sheet12"]

for season in range(12):
"""    

excel_file_path = r""

df_ipl08 = pd.read_excel(excel_file_path,\
                       sheet_name = "Sheet1",\
                       usecols = ['Team 1','Team 2','Winner'],\
                       skipfooter = 4)
    
team_streak = [[],[],[],[],[],[],[],[]]
no_of_teams = 8
num_outcomes = 8

def check_streak():
    global team_streak
    flag = 1
    
    for i in range(no_of_teams):
        if (len(team_streak[i]) < 3):
            flag = 0
        
    if flag == 1:
        latest_streak = set([])
        for i in range(no_of_teams):
                latest_streak.add(tuple(team_streak[i][-3:]))
    
        if len(latest_streak) == num_outcomes:
            print('Yay!')
            return True
   
    return False
    
for i in range(56):
#    global team_streak
    
    t1 = df_ipl08.loc[i].loc['Team 1']
    t2 = df_ipl08.loc[i].loc['Team 2']
    win = df_ipl08.loc[i].loc['Winner']
    
    if (t1 == win):
        team_streak[t1].append(1)
        team_streak[t2].append(0)
        
    elif (t2 == win):
        team_streak[t2].append(1)
        team_streak[t1].append(0)

    if (check_streak()):
        print('Match no.', i)
        