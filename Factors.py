def Factors(num):
    Factors_list = []
    for i in range(1,num):
        if (num%i ==0):
            Factors_list.append(i)
    return Factors_list

