

num_1  = int(input('Enter number 1: '))
num_2  = int(input('Enter number 2: '))
counter = 0
for i in range(num_1, num_2+1):
        print(i)
print('\n')
for i in range(num_2, num_1-1, -1):
        print(i)
print('\n')
for i in range(num_1, num_2+1):
     if i %7 ==0:
         print(i)
print('\n')
for i in range(num_1, num_2+1):
    if i %5 ==0:
        counter += 1
print(counter)