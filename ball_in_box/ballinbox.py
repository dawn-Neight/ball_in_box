import random 
import math
#blocks can be concentrated into points
#the area of this problem is [-1,1],[-1,1]


def ball_in_box(m, blockers):
    BalloonXPos=[0]*m
    BalloonYPos=[0]*m
    BalloonR=[0]*m
    r=0
    def ifin(pos):
        out=0
        for i in range(0,5):
            out=math.sqrt((pos[0]-BalloonXPos[i])**2+(pos[1]-BalloonYPos[i])**2)-BalloonR[i]>0
            if(out==0):
                break
        return out
    map=[(0,0)]*10000
    point=len(map)
    print(point)
    for i in range(1,101):
        for j in range(1,101):
            map[(i-1)*100+j-1]=(0.02*j-1,0.02*i-1)
    for j in range(0,m):
        for k in range(0,point):
            r=math.fabs(1-map[k][0])
            if(math.fabs(1-map[k][1])<r):
                r=math.fabs(1-map[k][1])
            if(math.fabs(-1-map[k][0])<r):
                r=math.fabs(-1-map[k][0])
            if(math.fabs(-1-map[k][1])<r):
                r=math.fabs(-1-map[k][1])
            for b in range(0,len(blockers)):
                if(math.sqrt((map[k][0]-blockers[b][0])**2+(map[k][1]-blockers[b][1])**2)<r):
                    r=math.sqrt((map[k][0]-blockers[b][0])**2+(map[k][1]-blockers[b][1])**2)
            for i in range(0,j):
                if(math.sqrt((map[k][0]-BalloonXPos[i])**2+(map[k][1]-BalloonYPos[i])**2)-BalloonR[i]<r):
                    r=math.sqrt((map[k][0]-BalloonXPos[i])**2+(map[k][1]-BalloonYPos[i])**2)-BalloonR[i]
            if(r>BalloonR[j]):
                BalloonR[j]=r
                BalloonXPos[j]=map[k][0]
                BalloonYPos[j]=map[k][1]
        map=list(filter(ifin,map))
        point=len(map)
    circles = []
    for circle_index in range(m):
        x = BalloonXPos[circle_index]
        y = BalloonYPos[circle_index]
        r = BalloonR[circle_index]
        circles.append((x, y, r))
        
    
    return circles


