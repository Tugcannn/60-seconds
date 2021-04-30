import turtle, random , time

def score(x, y) :
    global p
    p = p + 1
    board.clear()
    board.write('Score: {}'.format(p), align = 'center', font = ('Courier', 24, 'normal'))
    ball.goto(random.randint(-297, 297), random.randint(-297, 297))


window = turtle.Screen()
window.title('Mouse Click')
window.bgcolor('lightgrey')
window.setup(width=600 , height=600)


ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.shapesize(2)
ball.penup()
ball.goto(random.randint(-297, 297) , random.randint(-297, 297))

p = 0
board = turtle.Turtle()
board.speed(0)
board.color('white')
board.penup()
board.goto(0,260)
board.write('Start' , align= 'center' , font=('Courier', 24,'normal'))


count = 60
while True :
      start_time = time.time()
      while (time.time() - start_time) < count :
             ball.onclick(score)
      else:
          board.clear()
          board.write('Score: {}'.format(p), align='center', font=('Courier', 24, 'normal'))
          time.sleep(2)
          p = 0
          board.clear()
          board.write('Start',  align='center', font=('Courier', 24, 'normal'))


