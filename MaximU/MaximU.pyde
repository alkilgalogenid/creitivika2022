x=198
r=177
y=14
t=100
u=100
g=200
h=700
k=185
m=220
j=5
o=20
v=20
z=720
n=680
q=20
w=40
i=50
p=210
ss=0
def setup():    
    size(1000,1000)
    background(210,214,13)
def draw():
    global x, y, r,t,u,h,g,v,m,n,k,j,o,z,q,w,i,p,ss
    push()
    fill(x,r,y)
    rect(0,0,425,1000)
    pop()
    rect(100,300,100,100)
    rect(300,300,100,100)
def mouseClicked():
    global x, y ,r,t,u,g,h,v,m,n,k,j,o,z,q,w,i,p,ss
    if mouseX>100 and mouseX<200 and mouseY>300 and mouseY<400 :
        background(0)
        fill(39,38,34)
        push()
        x=118
        r=113
        y=67
        pop()
    if mouseX>300 and mouseX<400 and mouseY>300 and mouseY<400 :
        background(210,214,13)
        x=198
        r=177
        y=14
        fill(x,r,y)
        rect(0,0,425,1000)
        fill(255)
        ellipse(h,g,t,t)
        fill(0)
        ellipse(h+t/5,g-t/6,t/5,t/5)
        ellipse(h-t/5,g-t/6,t/5,t/5)
        push()
        rectMode(CENTER)
        rect(700,g+t/10,t/2,t/5)
        pop()
        ellipse(700,g+t/5,t/2,t/4)
        fill(255)
        ellipse(h+t/5,g-t/6,t/20,t/20)
        ellipse(h-t/5,g-t/6,t/20,t/20)
        g=g+100
        t=t+50
        ss=ss+1
        if ss>3 :
            background(0)
