# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:19:17 2020

@author: Sachin
"""
import random as rd
#from itertools import product

##########      LIST OF GLOBAL VARIABLES        ###########

num_teams = 8
teams = list(range(num_teams))
streak_len = 3
num_outcomes = 2**streak_len
team_streak = [[],[],[],[],[],[],[],[]]
draw = []
match_of_streak = []
list_no_of_hits =[]
total_hits = 0

temp_hits = 0
seasons_with_hits = 0

#all_matches = list(set(product(teams,teams)) - set(zip(teams,teams)))
#matches_avbl = set(all_matches[:])
#want_streak = {}
#for i in range(num_teams):   want_streak.add([i%2,int(i/2)%2,int(i/4)%2])

############################################################
def reset():
    global team_streak, draw, list_no_of_hits, total_hits, temp_hits, seasons_with_hits
    team_streak = [[],[],[],[],[],[],[],[]]
    draw = []
    list_no_of_hits =[]
    total_hits = 0
    temp_hits = 0
    seasons_with_hits = 0

def do_sim(n):
#    global team_streak, draw, list_no_of_hits, total_hits, seasons_with_hits, temp_hits
    
#    reset()
    
    i=n
    while i>0:
        
#        global team_streak, draw, list_no_of_hits, total_hits, seasons_with_hits, temp_hits
        
        team_streak = [[],[],[],[],[],[],[],[]]
        draw = []
#        match_of_streak = []
        
        gen_draw()                    #<------ gen_draw() is called
        
        list_no_of_hits.append(temp_hits)        
        total_hits+=temp_hits
        if (temp_hits):
            seasons_with_hits +=1
        i-=1
    prob_perc = (100*seasons_with_hits/n)
    
    print('prob_perc = ', prob_perc)
    return total_hits

###########################################################
def check_streak():
   latest_streak = set([])
   for i in range(num_teams):
       latest_streak.add(tuple(team_streak[i][-3:]))
    
   if len(latest_streak) == num_outcomes:
     #  print('Yay!')
       return True
   
   return False 
#    for x in set_of_last_3:
#        latest_streak.add(x)
    

def match_result(match):
#    match = list(match)
    winner = rd.choice(match)
    match.remove(winner)
    team_streak[winner].append(1)
    team_streak[match[0]].append(0)

def gen_draw():
    global temp_hits,draw
    
    temp_hits = 0
    matches_done= 0
    ribbon = teams[:]
    rd.shuffle(ribbon)
 #   matchday = []
    #LOOP FOR MATCHDAY GENERATION
    for i in range((num_teams-1)*2):
        
        for j in range(int(num_teams/2)):
            
            draw.append([ribbon[j],ribbon[num_teams-1-j]])
            match_result([ribbon[j],ribbon[num_teams-1-j]])
            matches_done += 1
            
            if (i>=3 or (i == 2 and j == int(num_teams/2 - 1))):
        
                if (check_streak()):
                    if matches_done<12:
                        return 0
                    #match_of_streak.append(matches_done)
                    temp_hits+=1
                
        #ROTATION (RIBBON[0] IS FIXED)
        k = num_teams-1
        temp = ribbon[k]
        while k>1:
            ribbon[k] = ribbon[k-1]
            k-=1
        ribbon[1] = temp
    
    return 1


"""                     Failed attempts before I knew about round robin algorithms

def  gen_matchday():
    matchday = []
    teams_avbl = set(teams[:])
    i=0
    count = 0
    
    while i<4:
        
        t1 = rd.sample(teams_avbl, k=1)[0]
        t1_home = [y for y in matches_avbl if (y[0]==t1 and y[1] in teams_avbl)]
        
        if (t1_home == []):
            i=0
            count += 1
            teams_avbl = set(teams[:])
            matchday = []
            print("RESET",count)
            if (count == 200):
                import sys
                sys.exit()
            
            continue
            
            
        match = rd.choice(t1_home)
        
        
        match_result(match)
        
        teams_avbl.remove(match[0])        
        teams_avbl.remove(match[1])
        
        matchday.append(match)
        
        i+=1
    for x in matchday:
        matches_avbl.remove(x)
    return matchday
        
#rd.shuffle(team)
"""