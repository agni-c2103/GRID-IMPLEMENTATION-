from graphics import *
import numpy as np

win = GraphWin("Rectangular Grid", 700, 700)
Img = Image(Point(0,0),"doc.gif")
w=Img.getWidth()
h=Img.getWidth()
    

def write_image():
    f=open('image_data.txt','w')
    
    for i in range(0,w):
        for j in range (0,h):
            color=Img.getPixel(i,j)
            r=str(color[0])
            g=str(color[1])
            b=str(color[2])
            string=""
            string=string+r+","+g+","+b+"\n"
            f.write(string)


def read_image():
    f=open('image_data.txt','r')
    line=[]
    line=f.readlines()
    l=0
    for i in range(0,w+1):
        for j in range(0,h+1):
            col = line[l].split(",")
            r=int(col[0])
            g=int(col[1])
            b= int(col[2].rstrip())
            l=l+1
            obj = Rectangle(Point(i,j),Point(i+1,j+1))
            obj.setFill(color_rgb(r,g,b))
            obj.setOutline(color_rgb(r,g,b))
            obj.draw(win)
        
    
        
        
            
            
    
    

def main():
    
    win.setCoords(0.0,0.0,w,h)
    win.setBackground("white")
    #draw x axes
    for i in range (0,w+1):
      lx=Line(Point(0,i),Point(w,i))
      lx.draw(win)
      lx.setFill("green")
      lx.setWidth(0.1)
    #draw y axes
    for j in range (0,h+1):
      ly=Line(Point(j,0),Point(j,h))
      ly.draw(win)
      ly.setFill("green")
      ly.setWidth(0.1)

    ox =Line(Point(w/2,0),Point(w/2,w))
    oy =Line(Point(0,h/2),Point(h,h/2))
    ox.draw(win)
    oy.draw(win)
    ox.setFill("red")
    oy.setFill("red")
    write_image()
    read_image()
   # win.close()    

main()
#read_image()
