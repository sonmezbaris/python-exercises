
#Prints the number in matrix form
def print_numbers(number):
    for i in range(1,number+1):
        for j in range(1, number+1):
            print(i,end=" ") 
        print()


number=int(input("please enter a number"))

if number%2==0:
    print_numbers(number+1)
else:
    print_numbers(number-1)


