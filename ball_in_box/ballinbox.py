import math
import random


__all__ = ['ball_in_box']
# m stands for the number of the balloons while blockers stands for the position of the barricades.
def ball_in_box(m, blockers):
    k=0
    max=0
    circles = []
    #circles is a list which is made up of the "coordinate"---(posX,posY,radius)
    #initializing arrays whose length is changeable
    BalloonR=[0]*int(m)
    BalloonXPos=[0]*int(m)
    BalloonYPos=[0]*int(m)
    mBalloonR=[0]*int(m)
    mBalloonXPos=[0]*int(m)
    mBalloonYPos=[0]*int(m)
    while k<50000:
        sum=0
        
        BalloonR=[0]*int(m)
        for j in range(0,int(m)):
            r=0
            #randomly appoint a number which ranges from -1 to 1
            BalloonXPos[j]=random.random()*2-1
            BalloonYPos[j]=random.random()*2-1
            i=0
            while(i<j):
                if(math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]>0):
                    i=i+1
                else:
                    i=0
                    BalloonXPos[j]=random.random()*2-1
                    BalloonYPos[j]=random.random()*2-1
                    continue
    #use mathematical methods to judge whether the circles overlap
            r=math.fabs(1-BalloonXPos[j])
            if(math.fabs(1-BalloonYPos[j])<r):
                r=math.fabs(1-BalloonYPos[j])
            if(math.fabs(-1-BalloonXPos[j])<r):
                r=math.fabs(-1-BalloonXPos[j])
            if(math.fabs(-1-BalloonYPos[j])<r):
                r=math.fabs(-1-BalloonYPos[j])
            if(math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]-0.5)**2)<r):
                r=math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]-0.5)**2)
            if(math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]+0.3)**2)<r):
                r=math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]+0.3)**2)
            for i in range(0,j):
                if(math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]<r):
                    r=math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]
            BalloonR[j]=r
            sum=sum+BalloonR[j]**2
        if(sum>max):
            for x in range(m):
                mBalloonXPos[x]=BalloonXPos[x]
                mBalloonYPos[x]=BalloonYPos[x]
                mBalloonR[x]=BalloonR[x]  
            max=sum
        k=k+1
    for circle_index in range(m):

        x = mBalloonXPos[circle_index]
        y = mBalloonYPos[circle_index]
        r = mBalloonR[circle_index]
        circles.append((x, y, r))
        
    
    return circles
