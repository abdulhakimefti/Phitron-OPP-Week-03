def exp(a,n):
    return pow(a,n)
print('Example input: ')
a = input('>> enter numbers: ')
int_a = int(a.split(' ')[0])
int_n = int(a.split(' ')[1])
result = exp(int_a,int_n)
print('Example Output:')
print(">> result is : ",result)
