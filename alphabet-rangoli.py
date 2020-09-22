def print_rangoli(size):
    # your code goes here
    
    width = 2 * (size * 2 -1) - 1
    
    # To make list of alphabets
    a = [chr(i) for i in range(96+size,96,-1)]

    # Assigning alphabets like [['b'],['b','a']]
    b = [a[:i+1] for i,v in enumerate(a) ]

    # Joining data like ['b','b-a-b'] for the design
    c = ["-".join(v+b[i][:i][::-1]) for i,v in enumerate(b)]

    #printing out all the elements in the list using center for align
    for i in range(size,-size-1,-1):
        if i > 0 :

            print(c[size-i].center(width,"-"))
        elif i < -1:
            print(c[i].center(width,"-"))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
