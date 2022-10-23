print('Example input: ')
floatInput = input('>> enter numbers: ')
broken_input = floatInput.split('-')
sum = 0
for n in broken_input:
    sum+=float(n)
print('Example Output:')
print(">> result is : ",sum)