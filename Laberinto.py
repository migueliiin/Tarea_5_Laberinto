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

def buscar_mover(x1,y1,ult):
    salir=False
    mov=1
    while(salir==False):
        if(mov==1 and ult != 3 and x1+1<5):
            if(laberinto[x1+1][y1] in (' ','s')):
                salir=True
        elif(mov==2 and ult != 4 and y1+1<5):
            if(laberinto[x1][y1+1] in (' ','s')):
                salir=True
        elif(mov==3 and ult != 1 and x1-1>-1):
            if(laberinto[x1-1][y1] in (' ','s')):
                salir=True
        elif(mov==4 and ult != 2 and y1-1>-1):
            if(laberinto[x1][y1-1] in (' ','s')):
                salir=True
        elif(mov>4):
            salir=True
        mov = mov + 1
    if(mov-1 in [1,2,3,4]):
        return mov-1
    else:
        return 0


def mover(x1,y1,mov):
    global x
    global y
    camino.append(mov)
    if(mov==1):
        x=x1+1
    elif(mov==2):
        y=y1+1
    elif(mov==3):
        x=x1-1
    elif(mov==4):
        y=y1-1
    else:
        print("DEL 1 al 4")


def main():

    salir = False
    ult = 0

    while(salir == False):
        mov=buscar_mover(x,y,ult)
        ult=mov
        if(mov in [1,2,3,4]):
            mover(x,y,mov)
        if(laberinto[x][y] == 's'):
            salir = True

    print("El laberinto es el siguiente:")
    for i in range(0, 5):
        print("|",end="")
        for j in range(0, 5):
            print(laberinto[i][j]," ",end="")
        print("|")

    print("Esta es la solucion al laberinto")
    print("( ",end="")
    for i in range(0, len(camino)):
        if(camino[i]==1):
            print("Abajo ,",end="")
        elif(camino[i]==2):
            print("Derecha ,",end="")
        elif(camino[i]==3):
            print("Arriba ,",end="")
        elif(camino[i]==4):
            print("Izquierda ,",end="")

    print("FIN )")

if __name__ == "__main__":
    main()