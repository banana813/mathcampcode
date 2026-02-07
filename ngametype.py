#Type in the R and B string for the circles. helpful for testing stuff
import tkinter as tk
import random
import math

ringR = 60
ringSpacing = 10
lilR = 10
trueForAll = False

root = tk.Tk()
root.title("N-Game")

inputbox = tk.Entry(root)
inputbox.pack()

canvas = tk.Canvas(root, width = "800", height="400", bg="white")
canvas.pack()

def onEnter(_):
    try:
        global numCircles
        global circles
        global trueForAll
        global fillString
        numCircles = len(inputbox.get())
        fillString = inputbox.get().lower().strip()
        canvas.delete("all")
        circles = []
        trueForAll = False
        playGame()
    except:
        pass

numCircles = 6
fillString = ""
circles = []

def fillCircles():
    global fillString
    for i in range(len(fillString)):
        if(fillString[i] == "r"):
            circles.append(["red", i])
            print("Appending R")
        elif(fillString[i] == "b"):
            circles.append(["blue", i])
            print("Appending B")

def round(x, y, circles):
    global trueForAll
    toKeep = []
    canvas.create_oval(x - ringR, y - ringR, x + ringR, y + ringR, outline="black", width=3, fill="")
    for i in range(len(circles)):
        angle = (math.pi*2*i)/len(circles)
        circleX = math.cos(angle)*ringR + x
        circleY = math.sin(angle)*ringR + y
        canvas.create_oval(circleX - lilR, circleY - lilR, circleX + lilR, circleY + lilR, outline="", fill=circles[i][0])

    
    trueForAll = True    
    for i in range(len(circles)):
        prev = circles[(i-1)%len(circles)][0]
        next = circles[(i+1)%len(circles)][0]
        if(prev == next):
            toKeep.append(circles[i])
        else:
            trueForAll = False
  
    circles = toKeep
    return toKeep

def playGame():
    global circles
    fillCircles()
    roundNum = 1
    while not trueForAll:
        circles = round(150*((roundNum-1)%4)+150, 140*((roundNum//5)+1)-40, circles)
        roundNum+=1

inputbox.bind("<Return>", onEnter)
root.mainloop()