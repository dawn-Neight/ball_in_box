import math
import random


__all__ = ['ball_in_box']

def ball_in_box(m, blockers):
    k=0
    max=0
    circles = []
    BalloonR=[0]*int(m)                                     #生成m个球的x，y，r的列表信息
    BalloonXPos=[0]*int(m)
    BalloonYPos=[0]*int(m)
    mBalloonR=[0]*int(m)                                    #记录最大球的x，y，r的列表信息
    mBalloonXPos=[0]*int(m)
    mBalloonYPos=[0]*int(m)
    while k<50000:                                          #随机生成点，循环5w次，找出最大的半径平方和
        sum=0
        BalloonR=[0]*int(m)                                 
        for j in range(0,int(m)):
            r=0
            BalloonXPos[j]=random.random()*2-1
            BalloonYPos[j]=random.random()*2-1
            i=0
            while(i<j):                                    #第一次随机生成点，之后的点不能生成在第一个圆内，如果在圆内重新生成，知道在圆外
                if(math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]>0):
                    i=i+1
                else:
                    i=0
                    BalloonXPos[j]=random.random()*2-1
                    BalloonYPos[j]=random.random()*2-1
                    continue
    
            r=math.fabs(1-BalloonXPos[j])                  #找出圆半径的方法是寻找一个点能达到的最大半径，基本思路是：使一个圆膨胀，知道碰到界外
            if(math.fabs(1-BalloonYPos[j])<r):              #或者其他障碍物或者圆，找出距离这些障碍物的最短的，就是能够达到的最大半径
                r=math.fabs(1-BalloonYPos[j])               #进行m次，分别找出这些点的最大圆
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
