#!/usr/bin/python3

if __name__ == "__main__":
    a = list(map(int,input("").split()))

    column = a[0]
    row = a[1]

    for i in range(1,column,2):

        txt = ".|." * i
        print(txt.center(row,"-"))

    print("WELCOME".center(row,"-"))
    
    for i in range(column-2,0,-2):

        txt = ".|." * i
        print(txt.center(row,"-"))
