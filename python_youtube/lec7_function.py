# def calsum(a,b):
    
#     sum = a+b
 
#     print(sum)


# calsum(2,3)

# def calavg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg


# calavg(2,3,1)

def calproduct(a=1,b=1): # by default value one hai 
    print(a*b)
    return a+b

calproduct()

def calproduct(a,b=1): # by default value one hai b ki ab ham only a ki value pass kara skte hai
    print(a*b)
    return a+b

calproduct(2)