#The OG! completely random just to get a nice gist
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
        numCircles = int(inputbox.get())
        canvas.delete("all")
        circles = []
        trueForAll = False
        playGame()
    except:
        pass

numCircles = 6
circles = []

def fillCircles():
    
    if numCircles < 3:    
        for i in range(numCircles):
            color = "blue" if random.randint(0, 1) == 1 else "red"
            circles.append([color, i])
    else:
        circles.append(["blue" if random.randint(0,1) == 1 else "red", 0])
        circles.append(["blue" if random.randint(0,1) == 1 else "red", 1])
        index = 2
        while len(circles) < numCircles:
            if(circles[index - 2][0] == "blue"):
                circles.append(["red", index])
            elif(circles[index - 2][0] == "red"):
                circles.append(["blue", index])
            index += 1

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
    prevLen = numCircles
    while not trueForAll:
        prevLen = len(circles)
        circles = round(150*((roundNum-1)%4)+150, 140*((roundNum//5)+1)-40, circles)
        roundNum+=1

inputbox.bind("<Return>", onEnter)
root.mainloop()