def fizzbuzz(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        return "Invalid input"

    newlist = a+b
    mylist = len(newlist)

    if(mylist % 5 == 0 and mylist % 3 == 0):
        return "fizzbuzz"

    if (mylist % 5 == 0):
        return "buzz"

    if (mylist % 3 == 0):
        return "fizz"

    return len(newlist)
