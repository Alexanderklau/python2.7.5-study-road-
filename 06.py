def search(sequace, number, lower, upper):
    if lower == upper:
        assert  number == sequace[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequace[middle]:
            return  search(sequace,number,middle + 1,upper)
        else:
            return search(sequace,number,lower,middle)
