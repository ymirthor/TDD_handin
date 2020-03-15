class NegativeNotAllowed(Exception):
    pass

def add(numbers):
    if not numbers:
        return 0

    user_split = "\n"
    if numbers[:2] == "//":
        user_split = numbers[2]
        numbers = numbers[4:]
    
    list_not_allowed = []
    
    list_numbers = numbers.replace(user_split, ",").replace("\n", ",").split(",")
    list_numbers = [int(x) if int(x) >= 0 else list_not_allowed.append(x) for x in list_numbers]
    
    if list_not_allowed:
        raise NegativeNotAllowed("Negatives not allowed:" + ",".join(list_not_allowed))

    ret_val = sum([x for x in list_numbers if x <= 1000])

    return ret_val
