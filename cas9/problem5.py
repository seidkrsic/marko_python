

# najvecu cifru u broju rekurzivno 


def max_digit(n): 
    if n == 0: 
        return 0 
    else: 
        last_digit = n % 10 
        reminder_of_number = n // 10 
        if last_digit > max_digit(reminder_of_number): 
            return last_digit 
        else: 
            return max_digit(reminder_of_number) 

print(max_digit(523)) 