def result(text):
    count=0
    for i in range(len(metin)):
        if(ord(metin[i])>=65 and ord(metin[i])<=90):
            count=count+1
    return count       
