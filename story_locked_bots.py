# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 08:29:09 2026

@author: User
"""

##STORY LOCKED EXPLANATION: whenever characters make random choices, the
##result will be as is in the narrative, like daimon's random number being 62

def Choice():
    decision = input("do you want to show Kuzuryu your number? ")
    if decision == "yes":
        return True
    else:
        return False

def Kuzuryu(players,prev_guess,result,clause,last_winner):
    if prev_guess == -1:
       return 29
    elif len(players) == 2:
       if Choice():
           return 0
       else:
           if prev_guess == 1 and prev_guess != last_winner:
               return 1
           elif prev_guess != 100:
               if prev_guess != last_winner:
                   return 100
               else:
                   return 1
           else:
               return 0
    if len(players) == 3:
        return 1
    elif clause < 1:
        if prev_guess == 0:
            if int(result) == 0:
                if max(players) == players[2]:
                    return 0
                else:
                    return 100
                
        if last_winner/2 >= 10:
            return last_winner // 2
        else:
            if last_winner % 2 == 0:
                discount = 1.5
            else:
                discount = 1
            number = int(last_winner/2 - discount)
            if number < 0:
                number = 0
            return number
    else:
        if clause == 1:
            return int(result) + 1
        elif clause < 3:
            return int(0.8*(result/2)) + 1
        else:
            return 20
                   
def Daimon(players,prev_guess,result,clause,last_winner):
    if prev_guess == -1:
        return 40 
    elif len(players) == 3:
        if players[2] >= -8 and -9 in players:
            return 62
        else:
            return 1
    if clause > 0:
        if clause == 1:
            return 100
        elif prev_guess == 100:
            return int((last_winner/2 * 4 + 100)/5)
        if -9 in players:
            return int(result)
        else:
            if int(result/2) - 1 >= 0:
                return int(result/2) - 1
            return 0
    else:
        if prev_guess//2 < int(result):
            if (prev_guess/0.8)/2 == (int(result)):
                return prev_guess//2
            elif (prev_guess/0.8)/2 < int(result)-1:
                return prev_guess//2 -1
            return int(prev_guess/2 + 1)
        else:
            if int(result) == 0:
                return 0
            else:
                return prev_guess//2 - 1
    
def Benzo(players,prev_guess,result,clause,last_winner):
    if prev_guess == -1:
        return 30
    else:
        if clause >= 3:
            return 36
        elif type(clause) == int:
            if prev_guess == 0:
                return 0
            else:
                if result/2 < 10:
                    number = (0.8*(result/2) + 0.8*(result/4))/2*0.8
                    if int(number) <= 1:
                        return 0
                else:
                    number = (result/2 + result)/2*0.8
                return round(number)
        else:
            if result > 10:
                if prev_guess == 2:
                        return 3
                else:
                    return 2
            else:
                return 0
        
def Asuma(players,prev_guess,result,clause,last_winner):
    if prev_guess == -1:
        return 33
    if clause < 1:               
        if last_winner/2 <= 4:
            return 0
        if type(clause) != int:
            if last_winner/2 <= 3:
                return 0
            return last_winner
        return round(last_winner/2+0.1)
    else:
        if clause < 2:
            return 5
        elif clause < 3:
            return prev_guess - 1
        else:
            return 34
