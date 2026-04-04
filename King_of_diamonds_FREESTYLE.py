# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:46:18 2026

@author: User
"""

players = [0,0,0,0,0]
round_count = 1

def rounds(players):
    current = []
    for p in players:
        number = int(input("choose a number in range 0 to 100: "))
        current.append(number)
    result = (sum(current)/len(current))*0.8
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
    else:
        diff = point_counter(current, result)
        kill(players,current,result,diff)
    return players

def point_counter(current,result):
    diff = 100
    if len(current) <= 3:
        for i in range(len(current)):
            for j in range(i+1,len(current)):
                if current[i] == current[j]:
                    current[i] = current[j] = 100
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
    for j in range(len(players)):
        if abs(result-current[j]) != diff:
            players[j] -= penalty
    while -10 in players:
        players.remove(-10)
    while -11 in players:
        players.remove(-11)
    return players

while len(players) > 1:
    print(rounds(players))
    round_count += 1