text=input("please enter a massage: ")
key=input("please enter a key: ")
result=""
length_key=len(key)
for i in range(len(text)):
    a=i%length_key
    k=key[a]
    t=text[i]
    print("text: ",t,"key: ",k)
    
    ascii_t=ord(t)
    ascii_k=ord(k)
    s=(ascii_t+ascii_k)%120
    c=chr(s)
    print("ascii t: ",ascii_t,"ascii k: ",ascii_k,"s: ",s,"c: ",c)
    result=result+c
    print("result: ",result)
    
print(result)    
    



    


