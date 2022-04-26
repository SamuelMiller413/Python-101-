import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(10):
    painter.forward(50)
    painter.left(198) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()


# from turtle import * 
# from random import randint 
# bgcolor('black') 
# x = 1 
# speed(0) 
# while x < 100: 
  
#  r = randint(0,255) 
#  g = randint(0,255)  
#  b = randint(0,255) 
  
#  colormode(255)  
#  pencolor(r,g,b) 
#  fd(.5 + x) 
#  rt(90) 
#  x = x+1

# while x >= 50 and x < 150: 
  
#  r = randint(0,255) 
#  g = randint(0,255)  
#  b = randint(0,255) 
  
#  colormode(255)  
#  pencolor(r,g,b) 
#  fd(.5 + x) 
#  rt(90.091) 
#  x = x+1

# while x >= 100 and x < 200: 
  
#  r = randint(0,255) 
#  g = randint(0,255)  
#  b = randint(0,255) 
  
#  colormode(255)  
#  pencolor(r,g,b) 
#  fd(.5 + x) 
#  rt(90) 
#  x = x+1

# while x >= 150 and x < 300: 
  
#  r = randint(0,100) 
#  g = randint(0,100)  
#  b = randint(0,255) 
  
#  colormode(255)  
#  pencolor(r,g,b) 
#  fd(.5 + x) 
#  rt(90.91) 
#  x = x+1

# while x >= 150 and x < 800: 
  
#  r = randint(0,255) 
#  g = randint(0,255)  
#  b = randint(0,255) 
  
#  colormode(255)  
#  pencolor(r,g,b) 
#  fd(.5 + x) 
#  rt(45) 
#  x = x+1
 
# exitonclick() 