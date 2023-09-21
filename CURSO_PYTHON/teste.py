def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
       return leap
    else:
        if year % 400 == 0:
            return leap

    
    return leap

year = int(input())
print(is_leap(year))