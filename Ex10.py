x = 1
while x <= 5:  
    y = 1
    while y <= 5:
        if y % 2 != 0:
            print(y," ", end="")
        else:
            print("*", " ", end="")
        y += 1  
        
    print("\n")  
    x += 1  
    
'''
1  *  3  *  5

1  *  3  *  5

1  *  3  *  5

1  *  3  *  5

1  *  3  *  5
'''    