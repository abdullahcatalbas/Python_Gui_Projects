from graphics import *
import random 

def main():
    
    def gain(a):
        p=[]
        if 0 in a:
            if 3 in a:
                if 6 in a:
                    return 1
            elif 4 in a:
                if 8 in a:
                   return 1 
        if 1 in a:
             if 4 in a:
                 if 7 in a:
                     return 1
        if 2 in a:
            if 5 in a:
                if 8 in a:
                    return 1     
            elif 4 in a:
                if 6 in a:
                    return 1
        if 0 in a:
            if 1 in a:
                if 2 in a:
                    return 1
        if 3 in a:
            if 4 in a:
                if 5 in a:
                    return 1
        if 6 in a:
            if 7 in a:
                if 8 in a:
                    return 1


    win = GraphWin("18290089",300,350)
    
    rect = []
    for y in range(0,300,100):
       for x in range(0,300,100):
         
         rect.append(Rectangle(Point(x,y),Point(x+100,y+100)).draw(win)) 
         
         
    r=Rectangle(Point(0,300),Point(300,350)).draw(win)  
   
    butt=[]     
    com=[]
    key=0
    total=[]
    num=0
    out=Text(r.getCenter(),"").draw(win)
    while True:
      
      try:      
        cor=win.getMouse()
      except GraphicsError:
          break      
      try:
             
        x = cor.getX()
        y = cor.getY()
        for i in butt:
           if i not in total:               
               total.append(i)
        for i in com:
           if i not in total:               
               total.append(i)
        if y>0 and y <100 :
                             
           if x >0 and x <100:
             if 0 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[0].getCenter(),"X").draw(win)
             butt.append(0)
             
             if key==1:
                 out.setText("")
                 key=0
           elif x >100 and x <200:
             if 1 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[1].getCenter(),"X").draw(win)
             butt.append(1)
            
             if key==1:
                 out.setText("")
                 key=0
           elif x >200 and x <300:
             if 2 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[2].getCenter(),"X").draw(win) 
             butt.append(2)
         
             if key==1:
                 out.setText("")
                 key=0
        elif y>100 and y <200 :
                             
           if x >0 and x <100:
             if 3 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[3].getCenter(),"X").draw(win)
             butt.append(3)
       
             if key==1:
                 out.setText("")
                 key=0
           elif x >100 and x <200:
             if 4 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[4].getCenter(),"X").draw(win)
             butt.append(4)
           
             if key==1:
                 out.setText("")
                 key=0
           elif x >200 and x <300:
             if 5 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[5].getCenter(),"X").draw(win)      
             butt.append(5)
             
             if key==1:
                 out.setText("")
                 key=0
        elif y>200 and y <300:         
           
           if x >0 and x <100:
             if 6 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[6].getCenter(),"X").draw(win)
             butt.append(6)
             
             if key==1:
                 out.setText("")
                 key=0
           elif x >100 and x <200:
             if 7 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             mess=Text(rect[7].getCenter(),"X").draw(win)
             butt.append(7)
             
             if key==1:
                 out.setText("")
                 key=0
           elif x >200 and x<300:
             if 8 in total:
                 out.setText("You cannot click the filled squares!")
                 key=1
                 continue
             
             mess=Text(rect[8].getCenter(),"X").draw(win)
             butt.append(8)
        
             if key==1:
                 out.setText("")
                 key=0
        
        list1=[]  
        for i in range(9):
            if i not in butt:
                if i not in com:
                  list1.append(i)
                
        if list1!=[]:
           a=random.choice(list1)
           
           com.append(a)
       
        for i in range(9):
             if a==i:
              Text(rect[a].getCenter(),"O").draw(win)
            
        h=gain(butt)
        
        if h==1:
           out.setText("X wins")
           goal=1 
       
        if goal==1:
            c=win.getKey()
            if c=="q":
                break
        h1=gain(com)
        if h1==1:
            out.setText("O wins")
            goal=1
       
        s=len(total)
        if s==8:
            if goal==0:
             out.setText("Draw!")
             goal=1
              
        if goal==1:
            c=win.getKey()
            if c=="q":
                break
      except:
         continue
    
    win.close()
    
main()


