from graphics import *
import random
import math

# Do not change these following 4 variables
margin = 10 # height of the paddle from the ground
moveIncrement = 15 # paddle movement
ballRadius = 15
BOUNCE_WAIT= 1200 
    
BALL_COUNT = 1 # If we change this, the number of ball changes!


class Timer:
    def __init__(self):
        self.value = 0

class Paddle:

    def __init__(self, color, width, height, coordx, win):
        self.color = color
        self.width = width
        self.height = height
        self.x = coordx
        self.shape = Rectangle(Point(self.x - int(self.width / 2), win.getHeight() - margin - self.height),
                               Point(self.x + int(self.width / 2), win.getHeight() - margin))
        self.shape.setFill(self.color)
        self.window = win
        self.shape.draw(self.window)

    def move_left(self):   # move paddle to the left by the amount of global variable moveIncrement
        # TODO: control that it does not exceed the window
        if self.x>=50 and self.x<=255:
          self.x -= moveIncrement
          self.shape.move(-moveIncrement, 0)

    def move_right(self):  # move paddle to the right by the amount of global variable moveIncrement
        # TODO: control that it does not exceed the window
        if self.x>=25 and self.x<=250:
          self.x += moveIncrement
          self.shape.move(moveIncrement, 0)
    def move_paddle(self):
        if self.x>=150:            
          self.shape.move(150-self.x,0)
        if self.x<150:
            self.shape.move(150-self.x,0)
        self.x=150 
    def delete_paddle(self):
        self.shape.undraw()
        
# TODO
class Bubbles(): 
    # Define it by yourself to implement bubbles in the assignment
    def __init__(self,win):
        self.bubbles=[]
        self.del_bubbles=[]
        self.window=win
              
    def create_bubbles(self):
        for y in range(30,180,60):
            for x in range(30,300,60):
              self.bubbles.append(Circle(Point(x,y),30))
        
        for i in range(len(self.bubbles)):
            
            self.bubbles[i].draw(self.window)
            if i<5:
               self.bubbles[i].setFill("green")
            if i>4 and i<10:
                self.bubbles[i].setFill("blue")
            if i>=10:
                self.bubbles[i].setFill("red")
               
    def delete_bubbles(self,a):
         if a=="yes":
             for i in range(len(self.bubbles)):
                self.bubbles[i].undraw()
             self.bubbles=[]
             self.del_bubbles=[]
             
         for i in range(len(self.bubbles)):
           r1=45
           p1=self.bubbles[i].getCenter()
           x=p1.getX()
           y=p1.getY()        
           p2=a.getCenter()
           x1=p2.getX()
           y1=p2.getY()
           d=(x1-x)**2 + (y1-y)**2
           s=math.sqrt(d)          
           if r1>=s:             
              self.bubbles[i].undraw()
              if i not in self.del_bubbles:               
                self.del_bubbles.append(i)
    def game_overr(self):        
         if len(self.del_bubbles)==15:
             return 1
         else:
             return 0
  
class Ball:

    def __init__(self, coordx, coordy, color, radius, x_direction, speed, win):
        self.shape = Circle(Point(coordx, coordy), radius)
        self.x = coordx
        self.y = coordy
        self.xMovement = 0 # Current x movement
        self.yMovement = 0 # Current y movement
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius
        self.timer = 0
        self.x_direction = x_direction   # Initial x direction. This variable will be 0 or 1. 1:right 0:left
        self.speed = speed
        self.count=1
               
    def get_value(self):      
        return self.shape
        
    def is_moving(self):   
        # TODO: It returns true if ball is moving
        if self.xMovement!=-0:
            return True
        return False

    def bounce(self, gameTimer, minX, maxX, maxY):
        # Calculating x-axis ball movement and bouncing
        # minX: min x coord. of paddle
        # maxX: max x coord. of paddle
        # maxY: max y coord. at which the ball can be move. If it goes further, it falls to the ground.
        
        global BOUNCE_WAIT
        gameOver = False

        if gameTimer >= self.timer + BOUNCE_WAIT:
            self.timer = gameTimer
              
            m=self.shape.getCenter()
            x=m.getX()
            y=m.getY()
            
            dis1=self.shape.getP1()
            dis2=self.shape.getP2()
           
            x1=dis1.getX()
            y1=dis1.getY()
            x2=dis2.getX()
            y2=dis2.getY()
                       
            if x1-self.speed<0:
                self.sped=x1              
                self.shape.move(self.xMovement * self.sped,self.yMovement *self.sped)
             
                
            if x2+self.speed>300:
                self.sped=300-x2
                self.shape.move(self.xMovement *self.sped, self.yMovement * self.sped)
                key=1 
            if y1-self.speed<0:
                self.sped=y1
                self.shape.move(self.xMovement *self.sped, self.yMovement * self.sped)
             
            if y2+self.speed>=575:
                self.sped=575-y2
                self.shape.move(self.xMovement * self.sped, self.yMovement * self.sped)             
                if self.xMovement !=0:
                 if x>=minX and x<=maxX:
                   self.yMovement=-1
                 self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
                   
            if y2>=600:
                self.count=self.count -1
                gameOver=True    
                
            dis1=self.shape.getP1()
            dis2=self.shape.getP2()
            x1=dis1.getX()
            y1=dis1.getY()
            x2=dis2.getX()
            y2=dis2.getY()   
            if x1==0 :              
              self.xMovement=1  
            if x2==300 :
               self.xMovement=-1
            if y1==0:
                self.yMovement=1 
                
            if self.xMovement == 1:
                self.x += self.speed
            elif self.xMovement == -1:
                self.x -= self.speed
                
            if self.yMovement==1:
                self.y -=self.speed
            
            self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
             
            return gameOver
        
    def counter_lives(self):
            if self.count==0:
                return 1
            else:
                self.count=1
                return 0
            
    def delete_ball(self):
       self.shape.undraw()  
       

