

def get_number():
    number=int(input("Please enter a number: "))
    return number


def get_operator():
    operator=input("Do you want to sum/multiply: ")
    return operator


def should_continue():
    decision=input("Do you want to continue yes/no: ")
    return decision


decision="yes"
sum=0
multiply=1
while decision=="yes":
    number=get_number()
    operator=get_operator()
    if operator=="sum":
        sum=sum+number
    elif operator=="multiply":
        multiply=multiply*number
    else:
        print("operator ",operator," not supported ")
    decision=should_continue()
print("sum=",sum,"multiply",multiply)    
        





    
