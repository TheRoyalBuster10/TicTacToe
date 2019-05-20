import random
matrix=[[1,1,1],[1,1,1],[1,1,1]]
pos=t=p=q=0
counter=0
def diagnol():
    c=d=l=m=x_coordinate=i=j=a=b=u=k=0
    for x_coordinate in range(3):
        
        if matrix[x_coordinate][x_coordinate]==0:
            c+=1
        if matrix[x_coordinate][x_coordinate]==2:
            d+=1
        if matrix[x_coordinate][x_coordinate]==1:
            a=b=x_coordinate
    j=2
    for i in range(3):
        if matrix[i][j]==0:
            l+=1
        if matrix[i][j]==2:
            m+=1
        if matrix[i][j]==1:
            u=i
            k=j
        j-=1
    if c==2 and matrix[a][b]==1:
        return a,b,0
    if l==2 and matrix[a][b]==1:
        return u,k,0
    if d==2 and matrix[a][b]==1:
        return a,b,2    
    if m==2 and matrix[a][b]==1:
        return u,k,2
    down=0
    for p in range(3):
        for q in range(3):
            if matrix[p][q]==1:
                down = down+1
    if down == 0:
        return 6,6,6
    return 5,5,5

def horizontal():
    c=d=x_coordinate=y_coordinate=a=b=0
    for x_coordinate in range(3):
        a=b=c=d=0
        for y_coordinate in range(3):
            if matrix[x_coordinate][y_coordinate]==0:
                c+=1
            if matrix[x_coordinate][y_coordinate]==2:
                d+=1
            if matrix[x_coordinate][y_coordinate]==1:
                a=x_coordinate
                b=y_coordinate
        if c==2 and matrix[a][b]==1:
            return a,b,0
        if d==2 and matrix[a][b]==1:
            return a,b,2
    return 5,5,5
def vertical():
    y_coordinate=a=b=c=d=0
    for y_coordinate in range(3):
        a=b=c=d=0
        for x_coordinate in range(3):
            if matrix[x_coordinate][y_coordinate]==0:
                c+=1
            if matrix[x_coordinate][y_coordinate]==2:
                d+=1
            if matrix[x_coordinate][y_coordinate]==1:
                a=x_coordinate
                b=y_coordinate
        if c==2 and matrix[a][b]==1:
            return a,b,0
        if d==2 and matrix[a][b]==1:
            return a,b,2
    return 5,5,5
def is_over():
    x_coordinate=y_coordinate=t=r=i=j=0
    if (matrix[x_coordinate][y_coordinate]==matrix[x_coordinate+1][y_coordinate+1] and matrix[x_coordinate+1][y_coordinate+1]==matrix[x_coordinate+2][y_coordinate+2]):
        if matrix[x_coordinate][y_coordinate]==0:
            return 0
        if matrix[x_coordinate][y_coordinate]==2:
            return 2
    if (matrix[x_coordinate][y_coordinate+2]==matrix[x_coordinate+1][y_coordinate+1] and matrix[x_coordinate+1][y_coordinate+1]==matrix[x_coordinate+2][y_coordinate]):
        if matrix[x_coordinate][y_coordinate+2]==0:
            return 0
        if matrix[x_coordinate][y_coordinate+2]==2:
            return 2
    for i in range(3):
        if (matrix[i][j]==matrix[i][j+1] and matrix[i][j+1]==matrix[i][j+2]):
            if matrix[i][j]==0:
                return 0
            if matrix[i][j]==2:
                return 2
    for t in range(3):
        if (matrix[r][t]==matrix[r+1][t] and matrix[r+1][t]==matrix[r+2][t]):
            if matrix[r][t]==0:
                return 0
            if matrix[i][j]==2:
                return 2
    return 3
def computer():
    loop=0
    y_coordinate=x_coordinate=pos=0
    while loop==0:
        pos=random.randint(1,10)
        for x_coordinate in range(3):
            y_coordinate =pos-1-3*x_coordinate
            if y_coordinate>=0 and y_coordinate<3:
                if matrix[x_coordinate][y_coordinate]==1:
                    return x_coordinate,y_coordinate
    return 3
def draw():
    e=f=c=0
    for e in range(3):
        for f in range(3):
            if matrix[e][f]==1:
                c=c+1
    if (c==0):
        return 1
    else:
        return 3
def array_print(case=1):
    for i in range(3):
        if case==2:
            print (end="             ")
        for j in range(3):
            if matrix[i][j]==2:
                print ('x',end="   "),
            elif matrix[i][j]==0:
                print ('o',end="   "),
            else:
                print ('-',end="   "),
        print ('\n')
def toss():
    x=y=pos=0
    turn=random.randint(1,11)
    if turn%2==0:
        array_print(1)
        pos=int(input('Enter the position'))
        x=0
        y=0
        for x in range(3):
            y =pos-1-3*x
            if y>=0 and y<3:
               matrix[x][y]=2
               array_print(1)
               return 1
    else:
        e=f=0
        e,f=computer()
        if(e<3 and f<3):
            if (matrix[e][f]!=2 and matrix[e][f]!=0):
                matrix[e][f]=0
                array_print(2)
                return 2
case=1
a=0
while(is_over()==3 and draw()!=1):
    if(a==0):
        t=toss()
    if (t!=1):
        if (t!=2):
            array_print(case)
        pos=int(input('Enter the position'))
        for x_coordinate in range(3):
            y_coordinate=pos-1-3*x_coordinate
            if y_coordinate>=0 and y_coordinate<3:
                    matrix[x_coordinate][y_coordinate]=2
                    case=1
                    array_print()
                    
    a+=4
    t+=5
    e=f=g=0
    e,f,g=diagnol()
    if (e==6 and f==6 and g==6):
        continue
    if (e<3 and f<3 and g<3):
        if (matrix[e][f]!=2 and matrix[e][f]!=0):
            matrix[e][f]=0
            case=2
            continue
    e=f=g=0
    e,f,g=horizontal()
    if(e<3 and f<3 and g<3):
        if (matrix[e][f]!=2 and matrix[e][f]!=0):
            matrix[e][f]=0
            case=2
            continue
    e=f=g=0
    e,f,g=vertical()
    if(e<3 and f<3 and g<3):
        if (matrix[e][f]!=2 and matrix[e][f]!=0):
            matrix[e][f]=0
            case=2
            continue
    e=f=0
    e,f=computer()
    if(e<3 and f<3):
        if (matrix[e][f]!=2 and matrix[e][f]!=0):
            matrix[e][f]=0
            case=2
            continue    
if (is_over()==0):
    array_print(2)
    print('Computer WINS')
elif (is_over()==2):
    array_print(2)
    print('You WIN')
elif (draw()==1):
    array_print(2)
    print('Match DRAW')

        
       
    
    
            
        
        
            
        
            
