
num_1  = int(input('Enter number 1: '))
num_2  = int(input('Enter number 2: '))
if num_1 > num_2:
    num_1,num_2=num_2,num_1  
for i in range(num_1, num_2+1):
    if i % 2 !=0:
        print(i)
 
