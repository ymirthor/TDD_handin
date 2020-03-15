def add(numbers):
    if not numbers:
        return 0
        
    list_numbers = numbers.split(",")
    ret_val = sum([int(x) for x in list_numbers])

    return ret_val