s = input('Input : ')
broken_s = s.split(' ')
reverse_s= ''
for i in broken_s :
    j =-1
    for k in i :
        reverse_s+=i[j]
        j-=1
    reverse_s+=' '
print("Output :",reverse_s)
