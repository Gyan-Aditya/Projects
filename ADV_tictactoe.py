# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 01:41:10 2024

@author: KIIT
"""

import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

top=Frame(root,bg='Cadet Blue',pady=2,width=1350,height=100,relief=RIDGE)
top.grid(row=0,column=0)

title=Label(top,font=('arial',50,'bold'),text="Advanced Tic Tac Toe Game",bd=21,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
title.grid(row=0,column=0)

mainFrame=Frame(root,bg='Powder Blue',pady=2,width=1350,height=600,relief=RIDGE)
mainFrame.grid(row=1,column=0)

leftFrame=Frame(mainFrame,bd=10,width=750,height=500,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame=Frame(mainFrame,bd=10,width=560,height=500,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1=Frame(rightFrame,bd=10,width=560,height=200,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
rightFrame1.grid(row=0,column=0)

rightFrame2=Frame(rightFrame,bd=10,width=560,height=200,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
rightFrame2.grid(row=1,column=0)

playerX=IntVar()
playerO=IntVar()

playerX.set(0)
playerO.set(0)

buttons=StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
        scorekeeper()
    elif buttons["text"]==" " and click==False:
        buttons["text"]="O"
        click=True
        scorekeeper()
        
def scorekeeper():
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
        button1.config(background="Powder Blue")
        button2.config(background="Powder Blue")
        button3.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
    if button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
        button4.config(background="Red")
        button5.config(background="Red")
        button6.config(background="Red")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
    if button7["text"]=="X" and button8["text"]=="X" and button8["text"]=="X":
        button7.config(background="Grey")
        button8.config(background="Grey")
        button9.config(background="Grey")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
        
    if button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
        button1.config(background="Powder Blue")
        button4.config(background="Powder Blue")
        button7.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
        
    if button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
        button2.config(background="Powder Blue")
        button5.config(background="Powder Blue")
        button8.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
        
    if button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
        button3.config(background="Powder Blue")
        button6.config(background="Powder Blue")
        button9.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
    
    if button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
        button1.config(background="Powder Blue")
        button5.config(background="Powder Blue")
        button9.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
        
    if button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
        button3.config(background="Powder Blue")
        button5.config(background="Powder Blue")
        button7.config(background="Powder Blue")
        n=float(playerX.get())
        score= n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X, You have just won a game")
        
        
        
        
        
        
    if button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O":
        button1.config(background="Orange")
        button2.config(background="Orange")
        button3.config(background="Orange")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
    if button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O":
        button4.config(background="Red")
        button5.config(background="Red")
        button6.config(background="Red")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
    if button7["text"]=="O" and button8["text"]=="O" and button8["text"]=="O":
        button7.config(background="Grey")
        button8.config(background="Grey")
        button9.config(background="Grey")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
        
    if button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O":
        button1.config(background="Powder Blue")
        button4.config(background="Powder Blue")
        button7.config(background="Powder Blue")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
        
    if button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O":
        button2.config(background="Powder Blue")
        button5.config(background="Powder Blue")
        button8.config(background="Powder Blue")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
        
    if button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O":
        button3.config(background="green")
        button6.config(background="green")
        button9.config(background="green")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
    
    if button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O":
        button1.config(background="Blue")
        button5.config(background="Blue")
        button9.config(background="Blue")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
        
    if button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O":
        button3.config(background="Blue")
        button5.config(background="Blue")
        button7.config(background="Blue")
        n=float(playerO.get())
        score= n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O, You have just won a game")
        
        
def reset():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    
    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

def NewGame():
    reset()
    playerx.set(0)
    playerO.set(0)
    
lblPlayerX=Label(rightFrame1,font=('arial', 40, 'bold'),text="Player X:",padx=2,pady=2,bg='Cadet Blue')
lblPlayerX.grid(row=0,column=0,sticky=W)
txtplayerX=Entry(rightFrame1,font=('arial',40,'bold'),bd=2,fg="Black",textvariable=playerX,width=14,justify=LEFT).grid(row=0,column=1)

lblPlayerO=Label(rightFrame1,font=('arial', 40, 'bold'),text="Player O:",padx=2,pady=2,bg='Cadet Blue')
lblPlayerO.grid(row=1,column=0,sticky=W)
txtplayerO=Entry(rightFrame1,font=('arial',40,'bold'),bd=2,fg="Black",textvariable=playerO,width=14,justify=LEFT).grid(row=1,column=1)

btnReset=Button(rightFrame2,text="Reset",font=('Times 26 bold'),height=1,width=20,bg='gainsboro',command=reset) 
btnReset.grid(row=0,column=0,padx=6,pady=11)

btnNew=Button(rightFrame2,text="New Game",font=('Times 26 bold'),height=1,width=20,bg='gainsboro',command=NewGame)
btnNew.grid(row=1,column=0,padx=6,pady=10)


button1=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

root.mainloop()
