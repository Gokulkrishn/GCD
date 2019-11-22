def GCD(num1,num2):
    if num2>num1:
        (num2,num1) = (num1,num2)
    for i in range(num2+1,0,-1):
        if (num1%i==0 and num2%i==0):
            return i

print(GCD(3,15))