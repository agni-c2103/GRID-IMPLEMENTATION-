from graphics import *

def main():
    win = GraphWin("Rectangular Grid", 700, 700)
    win.setCoords(0.0,0.0,100.0,100.0)
    win.setBackground("white")
    #draw x axes
    for i in range (0,101):
      lx=Line(Point(0,i),Point(100,i))
      lx.draw(win)
      lx.setFill("green")
    #draw y axes
    for j in range (0,101):
      ly=Line(Point(j,0),Point(j,100))
      ly.draw(win)
      ly.setFill("green")

    ox =Line(Point(50,0),Point(50,100))
    oy =Line(Point(0,50),Point(100,50))
    ox.draw(win)
    oy.draw(win)
    ox.setFill("red")
    oy.setFill("red")
    pix=Rectangle(Point(0,0),Point(1,1))
    coords=Text(Point(0,0),"")
    while(1):
        click=win.getMouse()
        pix.undraw()
        coords.undraw()
        xv=int(click.getX())
        yv=int(click.getY())
        pix=Rectangle((Point(xv,yv)),Point((xv+1),(yv+1)))
        pix.draw(win)
        pix.setFill("blue")
        pix.setOutline("blue")
        xv1=str(xv-50)
        yv1=str(yv-50)
        cd = "( "+xv1+','+yv1+" )"
        #coords=Text(Point(0,0),"")
        if(20<xv<80 and 20 <yv<80):
            coords= Text(Point(xv+3,yv+3),cd)
        elif(xv<20):
            coords= Text(Point(xv+5,yv-3),cd)
        elif(xv>80):
            coords= Text(Point(xv-3,yv-3),cd)
        elif(yv<20):
            coords= Text(Point(xv-3,yv+3),cd)
        elif(yv>80):
            coords= Text(Point(xv-3,yv-3),cd)
            
        coords.draw(win)
        coords.setFace("helvetica")
        coords.setFill('red')
        
    
   # win.close()    

main()
