#lets you type in number of blue and red, and randomly does it
import tkinter as tk
import random
import math

ringR = 60
ringSpacing = 10
lilR = 10
trueForAll = False

root = tk.Tk()
root.title("N-Game")

inputboxblue = tk.Entry(root)
inputboxblue.pack()
inputboxred = tk.Entry(root)
inputboxred.pack()

canvas = tk.Canvas(root, width = "800", height="400", bg="white")
canvas.pack()

def onEnter(_):
    try:
        global numBlueCircles
        global numRedCircles
        global circles
        global trueForAll
        print(int(inputboxblue.get()))
        numBlueCircles = int(inputboxblue.get())
        print(int(inputboxred.get()))
        numRedCircles = int(inputboxred.get())
        canvas.delete("all")
        circles = []
        trueForAll = False
        playGame()
    except:
        pass

numBlueCircles = 3
numRedCircles = 3
circles = []

def fillCircles():
    global numBlueCircles
    global numRedCircles
    global circles
    for i in range(numBlueCircles):
        print("Appending Blue")
        circles.append(["blue", i])
    while len(circles) < numBlueCircles + numRedCircles:
        index = random.randint(0, len(circles))
        print("Appending red")
        circles.insert(index ,["red", index])
    print(f"Done filling circles; {len(circles)}")
    print(circles)

def round(x, y, circles):
    print("Entering Round!")
    global trueForAll
    toKeep = []
    print("About to draw big circle!")
    canvas.create_oval(x - ringR, y - ringR, x + ringR, y + ringR, outline="black", width=3, fill="")
    print("Finished drawing big circle!")
    for i in range(len(circles)):
        angle = (math.pi*2*i)/len(circles)
        circleX = math.cos(angle)*ringR + x
        circleY = math.sin(angle)*ringR + y
        canvas.create_oval(circleX - lilR, circleY - lilR, circleX + lilR, circleY + lilR, outline="", fill=circles[i][0])

    
    trueForAll = True    
    for i in range(len(circles)):
        print(f"Iteration: {i}")
        prev = circles[(i-1)%len(circles)][0]
        next = circles[(i+1)%len(circles)][0]
        if(prev == next):
            toKeep.append(circles[i])
            print("I've been kept!")
        else:
            trueForAll = False
            print("Sorry nope")
        print(f"True For All: {trueForAll}")
    print("I have now made it to the end of the for loop!")
    
    print("Ok, here i am prior to being about to exit this round?")
    circles = toKeep
    print("Here i am, about to exit this round")
    return toKeep

def playGame():
    global circles
    fillCircles()
    roundNum = 1
    prevLen = numRedCircles+numBlueCircles
    while not trueForAll:
        prevLen = len(circles)
        circles = round(150*((roundNum-1)%4)+150, 140*((roundNum//5)+1)-40, circles)
        roundNum+=1

inputboxblue.bind("<Return>", onEnter)
inputboxred.bind("<Return>", onEnter)
root.mainloop()