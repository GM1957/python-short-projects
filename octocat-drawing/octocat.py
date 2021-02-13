import turtle as t

def talloval(r):               
    t.left(45)
    for loop in range(2):      
        t.circle(r,90)    
        t.circle(r/2,90) 

def draw_head():
    t.penup()
    t.goto(10,20)
    t.pendown()
    t.speed(10)
    t.pensize(3)
    t.pencolor("black")
    t.fillcolor("black")

    t.begin_fill()

    t.forward(20)
    t.circle(160,30)
    t.seth(40)
    t.circle(130,20)
    t.seth(70)
    t.circle(130,20)
    t.seth(80)
    t.circle(100,10)
    t.seth(100)
    t.circle(130,30)

    #ear
    t.seth(60)
    t.circle(80,20)
    t.seth(80)
    t.circle(80,30)
    t.seth(-350)
    t.circle(-80,-40)
    t.seth(-310)
    t.circle(-100,-10)

    t.seth(-20)
    t.circle(-200,-40)
   
    #ear
    t.seth(100)
    t.circle(75,20)
    t.seth(120)
    t.circle(80,25)
    t.seth(-320)
    t.circle(-60,-70)

    t.seth(-320)
    t.circle(-120,-30)
    t.seth(-290)
    t.circle(-150,-20)
    t.seth(-260)
    t.circle(-160,-20)
    t.seth(-220)
    t.circle(-180,-15)
    t.seth(-200)
    t.circle(-180,-8)
    t.seth(-180)
    t.circle(-180,-5)
    t.seth(-180)
    t.forward(-20)
    t.seth(-185)
    t.forward(-50)

    t.end_fill()

def draw_face():
    t.penup()
    t.goto(20,50)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("#F4CAB1")
    t.fillcolor("#F4CAB1")

    t.begin_fill()
    
    t.seth(-180)
    t.forward(20)
    t.circle(-250,25)
    t.seth(-220)
    t.circle(-200,5)
    t.seth(-250)
    t.circle(-200,5)
    t.seth(-270)
    t.circle(-200,10)
    t.seth(-290)
    t.circle(-200,10)
    t.seth(-320)
    t.circle(-200,10)
    t.seth(-340)
    t.circle(-200,10)
    t.seth(-350)
    t.circle(-200,10)
    t.seth(-360)
    t.circle(-200,10)
    t.seth(-370)
    t.circle(-200,10)
    t.seth(-20)
    t.circle(-200,10)
    t.seth(-50)
    t.circle(-200,10)
    t.seth(-80)
    t.circle(-200,10)
    t.seth(-110)
    t.circle(-200,10)
    t.seth(-140)
    t.circle(-200,10)
    t.seth(-160)
    t.circle(-200,10)
    
    t.end_fill()

def draw_eyes():
    #left eye
    t.penup()
    t.goto(-80,150)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("white")
    t.fillcolor("white")

    t.begin_fill()
    
    talloval(30)
    
    t.end_fill()

     #inner right eye
    t.penup()
    t.goto(-56,118)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("#AC5C51")
    t.fillcolor("#AC5C51")

    t.begin_fill()

    t.seth(-350)
    talloval(20)

    t.end_fill()

    #right eye
    t.penup()
    t.goto(60,150)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("white")
    t.fillcolor("white")

    t.begin_fill()

    t.seth(-190)
    talloval(30)

    t.end_fill()

    #inner right eye
    t.penup()
    t.goto(62,142)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("#AC5C51")
    t.fillcolor("#AC5C51")

    t.begin_fill()

    t.seth(-190)
    talloval(20)

    t.end_fill()

    #nose
    t.penup()
    t.goto(0,105)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("#AC5C51")
    t.fillcolor("#AC5C51")

    t.begin_fill()

    t.seth(-190)
    t.circle(8)

    t.end_fill()

    #mouth
    t.penup()
    t.goto(12,80)
    t.pendown()
    t.speed(10)
    t.pensize(6)
    t.pencolor("#AC5C51")
    t.fillcolor("#AC5C51")

    t.seth(-95)
    t.circle(-15,180)

    #mustache
    t.penup()
    t.goto(268,80)
    t.pendown()
    t.speed(10)
    t.pensize(3)
    t.pencolor("black")
    t.fillcolor("black")

    t.seth(150)
    t.circle(220,40)

    t.penup()
    t.goto(268,110)
    t.pendown()

    t.seth(160)
    t.circle(220,40)


    t.penup()
    t.goto(-280,80)
    t.pendown()
    t.speed(10)
    t.pensize(3)
    t.pencolor("black")
    t.fillcolor("black")

    t.seth(-150)
    t.circle(220,-40)

    t.penup()
    t.goto(-280,110)
    t.pendown()

    t.seth(-160)
    t.circle(220,-40)

    

def draw_legs():
    t.penup()
    t.goto(-30,30)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("black")
    t.fillcolor("black")

    t.begin_fill()
    
    t.seth(-190)
    t.circle(60,80)
    t.seth(-110)
    t.circle(250,40)
    t.seth(110)
    t.circle(10,-30)
    t.seth(120)
    t.circle(20,-120)

    t.seth(-60)
    t.circle(20,120)
    
    t.seth(60)
    t.circle(150,40)
    
    t.seth(-70)
    t.circle(100,-60)

    t.seth(-265)
    t.forward(-30)
    t.seth(-265)
    t.forward(-20)

    t.seth(-270)
    t.forward(-100)

    t.seth(-280)
    t.forward(-20)

    t.seth(-290)
    t.forward(-20)

    t.seth(-120)
    t.circle(-200,12)

    t.seth(180)
    t.circle(-100,-10)
    t.seth(200)
    t.circle(-80,-30)
    t.seth(250)
    t.circle(-330,-30)

    t.seth(270)
    t.circle(330,-5)

    t.seth(180)
    t.forward(-5)

    t.seth(280)
    t.forward(20)

    t.seth(275)
    t.forward(80)

    t.seth(270)
    t.circle(280, 20)

    t.seth(300)
    t.circle(100, 30)

    t.seth(300)
    t.circle(100, -30)
    t.seth(280)
    t.circle(600, -17)

    t.seth(140)
    t.circle(50,-30)

    t.seth(120)
    t.circle(100,-30)

    t.seth(-110)
    t.circle(160,40)

    t.seth(-70)
    t.circle(30,70)

    t.circle(30,20)

    t.seth(150)
    t.circle(-50,30)

    t.seth(100)
    t.circle(-150,40)

    t.seth(80)
    t.circle(150,50)

    t.seth(-200)
    t.forward(30)

    t.seth(-177)
    t.forward(90)

    t.end_fill()

def draw_tail():
    t.penup()
    t.goto(-200,-5)
    t.pendown()
    t.speed(10)
    t.pensize(2)
    t.pencolor("black")
    t.fillcolor("black")

    t.begin_fill()
    t.circle(50,-70)
    t.circle(-80,-50)

    t.seth(-90)
    t.forward(30)

    t.seth(170)
    t.circle(-80,70)
    t.circle(50,60)

    t.end_fill()

    t.penup()
    t.goto(-180,-5)
    t.pendown()
    t.pencolor("#9CDAF0")
    t.fillcolor("#9CDAF0")

    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()

    t.goto(-160,-20)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()

    t.goto(-150,-45)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.penup()

    t.goto(-130,-70)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()

draw_head()
draw_face()
draw_eyes()
draw_legs()
draw_tail()

t.done()    