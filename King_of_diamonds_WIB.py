# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:36:03 2026

@author: User
"""
import story_locked_bots as bot

players = [0,0,0,0,0]
my_bots = [bot.Benzo,bot.Kuzuryu,bot.Daimon,bot.Asuma]
el_status = [["BENZO",0],["CHISHIYA",0],["KUZURYU",0],["DAIMON",0],["ASUMA",0]]

last_choices = [-1,-1,-1,-1,-1]
clause = 0
round_count = 0
result = None
won = None

def rounds(players,clause):
    current = []
    Players(current,el_status)
    print("Player choices: ", current)
    result = (sum(current)/len(current))*0.8
    print("Result: ",result)
    if len(players) <= 2:
        if 100 not in current or 0 not in current:
            diff = point_counter(current,result)
            kill(players,current,result,diff)
        else:
            for i in range(2):
                if current[i] == 0:
                    players[i] -= 1
                    while -10 in players:
                        players.remove(-10)
                    while -11 in players:
                        players.remove(-11)
            diff = 100
    else:
        diff = point_counter(current, result)
        kill(players,current,result,diff)
    last_choices = current
    return players,last_choices,result,diff

def point_counter(current,result):
    diff = 100
    if len(current) <= 3:
        temp = current.copy()
        for i in range(len(current)):
            for j in range(i+1,len(current)):
                if current[i] == current[j]:
                    temp[i] = temp[j] = 100
        current = temp
    for k,i in enumerate(current):
        c_diff = abs(result-i)
        if c_diff < diff:
            diff = c_diff
    return diff
        
def kill(players,current,result,diff):
    penalty = 1
    if len(players) <= 4:
        if int(diff) == 0:
            penalty = 2
    player = 0
    for j in range(len(players)):
        if el_status[j][1]:
            player += 1
        if abs(result-current[j]) != diff:
            players[j] -= penalty
            if players[j] == -10 or players[j] == -11:
                el_status[player][1] = 1
        player += 1
    number = current[0]
    for i in range(len(current)):
        if current[i] != number:
            break
        if i == len(current):
            for p in players:
                p -= 1
    while -10 in players:
        players.remove(-10)
    while - 11 in players:
        players.remove(-11)
    return players
 
def Players(current,el_status):
    j = 0
    for i in range(5):
        if i == 1:
            current.append(int(input("choose a number in range 0 to 100: ")))
        else:
            if not el_status[i][1]:
                try:
                    prev_guess = last_choices[i]
                    current.append(my_bots[j](players,prev_guess,result,clause,won))
                    j += 1
                except:
                    prev_guess = last_choices[j - 1]
                    current.append(my_bots[j](players,prev_guess,result,clause,won))
            else:
                j += 1
    return current
    
while len(players) > 1:
    
    print(f"Round {round_count+1}")
    players,last_choices,result,diff = rounds(players,clause)
    
    if el_status[1][1]:
        print("\nGame Over!")
        break
    elif len(players) == 1:
        print("Game clear, the winner is Chishiya Shuntarou")
        break
    if diff + result in last_choices:
        won = diff + result
    else:
        won = result - diff   
    game_screen = []
    j = 0
    for i in range(5):
        if el_status[i][1]:
            status = "eliminated"
            j -= 1
        else:
            try:
                status = players[j]
            except:
                print("\nidk bro\n")
        game_screen.append(f"{el_status[i][0]}: {status}")
        j += 1
    print(game_screen,'\n')
    
    if 100 in last_choices:
        clause += 1
    elif clause > 0:
        clause = 0.5
    round_count += 1