


def broj_samoglasnika(n): 
    if len(n) == 0: 
        return 0 
    else: 
        if n[0] in "aeiou": 
            return 1 + broj_samoglasnika(n[1:]) 
        else: 
            return 0 + broj_samoglasnika(n[1:]) 

result = broj_samoglasnika("ja volim python aaa") 
print(result) # 4 

