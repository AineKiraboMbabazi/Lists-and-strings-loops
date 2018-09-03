def vowel_count(txt):
    vowels='aeiou'
    newtxt=txt.lower()
    noduplicates=set(newtxt)
    duplication=len(newtxt)-len(noduplicates)
    vowelstring=""

    for i in vowels:
         if i in noduplicates:
            vowelstring+=str(i)

    
    return (vowelstring,duplication)




if __name__ == "__main__":
   
    teststring=input("Enter string: ")
  
    print(vowel_count(teststring))
