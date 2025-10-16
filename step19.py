import turtle as trtl 

painter = trtl.Turtle() 
painter.speed(0)
painter.pensize(5)

x = -250  
y = -150 

num_floors = 63 

for floor in range(num_floors): 
  
  if floor % 21 == 0: 
    x = x + 100
    y = -150
    
  painter.penup()
  painter.goto(x, y)

  if floor % 6 > 2:
    painter.color("blue")
  else:
    painter.color("gray")
 
  y = y + 5 

  painter.pendown()
  painter.forward(50)

window = trtl.Screen()
window.mainloop()
