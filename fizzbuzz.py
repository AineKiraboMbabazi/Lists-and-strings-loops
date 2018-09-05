def fizzbuzz(list1,list2):
    if not (isinstance(list1,list) and isinstance(list2,list)):
        return 'please enter lists only'
    else:
        newlist=list1+list2
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




if __name__ == "__main__":
    a=[1,2,3]
    b=[]
    c=[4]
    d=[1,1,2,3,5,6,7,8,9,0]
    e=[1,2,3,4]
    f=[1,2,3,4,5]
    print(fizzbuzz(a,b))
    print(fizzbuzz(c,e))
    print(fizzbuzz(d,f))
    print(fizzbuzz(e,b))
    
   