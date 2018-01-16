A=[[1,2,3],[1,2,3],[1,2,3]]
satirboy=len(A)
sutunboy=len(A[0])
if (satirboy==sutunboy):
     B=[]
     köşegen_toplamı=0
     for i in range(satirboy):
         köşegen_toplamı=köşegen_toplamı+A[i][i]+A[i][satirboy-1-i]
         for i in range(satirboy):
             satir=[]
             for j in range(sutunboy):
                 x=A[i][j]-köşegen_toplamı
                 satir.append(x)
                 B.append(satir)
                 print(B)
else:
    print("Matris kare degildir.")
