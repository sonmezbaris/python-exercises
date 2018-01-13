def sum6to7(liste):
    
 toplam=0
 i=0
 j=0
 boy=len(liste)
 altiyer=liste.index(6)
 yediyer=liste.index(7)
 while i<altiyer:
     toplam=toplam+liste[i]
     i=i+1
     j=j+yediyer-altiyer
     i=i+j+1
 while i<boy:
     toplam=toplam+liste[i]
     i=i+1
 return toplam
