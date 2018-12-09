import turtle

def checkFactors(number,circleSize):
    numFactors = 0
    for i in range (2,int(number)):
        if (int(number) % i) == 0:
            numFactors+=1


    if numFactors > 0 :
        return ("yellow","yellow",circleSize)
    else:
        return ("red","red",circleSize)

def draw(turtleA):
    #square size = n*2 + 1
    n = 4
    up = 1
    right = 1
    left = 2
    down = 2
    x = 0
    y = 0
    circleNumber = 1
    circleSize = 20
    circleSpacing = circleSize*2 + 1

    turtleA.pendown()
    turtleA.begin_fill()
    turtleA.circle(circleSize)
    turtleA.setposition(x,y)
    turtleA.penup()
    turtleA.end_fill()
    y+=10
    turtleA.setposition(x,y)
    turtleA.color("black")
    turtleA.pendown()
    turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
    turtleA.penup()
    y-=10
    circleNumber+=1


    
    for i in range (0,int(n)):
        for r in range(0,int(right)):
            x+=circleSpacing
            turtleA.setposition(x,y)
            circleType = checkFactors(circleNumber,circleSize)
            turtleA.color(circleType[0],circleType[1])
            turtleA.pendown()
            turtleA.begin_fill()
            turtleA.circle(circleType[2])
            turtleA.penup()
            turtleA.end_fill()
            y+=10
            turtleA.setposition(x,y)
            turtleA.color("black")
            turtleA.pendown()
            turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
            turtleA.penup()
            y-=10
            circleNumber+=1
        for u in range(0,int(up)):
            y+=circleSpacing
            turtleA.setposition(x,y)
            circleType = checkFactors(circleNumber,circleSize)
            turtleA.color(circleType[0],circleType[1])
            turtleA.pendown()
            turtleA.begin_fill()
            turtleA.circle(circleType[2])
            turtleA.penup()
            turtleA.end_fill()
            y+=10
            turtleA.setposition(x,y)
            turtleA.color("black")
            turtleA.pendown()
            turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
            turtleA.penup()
            y-=10
            circleNumber+=1
        for l in range(0,int(left)):
            x-=circleSpacing
            turtleA.setposition(x,y)
            circleType = checkFactors(circleNumber,circleSize)
            turtleA.color(circleType[0],circleType[1])
            turtleA.pendown()
            turtleA.begin_fill()
            turtleA.circle(circleType[2])
            turtleA.penup()
            turtleA.end_fill()
            y+=10
            turtleA.setposition(x,y)
            turtleA.color("black")
            turtleA.pendown()
            turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
            turtleA.penup()
            y-=10
            circleNumber+=1
        for d in range(0,int(down)):
            y-=circleSpacing
            turtleA.setposition(x,y)
            circleType = checkFactors(circleNumber,circleSize)
            turtleA.color(circleType[0],circleType[1])
            turtleA.pendown()
            turtleA.begin_fill()
            turtleA.circle(circleType[2])
            turtleA.penup()
            turtleA.end_fill()
            y+=10
            turtleA.setposition(x,y)
            turtleA.color("black")
            turtleA.pendown()
            turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
            turtleA.penup()
            y-=10
            circleNumber+=1
        if i == int(n)-1:
           for r in range(0,int(right)+1):
            x+=circleSpacing
            turtleA.setposition(x,y)
            circleType = checkFactors(circleNumber,circleSize)
            turtleA.color(circleType[0],circleType[1])
            turtleA.pendown()
            turtleA.begin_fill()
            turtleA.circle(circleType[2])
            turtleA.penup()
            turtleA.end_fill()
            y+=10
            turtleA.setposition(x,y)
            turtleA.color("black")
            turtleA.pendown()
            turtleA.write(circleNumber,False, align = "center", font=("Arial",10, "bold"))
            turtleA.penup()
            y-=10
            circleNumber+=1
           
        up+=2
        right+=2
        left+=2
        down+=2
    
        
window = turtle.Screen()
window.bgcolor("black")

ulam = turtle.Turtle()
ulam.speed(0)
ulam.pensize(2)
ulam.penup()
ulam.color("green","green")
ulam.shapesize(0.1,0.1,1)


draw(ulam)











