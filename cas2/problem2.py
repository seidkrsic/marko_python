


def num_of_even(a):
    x=0
    for numbers in a:
        if numbers%2 == 0:
            x+=1

    return x


print(num_of_even([1,2,3,4,5,6]))