#draw grid
Grid = [['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]





#arrange board
def int_Grid():
    
    global Grid
    power=['R','H','B','Q','K','B','H','R']

    for i in range(8) :
        Grid[0][i] = 'B'+power[i]

    for i in range(8) :
        Grid[-1][i] = 'W'+power[i]

    for i in range(8) :
        Grid[1][i] = 'BP'

    for i in range(8) :
        Grid[-2][i] = 'WP'





#print grind in 8x8 form
def print_grid():
    global Grid
    for i in Grid:
        print (i)





#to check wheather the pices is moving stright
def ner():
    global ix,iy,fx,fy
    if ix == fx and iy != fy :
        return True
    elif ix != fx and iy == fy :
        return True
    else:
        return False
#to check wheather the pices is moving cross
def kon():
    global ix,iy,fx,fy
    if a == b :
        print('True-kon')
        return True
    elif c == b:
        print('True-kon')
        return True  
    elif c == d :
        print('True-kon')
        return True
    elif a == d :
        print('True-kon')
        return True
    else:
        print('False-kon')
        return False
#to check wheather the pices is moving l-Shaped  
def kud():
    global ix,iy,fx,fy
    if a == 1 and b == 2:
        print('True-kud-1')
        return True
    elif c == 1 and b == 2:
        print('True-kud-2')
        return True
    elif a == 2 and b == 1:
        print('True-kud-3')
        return True
    elif c == 1 and d == 2:
        print('True-kud-4')
        return True
    elif c == 2 and d == 1:
        print('True-kud-5')
        return True
    elif a == 1 and d == 2:
        print('True-kud-6')
        return True
    elif c == 2 and d == 1:
        print('True-kud-7')
        return True
    elif a == 2 and b == 1:
        print('True-kud-8')
        return True        
    else:
        print('False-kud')
        return False
#to check pawn move
def kal():
    global a,b,c,d
    if d == 1 and c == 0 and Grid[iy][ix][0] == 'B':
       print('True-kal-1')
       return True
    elif d == 2 and c == 0 and Grid[iy][ix][0] == 'B':
        print('True-kal-2')
        return True
    elif b == 1 and c == 0 and Grid[iy][ix][0] == 'W':
       print('True-kal-1')
       return True
    elif b == 2 and c == 0 and Grid[iy][ix][0] == 'W':
        print('True-kal-2')
        return True
    else:
        print('False-kal')
        return False
#to check king move
def raj():
    global a,b,c,d
    if a == 1 and b == 0:
        print('True-raj-1')
        return True
    elif c == 1 and b == 0:
        print('True-raj-2')
        return True
    elif a == 0 and b == 1:
        print('True-raj-3')
        return True
    elif c == 1 and d == 0:
        print('True-raj-4')
        return True
    elif c == 0 and d == 1:
        print('True-raj-5')
        return True
    elif a == 1 and d == 0:
        print('True-raj-6')
        return True
    elif c == 0 and d == 1:
        print('True-raj-7')
        return True
    elif a == 0 and b == 1:
        print('True-raj-8')
        return True        
    else:
        print('False-raj')
        return False    




#checks if rook is choosen
def Rook():
    
    if Grid[iy][ix][1] == 'R' and ner():
        print('True-Rook')
        return True
    else :
        print('False-Rook')
        return False
#checks if bishope is choosen    
def Bishop():
    if Grid[iy][ix][1] == 'B' and kon():
        print('True-Bishop')
        return True
    else :
        print('False-Bishop')
        return False
#checks if knight is choosen
def Horse():
    
    if Grid[iy][ix][1] == 'H' and kud():
        print('True-Horse')
        return True
    else :
        print('False-Horse')
        return False
#checks if queen is choosen
def Queen():

    if Grid[iy][ix][1] == 'Q' and (ner() or kon()):
        print('True-Queen')
        return True
    else :
        print('False-Queen')
        return False
#checks if pawn is choosen
def Pawn():

    if Grid[iy][ix][1] == 'P' and kal():
        print('True-Pawn')
        return True
    else :
        print('False-Pawn-else')
        return False
#checks if king is choosen    
def King():

    if Grid[iy][ix][1] == 'K' and raj():
        print('True-King')
        return True
    else :
        print('False-King')
        return False    





#checking the diff b/w intial and final position 
def diff():
    global x,y,qwert,qwerty
    if ix >= fx:
        x=ix-fx
        qwert=1
    elif fx >= ix:
        x=fx-ix
        qwert=0
    if iy >= fy:
        y=iy-fy
        qwerty=1
    elif fy >= iy:
        y=fy-iy
        qwerty=0





def if_check(z):
    if z=='.':
        print('no obstacle')
        print(z)
        return True
    else:
        print('Obstacle')
        return False
        




#checking for pices in the path of pices
def move_check(): 
    global x,y,qwert,qwerty   
    diff()       
    if x==0 and qwerty == 0:
        for i in range(1,y+1):
            return if_check(Grid[iy+i][ix])       
    elif y==0 and qwert==0:
        for i in range(1,x+1):
            return if_check(Grid[iy][ix+i])
    elif x==0 and qwerty == 1:
        for i in range(1,y+1):
            return if_check(Grid[iy-i][ix])        
    elif y==0 and qwert == 1:
        for i in range(1,x+1):
            return if_check(Grid[iy][ix-i]);     
    elif qwert == 0 and qwerty == 0:
        for i in range(1,x+1):
            return if_check(Grid[iy+i][ix+i])
    elif qwert == 0 and qwerty == 1:
        for i in range(1,x+1):
             return if_check(Grid[iy-i][ix+i])
    elif qwert == 1 and qwerty == 0:
        for i in range(1,y+1):
            return if_check(Grid[iy+i][ix-i])
    elif qwert == 1 and qwerty== 1:
        for i in range(1,y+1):
            return if_check(Grid[iy-i][ix-i])





#commending to move 
def move():
        print(Grid[iy][ix])
        Grid[fy][fx] = Grid[iy][ix]
        print(Grid[fy][fx])
        Grid[iy][ix] = '.'





#collecting details to move
def ini_move():
    global ix,iy,fx,fy,a,b,c,d,im


    print ('Enter final position:')
    fy=int(input('Y='))
    fx=int(input('X='))
 
    a=(ix - fx)
    b=(iy - fy)
    c=(fx - ix)
    d=(fy - iy)

    print(Grid[iy][ix][1])
    #moving rook
    if Rook() and move_check():
        move()
        im = True
    #moving bishop
    elif Bishop() and move_check():
        print('move-b-check')
        move()
        im = True
    #moving knight
    elif Horse():
        print('move-h-check')
        move()
        im = True
    #moving queen
    elif Queen() and move_check():
        print('move-q-check')
        move()
        im = True
    #moving pawn
    elif Pawn() and move_check():
        print('move-p-check')
        move()
        im = True
    #moving king
    elif King() and move_check():
        print('move-k-check')
        move()
        im = True
    else:
        im = False





#checking for check mate
def check_mate():
    return False


moves=1


int_Grid()
print_grid()
#continues till mate
while check_mate() == False:
    print ('Enter initial position:')
    iy=int(input('Y='))
    ix=int(input('X='))

    print(Grid[iy][ix])

    if moves %2 == 1 and Grid[iy][ix][0] == 'W' :
        ini_move()
        moves=moves+1
    elif moves %2 == 0 and Grid[iy][ix][0] == 'B' :
        ini_move()
        moves=moves+1
    else:
        print('invalid selection')
    if im == False:
        moves = moves -1
    print_grid()