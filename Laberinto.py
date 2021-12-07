x=0
y=0

laberinto=  [
    ['e','x','x','x','x'],
    [' ','x',' ',' ',' '],
    [' ','x',' ','x',' '],
    [' ',' ',' ','x',' '],
    ['x','x','x','x','s']
    ]

# 1=abajo 2=derecha 3=arriba 4=izquierda
camino = []

def buscar_mover(x,y):
    salir=False
    mov=1
    while(salir==False):
        if(mov==1 and laberinto[x+1][y]==' ' and x+1<5 ):
            salir=True
        elif(mov==2 and laberinto[x][y+1]==' ' and y+1<5):
            salir=True
        elif(mov==3 and laberinto[x-1][y]==' ' and x-1>-1):
            salir=True
        elif(mov==4 and laberinto[x][y-1]==' ' and y-1>-1):
            salir=True
        else:
            salir=True
    if(mov in [1,2,3,4]):
        return mov
    else:
        return 0


def mover(x1,y1,mov):
    global x
    global y
    camino.append(mov)
    if(mov==1):
        x=x1+1
        print("mueve ",mov, " x =",x)
    elif(mov==2):
        y=y1+1
        print("mueve ",mov, " x =",x)
    elif(mov==3):
        x=x1-1
        print("mueve ",mov, " x =",x)
    elif(mov==4):
        y=y1-1
        print("mueve ",mov, " x =",x)
    else:
        print("DEL 1 al 4")


def main():

    salir = False

    while(salir == False):
        mov=buscar_mover(x,y)
        print("-----",mov, " x =",x," y = ",y)
        if(mov in [1,2,3,4]):
            mover(x,y,mov)
        if(laberinto[x][y] == 's'):
            salir = True


        
    for i in range(0, 1):
        print(i,"   ",camino[i])



if __name__ == "__main__":
    main()