def main():
    win = GraphWin("18290089 Pong Game", 300, 600) # Replace your student id
    lives = 2
    win.setBackground("Black")
    myPaddle = Paddle("White", 100, 15, 150, win)
    
    ColorsList = ["Cyan","Red","Green","Yellow"]   
    BallList = list()
    for i in range(BALL_COUNT):
        rand_speed = random.randint(5,20) # random speed for ball
        # Note that the speed of the balls may vary depending on the hardware. If it is too fast or too slow, you can change the speed range for yourself while testing.
        # However, if you change these range, do not forget to reset these values to the initial limits before sending us.
        
        rand_direction = random.randint(0, 1) # This variable will be 0 or 1 randomly.
        ball = Ball(myPaddle.x - int(myPaddle.width/2) + i*30, win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i%4] , ballRadius,rand_direction,rand_speed, win)
        BallList.append(ball) 
 
    bubble=Bubbles(win)
    bubble.create_bubbles()
    
    livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- {lives}')
    livesCounter.setTextColor("Cyan")
    livesCounter.setSize(15)
    livesCounter.draw(win)
    gameTimer = Timer()
    game__over=False
    gameOver = False
    see=0
    try:
      while lives > 0:
      
        while not gameOver:
            if see==1:
               
               myPaddle.move_paddle()
               BallList=list()
               bubble.delete_bubbles("yes")
               bubble=Bubbles(win)
               bubble.create_bubbles()
               
               for i in range(BALL_COUNT):
                
                 rand_speed = random.randint(5,20) # random speed for ball  
                 rand_direction = random.randint(0, 1) # This variable will be 0 or 1 randomly.
                 ball = Ball(myPaddle.x - int(myPaddle.width/2) + i*30, win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i%4] , ballRadius,rand_direction,rand_speed, win)
                 BallList.append(ball)                 
               see=0
                 
            keyPress = win.checkKey()
            if keyPress == 'a': 
                myPaddle.move_left()
                
            if keyPress == 'd':
                myPaddle.move_right()
                
            if keyPress == 'l': # balls will move faster
                for item in BallList:
                    item.speed += 1  
                    
            if keyPress == 'k':  # Balls will move slower. Note that in our case min speed is 2.
                for item in BallList:
                    if item.speed > 2:
                        item.speed -= 1

            if keyPress == 's':  # Initial movement of balls
                for item in BallList:
                    if(not item.is_moving()):
                        if item.x_direction == 1:   # it means ball moves to right in x direction
                              item.xMovement = 1   
                        else:                   # it means ball moves to left in x direction
                            item.xMovement = -1
                        item.yMovement = -1 # at initial ball moves up in y direction

            
            gameTimer.value += 1        
            for item in BallList:
                
                gameOver = item.bounce(gameTimer.value,(myPaddle.x-int(myPaddle.width/2)), (myPaddle.x+int(myPaddle.width/2)), win.getHeight() - margin - myPaddle.height)
                a=item.get_value()
                bubble.delete_bubbles(a)
                result=item.counter_lives()
                end=bubble.game_overr()
                if result ==1:
                    lives -=1
                    livesCounter.setText(f'Lives -- {lives}')
                    see=1
                if end==1:
                   game__over=True
                   
                if gameOver == True:
                    break   
                  
                if game__over == True:               
                 for i in BallList:
                   i.delete_ball()
                 myPaddle.delete_paddle()
                 bubble.delete_bubbles("yes")
                 mess=[]
                 mess.append(Text(Point(150,300),"GAME OVER"))
                 mess.append(Text(Point(150,330),"YOU WİN"))    
                 mess.append(Text(Point(150,360),"Press Any Key to Quit"))
                 for i in range(3):
                   mess[i].setSize(15)
                   mess[i].setTextColor("red")
                   mess[i].draw(win)
                 while True:
        
                   key=win.checkKey()
                   if key !="":
                     break
                 win.close()
                 break             
                 
                  
                
        
        see=1
        gameOver=False
        for w in BallList:
            w.delete_ball()
        if game__over == True:                      
          break
    except GraphicsError:
        pass
    if lives==0:
     for i in BallList:
       i.delete_ball()
     myPaddle.delete_paddle()
     bubble.delete_bubbles("yes")
     mess=[]
     mess.append(Text(Point(150,300),"GAME OVER"))
     
     mess.append(Text(Point(150,330),"YOU LOST!"))
     mess.append(Text(Point(150,360),"Press Any Key to Quit"))
     for i in range(3):
       mess[i].setSize(15)
       mess[i].setTextColor("red")
       mess[i].draw(win)
     while True:
        
      key=win.checkKey()
      if key !="":
         break  
     win.close()
 
      
main()




