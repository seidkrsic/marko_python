

""" 
naci zbir cifara broja n. 

n = 2024 
zbir je 2+0+2+4 

"""
# #    0123 
# n = "2024" 
# sum = 0
# for i in n: 
#     sum += int(i)   # i = "2" int(i) --> 2 
# print(sum)  

def sum_of_digits(n): 
    if n == 0: 
        return 0 
    else: 
        return (n % 10) + sum_of_digits(n//10) 
    
    # sum_of_digits(123) ------ 3 + sum_of_digits(12) .... 3 + 3 = 6
    # sum_of_digits(12)         2 + sum_of_digits(1)  .... 2 + 1 = 3 
    # sum_of_digits(1)          1 + sum_of_digits(0)   ... 1 + 0 = 1 
    # sum_of_digits(0)          0 

print(sum_of_digits(555)) 