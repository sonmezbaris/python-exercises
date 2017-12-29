
def print_numbers(number):
    print(number)



number=int(input("please enter a number"))
if number%2==0:
    print_numbers(number+1)
else:
    print_numbers(number-1)
    

