#   a123_apple_1.py
import turtle as trtl

import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()

turtles = [apple,apple1,apple2,apple3]

drawer = trtl.Turtle()

global alphabet
alphabet  = ['q','w','e','r']
#,'t','y','u','i','o','p']
global letter
letter = ""
global correct
correct = False
global pop
pop = ""
active = []
global number


drawer.hideturtle()
drawer.color("white")
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def key_presses():
  try:
    wn.onkeypress(drop_apple, alphabet[0])
  except Exception:
    a = "a"
  try:
    wn.onkeypress(drop_apple1, alphabet[1])
  except Exception:
    a = "a"
  try:
    wn.onkeypress(drop_apple2, alphabet[2])
  except Exception:
    a = "a"
  try:
    wn.onkeypress(drop_apple3, alphabet[3])
  except Exception:
    a = "a"  

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  move_apple(active_apple)
  active_apple.showturtle()
  active.append(active_apple)
  
  wn.update()

def move_apple(apple):
      apple.penup()
      apple.setposition(rand.randint(-150,150),rand.randint(-150,150))


def drop_apple():
  global letter
  global number
  for i in range (len(active)):
    if active[i] == apple:
      print(i)
      wn.onkeypress(None, alphabet[0])
      apple.showturtle()
      apple.penup()
      apple.setposition(apple.xcor(), (apple.ycor()-200))
      apple.hideturtle()
      wn.update()
      alphabet.pop(i)
      turtles.pop(i) 
      print (alphabet)
      active.pop(i)
      number = rand.randint(0,len(turtles)-1)

      draw_apple(turtles[number])

      letter = alphabet[number]
      print(letter)
      drawer.clear()
      wn.update()
      key_presses()
      


      

def drop_apple1():
  global letter
  global number
  for i in range (len(active)):
    if active[i] == apple1:
      print(i)
      wn.onkeypress(None, alphabet[1])
      
      apple1.showturtle()
      apple1.penup()
      apple1.setposition(apple1.xcor(), (apple1.ycor()-200))
      wn.update()
      apple.hideturtle()
      number = rand.randint(0,len(turtles)-1)
      draw_apple(turtles[number])
      letter = alphabet[number]
      alphabet.pop(i)
      turtles.pop(i)
      print (alphabet)
      active.pop(i)
      number = rand.randint(0,len(turtles)-1)

      draw_apple(turtles[number])
      drawer.clear()
      wn.update()
      letter = alphabet[number]
      print(letter)
      key_presses()



def drop_apple2():
  global letter
  global number
for i in range (len(active)):
    if active[i] == apple2:
      print(i)
      wn.onkeypress(None, alphabet[2])
      
      apple2.showturtle()
      apple2.penup()
      apple2.setposition(apple2.xcor(), (apple2.ycor()-200))
      wn.update()
      apple2.hideturtle()
      number = rand.randint(0,len(turtles)-1)
      draw_apple(turtles[number])
      letter = alphabet[number]
      alphabet.pop(i)
      turtles.pop(i) 
      print (alphabet)
      active.pop(i)
      number = rand.randint(0,len(turtles)-1)

      draw_apple(turtles[number])
      drawer.clear()
      wn.update()
      letter = alphabet[number]
      print(letter)
      key_presses()


def drop_apple3():
  global letter
  global number
  for i in range (len(active)):
    if active[i] == apple3:
      print(i)
      wn.onkeypress(None, alphabet[3])
      
      apple3.showturtle()
      apple3.penup()
      apple3.setposition(apple3.xcor(), (apple3.ycor()-200))
      wn.update()
      apple3.hideturtle()
      number = rand.randint(0,len(turtles)-1)
      draw_apple(turtles[number])
      letter = alphabet[number]
      alphabet.pop(i)
      turtles.pop(i)
      print (alphabet)
      active.pop(i)
      number = rand.randint(0,len(turtles)-1)

      draw_apple(turtles[number])
      drawer.clear()
      wn.update()
      letter = alphabet[number]
      print(letter)
      key_presses()
      wn.listen()


#-----function calls-----



number = rand.randint(0,len(turtles)-1)

draw_apple(turtles[number])

letter = alphabet[number]

drawer.write(letter, font=("Arial",74, "bold")) 

print (alphabet)
print (active)

key_presses()

wn.listen()
print (alphabet)
print(active)


wn.mainloop()
