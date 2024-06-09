# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:37:55 2024

@author: KIIT

"""
import random
boards=["-","-","-","-","-","-","-","-","-"]
currentPlayer='X'
gameRunning=True
winnner=None

def printboard(boards):
    print(boards[0]," | ",boards[1]," | ",boards[2])
    print(boards[3]," | ",boards[4]," | ",boards[5])
    print(boards[6]," | ",boards[7]," | ",boards[8])
    
def userInput(boards):
    insp=int(input("Enter a number between 1-9:"))
    if boards[insp-1]=="-":
        boards[insp-1]=currentPlayer
    else:
        print("Other player")
        userInput(boards)
        
def checkHorizontal(boards):
    global winner
    if boards[0]==boards[1]==boards[2] and boards[0]!="-":
        winner=boards[1]
        return True
    elif boards[3]==boards[4]==boards[5] and boards[3]!="-":
        winner=boards[3]
        return True
    elif boards[6]==boards[7]==boards[8] and boards[6]!="-":
        winner=boards[7]
        return True
    
def checkVertical(boards):
    global winner
    if boards[0]==boards[3]==boards[6] and boards[0]!="-":
        winner=boards[0]
        return True
    elif boards[1]==boards[4]==boards[7] and boards[1]!="-":
        winner=boards[1]
        return True
    elif boards[2]==boards[5]==boards[8] and boards[8]!="-":
        winner=boards[5]
        return True

def checkDiag(boards):
    global winner
    if boards[0]==boards[4]==boards[8] and boards[0]!="-":
        winner=boards[0]
        return True
    elif boards[2]==boards[4]==boards[6] and boards[6]!="-":
        winner=boards[4]
        return True
    
def checkWinner(boards):
    global gameRunning
    if checkDiag(boards) or checkHorizontal(boards) or checkVertical(boards):
        print("The winner is {}".format(winner))
        gameRunning=False
        
def checkTie(boards):
    global gameRunning
    if "-" not in boards:
        print("The match is draw")
        gameRunning=False

def switchPlayer(boards):
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="o"
    else:
        currentPlayer="X"
        
def computer(boards):
    insp=random.randint(0,8)
    if "-" not in boards:
        return 
    if boards[insp]=="-":
        boards[insp]="o"
    else:
        computer(boards)

while gameRunning:
    printboard(boards)
    userInput(boards)
    checkWinner(boards)
    checkTie(boards)
    #switchPlayer(boards)
    computer(boards)
    printboard(boards)
    checkWinner(boards)
    checkTie(boards)
    