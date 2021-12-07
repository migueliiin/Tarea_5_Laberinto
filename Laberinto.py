laberinto=  [
    ['e','x','x','x','x'],
    [' ','x',' ',' ',' '],
    [' ','x',' ','x',' '],
    [' ',' ',' ','x',' '],
    ['x','x','x','x','s']
    ]

# muro= ((0,1),(0,2),(0,3),(0,4),(1,1),(2,1),(2,3),(3,3),(4,0),(4,1),(4,2),(4,3))

# 1=abajo 2=derecha 3=arriba 4=izquierda
camino = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

x=0
y=0

def mover(x,y,mov):
    if(mov==1):
        x=x+1
    elif(mov==2):
        y=y+1
    elif(mov==3):
        x=x-1
    elif(mov==4):
        y=y-1
    else:
        print("DEL 1 al 4")


def main():


    for i in range(0, 5):
        for j in range(0, 5):
            print(i,j,"   ",laberinto[i][j])
        print()
    
    while(laberinto[x][y]=='s'):







if __name__ == "__main__":
    main()