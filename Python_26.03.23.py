
num_1  = int(input('Enter number 1: '))
num_2  = int(input('Enter number 2: '))

for i in range(num_1,num_2+1):
    if i %3 ==0 %5 ==0:
        print ("Fizz Buzz")
    elif i %3 ==0:
        print("Fizz")
    elif i %5 ==0:
        print("Buzz")
    else:
        print(i)