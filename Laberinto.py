laberinto=  [
    ['e','x','x','x','x'],
    [' ','x',' ',' ',' '],
    [' ','x',' ','x',' '],
    [' ',' ',' ','x',' '],
    ['x','x','x','x','s']
    ]

# muro= ((0,1),(0,2),(0,3),(0,4),(1,1),(2,1),(2,3),(3,3),(4,0),(4,1),(4,2),(4,3))

# 1=arriba 2=derecha 3=abajo 4=izquierda
camino = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

def main():
    x=0
    y=0
    for i in range(0, 5):
        for j in range(0, 5):
            print(i,j,"   ",laberinto[i][j])
        print()




if __name__ == "__main__":
    main()