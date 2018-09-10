def fizzbuzz(a,b):
    if not (isinstance(a,list) and isinstance(b,list)):
        return "Invalid input"
    else:
        newlist=a+b
        mylist=len(newlist)
        if(mylist%5==0 and mylist%3==0):
            message="fizzbuzz"
            
        
        elif (mylist%5==0):
            message="buzz"
            
        elif (mylist%3==0):
            message="fizz"
            
        else:
            message=len(newlist)
        return message





   