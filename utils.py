
def find_max(list):
    largest_number = list[0]
    for number in list:
        if number > largest_number:
            largest_number = number
    return largest_number