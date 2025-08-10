x = 1
while x <= 5:  
    y = 2
    while y <= x:
        print(x, " ",end="")
        y += 1  
        
    print(f"{x}\n")  
    x += 1 
    
'''
1

2  2

3  3  3

4  4  4  4

5  5  5  5  5
'''    