oku=open("kelimeler.txt","r")
yaz=open("sonuc.txt","w")
liste=oku.readlines()
for i in range(len(liste)):
    if (len(liste[i])-2)>=i:
        yaz.write("1\n")
    else:
        yaz.write("o\n")
oku.close()
yaz.close()
